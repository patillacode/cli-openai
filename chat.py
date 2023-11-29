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
    # message = {"role": "user", "content": ""}
    conversation = [system]
    tokens = 0
    console = Console()

    completion = client.chat.completions.create(
        model=model,
        messages=conversation,
        # stream=True,
    )
    # for chunk in completion:
    #     print(chunk.choices[0].delta)

    while True:
        prompt = input("\n􀳾 > ")
        if prompt == "exit":
            break
        try:
            conversation.append({"role": "user", "content": prompt})
            with console.status("[bold green]Generating..."):
                completion = client.chat.completions.create(
                    model=model,
                    messages=conversation,
                    stream=True,
                )
            # for chunk in completion:
            #     if chunk.choices[0].delta.content is not None:
            #         print(chunk.choices[0].delta.content, end="")
            message = completion.choices[0].message
            conversation.append({"role": "system", "content": message.content})
            tokens = completion.usage.total_tokens
            ic(conversation)
            display_output(f"\n􀪬  > {message.content}")
            display_output(f"\n􀤚  ({tokens})", color="magenta")

        except Exception as e:
            handle_error(e, verbose)
