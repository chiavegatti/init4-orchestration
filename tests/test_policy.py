import pytest
from src.policy.engine import PolicyEngine
from src.policy.rules import ROUTING_RULES, FALLBACK_RULES


def test_strict_override_force_local():
    """
    Test that force_local bypasses standard matching and routes to default_local.
    """
    payload = {
        "metadata": {
            "task_type": "reasoning",  # Usually deepseek-chat
            "force_local": True,
        }
    }
    routed_model = PolicyEngine.determine_route(payload)
    assert routed_model == ROUTING_RULES["default_local"]


def test_rule_matching_extraction():
    """
    Test that valid task types map to their expected model.
    """
    payload = {"metadata": {"task_type": "extraction"}}
    routed_model = PolicyEngine.determine_route(payload)
    assert routed_model == ROUTING_RULES["extraction"]


def test_rule_matching_reasoning():
    """
    Test that complex tasks map appropriately to their cloud equivalents.
    """
    payload = {"metadata": {"task_type": "reasoning"}}
    routed_model = PolicyEngine.determine_route(payload)
    assert routed_model == ROUTING_RULES["reasoning"]


def test_default_fallback_unknown_task():
    """
    Test that an unknown task_type routes to the default_cloud.
    """
    payload = {"metadata": {"task_type": "quantum_calculation"}}  # Unknown task
    routed_model = PolicyEngine.determine_route(payload)
    assert routed_model == ROUTING_RULES["default_cloud"]


def test_missing_metadata_goes_to_default_cloud():
    """
    Test that requests with no metadata or empty metadata route to default_cloud.
    """
    payload_empty = {}
    routed_model = PolicyEngine.determine_route(payload_empty)
    assert routed_model == ROUTING_RULES["default_cloud"]


def test_get_fallback_model_success():
    """
    Test fallback logic returning the correct mapped fallback model.
    """
    # Test fallback for local model
    local_model = ROUTING_RULES["default_local"]
    fallback = PolicyEngine.get_fallback_model(local_model)
    assert fallback == FALLBACK_RULES[local_model]

    # Test fallback for fallback model (chaining)
    next_fallback = PolicyEngine.get_fallback_model(fallback)
    assert next_fallback == FALLBACK_RULES[fallback]


def test_get_fallback_model_none():
    """
    Test fallback logic on a model that has no registered fallback.
    """
    model_without_fallback = "some-weird-model"
    fallback = PolicyEngine.get_fallback_model(model_without_fallback)
    assert fallback is None
