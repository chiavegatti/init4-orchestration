import pytest
from decimal import Decimal
from src.policy.cost import CostEngine


def test_cost_calculation_local_model():
    """Local models should always return 0.0 cost."""
    cost = CostEngine.calculate_cost("ollama/mistral:latest", 5000, 2000)
    assert cost == Decimal("0.000000")


def test_cost_calculation_cloud_model():
    """Test cost calculation with gpt-4o-mini rates."""
    # rates: 0.15 per 1M in, 0.60 per 1M out
    # 100,000 in (0.015) + 50,000 out (0.030) = 0.045
    cost = CostEngine.calculate_cost("gpt-4o-mini", 100000, 50000)
    assert cost == Decimal("0.045000")


def test_cost_calculation_unknown_model_fallback():
    """Test that a model not in the dictionary defaults to 0 safely."""
    cost = CostEngine.calculate_cost("unknown-future-model", 1000, 1000)
    assert cost == Decimal("0.000000")
