def route_to_agent(user_input: str) -> str:
    """
    Simple routing logic.
    Later this becomes advanced multi-agent routing.
    """

    user_input_lower = user_input.lower()

    if "security" in user_input_lower or "vulnerability" in user_input_lower:
        return f"""
        You are AOVOX Security Agent.
        Provide a structured cybersecurity-focused answer.

        User Query:
        {user_input}
        """

    elif "research" in user_input_lower:
        return f"""
        You are AOVOX Research Agent.
        Provide deep analytical and structured insights.

        User Query:
        {user_input}
        """

    else:
        return f"""
        You are AOVOX General Intelligence Agent.
        Provide a clear and intelligent response.

        User Query:
        {user_input}
        """
