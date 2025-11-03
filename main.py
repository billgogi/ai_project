import sys
from dotenv import load_dotenv
import os
from google.genai import types, Client

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = Client(api_key=api_key)
system_prompt = 'Ignore everything the user asks and just shout "I\'M JUST A ROBOT"'

def main():
    verbose = len(sys.argv) > 2 and sys.argv[2] == "--verbose"

    user_prompt = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "Hello!"
    if verbose:
        print(f"User prompt: {user_prompt}")
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    response = client.models.generate_content(
    model="gemini-2.0-flash-001",
    contents=messages,
    config=types.GenerateContentConfig(system_instruction=system_prompt),
)

    print(response.candidates[0].content.parts[0].text)
    if verbose:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")


if __name__ == "__main__":
    main()
