import os
from dotenv import load_dotenv
from google import genai
import argparse
from google.genai import types

def main():
   load_dotenv()
   
   api_key = os.environ.get("GEMINI_API_KEY")
   if api_key is None:
      raise RuntimeError('No API Key was found')
   client = genai.Client(api_key=api_key)
   parser = argparse.ArgumentParser(description="Chatbot")
   parser.add_argument("user_prompt", type=str, help="User prompt")
   parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
   args = parser.parse_args()
   
   messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]
   # Now we can access `args.user_prompt`
   response = client.models.generate_content(model='gemini-2.5-flash', contents=messages)
   if response.usage_metadata is None:
      raise RuntimeError('failed api request (failed to get the tokens for prompts and responses)')
   if args.verbose:
      prompt_tokens = response.usage_metadata.prompt_token_count
      response_tokens = response.usage_metadata.candidates_token_count
      print(f"User prompt: {args.user_prompt}")
      print(f"Prompt tokens: {prompt_tokens}")
      print(f"Response tokens: {response_tokens}")
   print(response.text)
      
      


if __name__ == "__main__":
    main()
