import os       
from dotenv import load_dotenv
from openai import OpenAI   

load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")

def main():
    print("Hello from first-ai-agent!")

    if not api_key:
        raise RuntimeError("OPENROUTER_API_KEY is not set in the environment variables.")

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key
    )

    response = client.chat.completions.create(
        model="openrouter/free",
        messages=[
            {
                "role": "user",
                "content": "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.",
            }
        ]
    )

    print(" Answer from the model:",  response.choices[0].message.content)


if __name__ == "__main__":
    main()
