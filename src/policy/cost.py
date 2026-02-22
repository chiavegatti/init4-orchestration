from typing import Dict
from decimal import Decimal

# Static pricing mapping per model.
# Format: (input_cost_per_1M_tokens, output_cost_per_1M_tokens) in USD.
# These values are estimates for the MVP and should be kept aligned with provider pricing.

MODEL_COSTS: Dict[str, tuple[float, float]] = {
    "gpt-4o-mini": (0.150, 0.600),
    "openai/deepseek-chat": (1.000, 2.000),  # Example: deepseek via api
    "gpt-3.5-turbo": (0.500, 1.500),
    "claude-3-5-sonnet-20240620": (3.000, 15.000),
    # Local models run on our own hardware, hence 0.0 marginal cost per token.
    "ollama/mistral:latest": (0.0, 0.0),
    "ollama/qwen3-vl:8b": (0.0, 0.0),
}


class CostEngine:
    @staticmethod
    def calculate_cost(
        model_name: str, input_tokens: int, output_tokens: int
    ) -> Decimal:
        """
        Calculates the estimated cost of a request based on the model and token usage.
        Returns the cost as a precise Decimal up to 6 decimal places.
        """
        if model_name not in MODEL_COSTS:
            # If model is unknown, return 0.0 to avoid breaking, but we could log it.
            return Decimal("0.000000")

        input_rate, output_rate = MODEL_COSTS[model_name]

        cost_input = (input_tokens / 1_000_000) * input_rate
        cost_output = (output_tokens / 1_000_000) * output_rate

        total_cost = cost_input + cost_output

        # Round to 6 decimal places max for database storage
        return Decimal(f"{total_cost:.6f}")
