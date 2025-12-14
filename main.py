import os
from dotenv import load_dotenv
from google import genai
import argparse


def main():
   load_dotenv()
   
   api_key = os.environ.get("GEMINI_API_KEY")
   if api_key is None:
       raise RuntimeError('No API Key was found')
   client = genai.Client(api_key=api_key)
   parser = argparse.ArgumentParser(description="Chatbot")
   parser.add_argument("user_prompt", type=str, help="User prompt")
   args = parser.parse_args()
   
   # Now we can access `args.user_prompt`
   response = client.models.generate_content(model='gemini-2.5-flash', contents=args.user_prompt)
   if response.usage_metadata is None:
       raise RuntimeError('failed api request (failed to get the tokens for prompts and responses)')
   prompt_tokens = response.usage_metadata.prompt_token_count
   response_tokens = response.usage_metadata.candidates_token_count
   print(f"Prompt tokens: {prompt_tokens}")
   print(f"Response tokens: {response_tokens}")
   print(response.text)
      
      


if __name__ == "__main__":
    main()
