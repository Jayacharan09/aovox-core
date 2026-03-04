"""
Agent Routing Logic
"""

class GeneralAgent:
    def execute(self, user_input: str) -> str:
        return f"Processed by General Agent: {user_input}"


class AgentRouter:

    def get_agent(self, intent: str):
        # Future: advanced routing logic
        return GeneralAgent()
