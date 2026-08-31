from textwrap import dedent
from openai import OpenAI
from django.conf import settings

class TopicGenerator():

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
        Return an array of exactly 10 objects.

        The name of each object should be a random topic of interest.

        Each object must follow this schema:

        {"name": string}

        The final output must look like:

        [
            {"name": "..."},
            {"name": "..."},
            ...
        ]

    """)

    base_exclude = "Don't include these topics: "

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
            extra_body={"thinking": {"type": "enabled"}}
        )

        text_response = response.choices[0].message.content
        self.response = text_response

    def test_ai_call(self):
        # Important data
        api_key = settings.API_KEY
        bot_identity = "You are a helpful assistant."
        model = {
            "pro": "deepseek-v4-pro",
            "flash": "deepseek-v4-flash"
        }

        # Prompt
        prompt = "Hello"

        client = OpenAI(
            api_key= api_key,
            base_url="https://api.deepseek.com")

        response = client.chat.completions.create(
            model=model["flash"],
            messages=[
                {"role": "system", "content": bot_identity},
                {"role": "user", "content": prompt},
            ],
            stream=False,
            reasoning_effort="high",
            extra_body={"thinking": {"type": "enabled"}}
        )

        text_response = response.choices[0].message.content
        print(text_response)