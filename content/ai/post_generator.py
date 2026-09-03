from textwrap import dedent
from openai import OpenAI
from django.conf import settings

class PostGenerator():

    api_key = settings.API_KEY
    base_url="https://api.deepseek.com"

    model = {
        "pro": "deepseek-v4-pro",
        "flash": "deepseek-v4-flash"
    }

    role = dedent("""
        You are a JSON-only generator.
        You MUST output only valid JSON.
        No prose, no explanation, no markdown.
        If you cannot answer, return {"error": "unable to comply"}.
    """)

    base_prompt = dedent("""
        Return exactly 3 article objects in a JSON array.

        All articles must be on the same topic but clearly different in angle.

        Each object must follow this schema:
        {
        "title": string,
        "description": string,
        "text": string
        }

        Content rules:
        - Unique, interesting title.
        - Short description.
        - 3 paragraphs in "text", separated by "\n\n".

        The final output must look like:
        [
            {"title": "...", "description": "...", "text": "..."},
            {"title": "...", "description": "...", "text": "..."},
            ...
        ]
    """)

    base_exclude = "Don't include articles too similar to the following titles: "

    def __init__(self, exclude):
        self.exclude = self.base_exclude + exclude
        self.response = ""

    def real_ai_call(self):
        client = OpenAI(
            api_key= self.api_key,
            base_url=self.base_url)

        response = client.chat.completions.create(
            model=self.model["flash"],
            messages=[
                {"role": "system", "content": self.role},
                {"role": "user", "content": self.base_prompt + self.exclude},
            ],
            stream=False,
            reasoning_effort="high",
            extra_body={"thinking": {"type": "disabled"}}
        )

        text_response = response.choices[0].message.content
        self.response = text_response