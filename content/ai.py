from textwrap import dedent
from openai import OpenAI
from django.conf import settings

class TopicGenerator():
    base_prompt = dedent("""
        Return an array of exactly 10 objects.

        The name of each object should be a random topic of interest.

        Each object must follow this schema:

        { "name": string }

        The final output must look like:

        [
            { "name": "..." },
            { "name": "..." },
            ...
        ]
    """)

    base_exclude = "Don't include these topics: "

    def __init__(self, exclude):
        self.exclude = self.base_exclude + exclude

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