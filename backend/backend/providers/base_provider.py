from abc import ABC, abstractmethod


class BaseProvider(ABC):
    """
    Abstract base class for all AI providers.
    Every provider must implement the generate method.
    """

    @abstractmethod
    def generate(self, prompt: str) -> str:
        pass
