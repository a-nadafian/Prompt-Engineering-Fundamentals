# LLM Prompting Techniques with OpenRouter

This project demonstrates various prompting techniques (Zero-Shot, One-Shot, and Few-Shot) for interacting with Large Language Models (LLMs) through the OpenRouter API. The `LLM_Prompt.py` script provides a clear, hands-on example of how to structure prompts to get different levels of contextual responses from an AI model.

## Features

- **Multiple Prompting Strategies:** See side-by-side examples of Zero-Shot, One-Shot, and Few-Shot prompting.
- **OpenRouter Integration:** Uses the `openai` library to connect to a wide range of models available on OpenRouter.
- **Easy to Configure:** Simply add your API key to a `.env` file to get started.
- **Clear and Educational:** The code is well-commented and designed to be a learning resource.

## Getting Started

Follow these instructions to get the project set up and running on your local machine.

### Prerequisites

- Python 3.6 or higher
- An API key from [OpenRouter](https://openrouter.ai/)

### Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2.  **Install dependencies:**
    Create a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
    Install the required packages from `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

### Obtaining Your OpenRouter API Key

1.  **Create an OpenRouter Account:**
    - Go to the [OpenRouter.ai](https://openrouter.ai/) website and sign up for an account.
    - You may need to add credits to your account to use certain models. Many models also have a free tier.

2.  **Generate an API Key:**
    - Once logged in, navigate to your **Account Settings** or **API Keys** section.
    - Click the button to create a new key.
    - Give your key a descriptive name (e.g., "LLM_Prompt_Project") and create it.

3.  **Copy Your Key:**
    - Your new API key will be displayed. **Copy it immediately**, as you may not be able to see it again for security reasons.

### Configure Your Environment

The script loads your API key from a `.env` file for security.

1.  **Create a `.env` file** in the root of the project directory.

2.  **Add your API key** to the `.env` file. The script expects the key to be named `LLAMA_4`:
    ```
    LLAMA_4="your_openrouter_api_key_here"
    ```
    Replace `"your_openrouter_api_key_here"` with the key you copied from OpenRouter.

## Usage

Once you have installed the dependencies and configured your API key, you can run the script:

```bash
python LLM_Prompt.py
```

The script will execute and print the responses from the language model for each of the three prompting techniques.

## Example Output

When you run the script, you will see output similar to the following:

```
Starting LLM Prompting Tests...

--- Testing Zero-Shot Prompt ---
Model Response:
Summer Rhodes
Will Power
Dr. Stone
Bill Gates
------------------------------

--- Testing One-Shot Prompt ---
Model Response:
Summer Rhodes
Will Power
Dr. Stone
Bill Gates
------------------------------

--- Testing Few-Shot Prompt ---
Model Response:
Summer Rhodes
Will Power
Dr. Stone
Bill Gates
------------------------------
```

## Explanation of Prompting Techniques

This project demonstrates three common prompting techniques:

-   **Zero-Shot Prompting:** You ask the model to perform a task without giving it any prior examples. The model relies solely on its pre-existing knowledge to understand and execute the request.

-   **One-Shot Prompting:** You provide the model with a single example of the task you want it to perform. This helps the model understand the expected format and context of the output.

-   **Few-Shot Prompting:** You provide the model with multiple examples (usually 2-5). This gives the model a more robust understanding of the task, leading to more consistent and accurate results, especially for complex tasks.
