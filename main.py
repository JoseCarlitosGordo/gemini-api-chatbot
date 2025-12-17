import os
from dotenv import load_dotenv
from google import genai
import argparse
from prompts import system_prompt
from google.genai import types
from function_declarations import available_functions
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
   response = client.models.generate_content(model='gemini-2.5-flash', contents=messages, config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt),)
   if response.usage_metadata is None:
      raise RuntimeError('failed api request (failed to get the tokens for prompts and responses)')
   if args.verbose:
      prompt_tokens = response.usage_metadata.prompt_token_count
      response_tokens = response.usage_metadata.candidates_token_count
      print(f"User prompt: {args.user_prompt}")
      print(f"Prompt tokens: {prompt_tokens}")
      print(f"Response tokens: {response_tokens}")
   if response.function_calls is not None:
      for call in response.function_calls:
         print(f"Calling function: {call.name}({call.args})\n")
   else:
      print(response.text)
      
      


if __name__ == "__main__":
    main()
