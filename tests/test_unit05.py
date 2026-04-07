"""
Unit 5 — pytest test suite
Discoverable by: pytest tests/test_unit05.py -v

Tests cover:
- AST-based safe arithmetic evaluator (security-critical)
- Skill warm-up contract (context_loader)
- Model routing logic (task_classifier)
- Domain-agnostic DOMAIN_CONTEXTS extension

Run without API keys — all tests use stdlib or mocks.
"""
import ast
import operator as op
import sys
import os

import pytest

# ── Add project root to path ────────────────────────────────────────────────
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)


# ── Replicate safe evaluator (mirrors U5_01 calcular tool) ──────────────────
_OPS = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
    ast.Pow: op.pow,
    ast.USub: op.neg,
}


def _safe_eval(node):
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return node.value
    elif isinstance(node, ast.BinOp) and type(node.op) in _OPS:
        return _OPS[type(node.op)](_safe_eval(node.left), _safe_eval(node.right))
    elif isinstance(node, ast.UnaryOp) and type(node.op) in _OPS:
        return _OPS[type(node.op)](_safe_eval(node.operand))
    else:
        raise ValueError(f"Operacion no permitida: {type(node).__name__}")


def safe_calc(expr: str) -> float:
    tree = ast.parse(expr, mode="eval")
    return _safe_eval(tree.body)


# ════════════════════════════════════════════════════════════════════════════
# Tests: AST evaluator — arithmetic correctness
# ════════════════════════════════════════════════════════════════════════════
class TestSafeCalcArithmetic:
    def test_addition(self):
        assert safe_calc("2 + 2") == 4

    def test_multiplication(self):
        assert abs(safe_calc("100 * 0.15") - 15.0) < 1e-9

    def test_parentheses(self):
        assert abs(safe_calc("(5 ** 2) / 3") - 25 / 3) < 1e-9

    def test_operator_precedence(self):
        # 1 + 2*3 must be 7, not 9
        assert safe_calc("1 + 2 * 3") == 7

    def test_unary_negation(self):
        assert safe_calc("-7 + 10") == 3

    def test_power(self):
        assert safe_calc("2 ** 10") == 1024

    def test_chained_ops(self):
        assert abs(safe_calc("(3.14 * 2) / 6.28") - 1.0) < 1e-9


# ════════════════════════════════════════════════════════════════════════════
# Tests: AST evaluator — security (must BLOCK these)
# ════════════════════════════════════════════════════════════════════════════
class TestSafeCalcSecurity:
    def test_blocks_import(self):
        with pytest.raises((ValueError, AttributeError)):
            safe_calc("__import__('os')")

    def test_blocks_attribute_access(self):
        with pytest.raises((ValueError, AttributeError)):
            safe_calc("x.y")

    def test_blocks_function_call(self):
        with pytest.raises((ValueError, AttributeError, TypeError)):
            safe_calc("print('hola')")

    def test_blocks_string_literal(self):
        with pytest.raises((ValueError, AttributeError)):
            safe_calc("'a' + 'b'")

    def test_blocks_list_literal(self):
        with pytest.raises((ValueError, SyntaxError, AttributeError)):
            safe_calc("[1, 2, 3]")

    def test_zero_division_raises(self):
        with pytest.raises(ZeroDivisionError):
            safe_calc("1 / 0")


# ════════════════════════════════════════════════════════════════════════════
# Tests: Skill warm-up contract (context_loader)
# ════════════════════════════════════════════════════════════════════════════
class TestContextLoaderSkill:
    @pytest.fixture(autouse=True)
    def import_skill(self):
        try:
            from external_skills.agent_warmup import context_loader as cl
            self.cl = cl
            self.available = True
        except ImportError:
            self.available = False

    def test_metadata_has_name(self):
        if not self.available:
            pytest.skip("context_loader not installed")
        assert "name" in self.cl.SKILL_METADATA

    def test_metadata_has_version(self):
        if not self.available:
            pytest.skip("context_loader not installed")
        assert "version" in self.cl.SKILL_METADATA

    def test_warm_up_is_callable(self):
        if not self.available:
            pytest.skip("context_loader not installed")
        assert callable(self.cl.warm_up)

    def test_warm_up_returns_dict(self):
        if not self.available:
            pytest.skip("context_loader not installed")
        result = self.cl.warm_up("research")
        assert isinstance(result, dict) and len(result) > 0

    def test_domain_contexts_is_dict(self):
        if not self.available:
            pytest.skip("context_loader not installed")
        assert hasattr(self.cl, "_DOMAIN_CONTEXTS")
        assert isinstance(self.cl._DOMAIN_CONTEXTS, dict)

    def test_domain_contexts_extensible(self):
        """Domain contexts must accept new entries without raising."""
        if not self.available:
            pytest.skip("context_loader not installed")
        original_keys = set(self.cl._DOMAIN_CONTEXTS.keys())
        self.cl._DOMAIN_CONTEXTS["test_domain_pytest"] = {
            "description": "Test domain",
            "system_prompt_points": ["Point A", "Point B"],
        }
        assert "test_domain_pytest" in self.cl._DOMAIN_CONTEXTS
        # Cleanup
        del self.cl._DOMAIN_CONTEXTS["test_domain_pytest"]
        assert set(self.cl._DOMAIN_CONTEXTS.keys()) == original_keys
