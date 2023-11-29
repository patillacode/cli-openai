from dotenv import load_dotenv
from icecream import ic  # noqa: F401
from openai import OpenAI

load_dotenv()

client = OpenAI()

stream = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "user",
            "content": "Say this is a test, write a 20 word text poem about it.",
        }
    ],
    stream=True,
)
ic(stream)
for chunk in stream:
    ic(chunk)
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")
