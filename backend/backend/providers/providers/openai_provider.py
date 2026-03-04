import os
from openai import OpenAI
from .base_provider import BaseProvider


class OpenAIProvider(BaseProvider):
    """
    OpenAI implementation of BaseProvider.
    """

    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def generate(self, prompt: str) -> str:
        try:
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )

            return response.choices[0].message.content

        except Exception as e:
            return f"OpenAI Error: {str(e)}"
