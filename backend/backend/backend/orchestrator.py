"""
AOVOX Orchestration Engine
"""

class Orchestrator:

    def __init__(self):
        print("Orchestrator Initialized")

    def process(self, user_input: str) -> str:
        """
        Core orchestration pipeline
        """

        # Step 1: Analyze intent
        intent = self._analyze_intent(user_input)

        # Step 2: Select agent
        agent = self._select_agent(intent)

        # Step 3: Execute
        response = agent.execute(user_input)

        return response

    def _analyze_intent(self, user_input: str) -> str:
        return "general"

    def _select_agent(self, intent: str):
        from agent_router import AgentRouter
        router = AgentRouter()
        return router.get_agent(intent)
