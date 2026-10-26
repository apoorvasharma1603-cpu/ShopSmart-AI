import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

response = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[
        {
            "role": "system",
            "content": "You are a cheerful assistant for an online store. Reply in paragraph by explaining what you can do."
        },
        {
            "role": "user",
            "content": "Say hello and confirm you're working!"
        },
    ],
    temperature=1,
)

print(response.choices[0].message.content)

print("\n--- Token Usage ---")
print("Request tokens:", response.usage.prompt_tokens)
print("Reply tokens:", response.usage.completion_tokens)
print("Total tokens:", response.usage.total_tokens)

