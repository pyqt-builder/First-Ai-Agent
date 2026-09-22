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

   