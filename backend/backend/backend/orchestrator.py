from providers.provider_factory import get_provider
from agent_router import route_to_agent


class AOVOXOrchestrator:
    """
    Central brain of AOVOX.
    Decides:
    - Which agent to use
    - Which provider to use
    - How to execute the request
    """

    def __init__(self, provider_name: str = "openai"):
        self.provider = get_provider(provider_name)

    def process(self, user_input: str) -> str:
        """
        Main entry point for handling user input.
        """

        # Step 1: Determine which agent should handle this
        agent_prompt = route_to_agent(user_input)

        # Step 2: Send final prompt to AI provider
        response = self.provider.generate(agent_prompt)

        return response
