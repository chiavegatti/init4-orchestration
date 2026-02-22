from typing import Optional
from src.policy.rules import ROUTING_RULES, FALLBACK_RULES


class PolicyEngine:
    @staticmethod
    def determine_route(request_payload: dict) -> str:
        """
        Deterministically decides which model will serve a request.
        Prioritizes the `task_type` field in the `metadata` payload structure.
        """
        metadata = request_payload.get("metadata", {})
        task_type = metadata.get("task_type")
        force_local = metadata.get("force_local", False)

        # 1. Strict override
        if force_local:
            return ROUTING_RULES["default_local"]

        # 2. Rule matching
        if task_type and task_type in ROUTING_RULES:
            return ROUTING_RULES[task_type]

        # 3. Default fallback for unknown tasks (can be set to either local or cloud depending on cost preference)
        # Defaulting to cloud for safety in unknown intents until explicitly added to the local rules.
        return ROUTING_RULES["default_cloud"]

    @staticmethod
    def get_fallback_model(failed_model: str) -> Optional[str]:
        """
        Returns the appropriate fallback model for a given failed model according to the policy rules.
        If no distinct fallback is defined, returns None.
        """
        return FALLBACK_RULES.get(failed_model)
