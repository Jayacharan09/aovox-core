from .openai_provider import OpenAIProvider


def get_provider(provider_name: str):
    """
    Returns provider instance based on name.
    """

    if provider_name.lower() == "openai":
        return OpenAIProvider()

    raise ValueError(f"Unsupported provider: {provider_name}")
