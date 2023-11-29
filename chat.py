from dotenv import load_dotenv
from icecream import ic  # noqa: F401
from openai import OpenAI
from rich.console import Console

from utils import display_output, handle_error

load_dotenv()
client = OpenAI()


def start_chat(model, verbose=False):
    """
    Start an interactive chat with the AI.

    Args:
        model (str): The model for the chat.
        verbose (bool, optional): Whether to display verbose output. Defaults to False.
    """
    display_output("Starting chat...")

    system = {"role": "system", "content": f"DIRECTIVE_FOR_{model}"}
    conversation = [system]
    console = Console()

    completion = client.chat.completions.create(
        model=model,
        messages=conversation,
    )

    while True:
        prompt = input("\n􀳾 > ")

        if prompt.strip() == "":
            continue
        elif prompt == "exit":
            break

        try:
            conversation.append({"role": "user", "content": prompt})
            with console.status("[bold green]Generating..."):
                completion = client.chat.completions.create(
                    model=model,
                    messages=conversation,
                    stream=True,
                )
            messages = []
            for chunk in completion:
                if chunk.choices[0].delta.content is not None:
                    content = chunk.choices[0].delta.content
                    messages.append(content)
                    display_output(content, color="yellow", end="")

            full_message = "".join(messages)
            conversation.append({"role": "system", "content": full_message})

        except Exception as e:
            handle_error(e, verbose)
