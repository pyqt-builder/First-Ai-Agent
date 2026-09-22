import os, argparse     
from dotenv import load_dotenv
from openai import OpenAI   


load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")



#generate_content()
#→ talks to the API
#→ extracts useful values
#→ returns them

def generate_content(client,messages):     
    response = client.chat.completions.create(
        model="openrouter/free",
        messages= messages
    )
    if response.usage is None:
            raise RuntimeError("No prompt tokens were used in the request. Please check your request and try again.")
    
    prompt_tokens = response.usage.prompt_tokens        
    response_tokens = response.usage.completion_tokens

    generated_content = response.choices[0].message.content

    return generated_content, prompt_tokens, response_tokens


#main()
#→ handles CLI input
#→ calls the helper
#→ prints results

def main():
    print("Hello from first-ai-agent!")

    if not api_key:
        raise RuntimeError("OPENROUTER_API_KEY is not set in the environment variables.")

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key
    )

    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="Message to send to the chatbot")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    generated_content, prompt_tokens, response_tokens = generate_content(client, [{"role": "user", "content": args.user_prompt}])


    
    if args.verbose:
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {prompt_tokens}")
        print(f"Response tokens: {response_tokens}")

    print("Answer from the model:", generated_content)
   
        


if __name__ == "__main__":
    main()
