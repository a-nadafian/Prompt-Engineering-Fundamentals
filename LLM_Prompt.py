import requests
import json
import os
from dotenv import load_dotenv
from openai import OpenAI, APIError
from openai.types.chat import ChatCompletionUserMessageParam

# Load environment variables from .env file
load_dotenv()

# --- CONFIGURATION ---
# 1. The script now reads the API key from .env file.
#    Make sure you have created a .env file with your key.
API_KEY = os.getenv("LLAMA_4")
MODEL_NAME = "meta-llama/llama-4-maverick:free"
API_URL = "https://openrouter.ai/api/v1"

# The text we want to analyze, taken directly from the blueprint.
TEXT_TO_ANALYZE = "Project leader Summer Rhodes informed Will Power that the documents from the Taylor Foundation were ready. She noted, 'The report from Dr. Stone is critical,' and asked him to check the latest figures from the Ford motor company before their meeting with Mr. Bill Gates."

# --- PROMPT DEFINITIONS ---

# Prompt A: Zero-Shot
ZERO_SHOT_PROMPT = f"""
Extract the names of all people from the following text. List them one per line.

Text: "{TEXT_TO_ANALYZE}"
"""

# Prompt B: One-Shot
ONE_SHOT_PROMPT = f"""
Extract the names of all people from the text.

Input: "The report was written by Mr. Alan Grant and reviewed by Sarah Connor."
Output:
Alan Grant
Sarah Connor
---
Input: "{TEXT_TO_ANALYZE}"
Output:
"""

# Prompt C: Few-Shot
FEW_SHOT_PROMPT = f"""
Extract the names of all people from the text.

Input: "The report was written by Mr. Alan Grant and reviewed by Sarah Connor."
Output:
Alan Grant
Sarah Connor
---
Input: "Please give the documents to Alice."
Output:
Alice
---
Input: "The main characters are Arthur Dent and Ford Prefect."
Output:
Arthur Dent
Ford Prefect
---
Input: "{TEXT_TO_ANALYZE}"
Output:
"""


def query_openrouter(prompt: str, prompt_type: str):
    """
    Sends a prompt to the OpenRouter API using the OpenAI SDK and prints the response.
    """
    print(f"--- Testing {prompt_type} Prompt ---")

    if not API_KEY:
        print("ERROR: API key not found. Please create a .env file and add your OPENROUTER_API_KEY.")
        return

    # Initialize the OpenAI client to connect to OpenRouter
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=API_KEY,
    )

    try:
        # Define the message with the specific type expected by the library to resolve the warning.
        messages: list[ChatCompletionUserMessageParam] = [
            {"role": "user", "content": prompt}
        ]

        completion = client.chat.completions.create(
            model=MODEL_NAME,
            messages=messages
        )

        model_response = completion.choices[0].message.content

        print("Model Response:")
        print(model_response)
        print("-" * 30 + "\n")

    except APIError as e:
        print(f"An API error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    print("Starting LLM Prompting Tests...\n")
    query_openrouter(ZERO_SHOT_PROMPT.strip(), "Zero-Shot")
    query_openrouter(ONE_SHOT_PROMPT.strip(), "One-Shot")
    query_openrouter(FEW_SHOT_PROMPT.strip(), "Few-Shot")
