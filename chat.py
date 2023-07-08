import openai

from rich.console import Console

from utils import display_output, handle_error


def start_chat(model, verbose=False):
    """
    Start an interactive chat with the AI.

    Args:
        model (str): The model for the chat.
        verbose (bool, optional): Whether to display verbose output. Defaults to False.
    """
    display_output("Starting chat...")

    system = {"role": "system", "content": f"DIRECTIVE_FOR_{model}"}
    message = {"role": "user", "content": ""}
    conversation = [system]
    tokens = 0
    console = Console()
    while True:
        prompt = input("\n􀳾 > ")
        if prompt == "exit":
            break
        try:
            message["content"] = prompt
            conversation.append(message)
            with console.status("[bold green]Generating..."):
                completion = openai.ChatCompletion.create(
                    model=model,
                    messages=conversation,
                )

            message = completion.choices[0].message
            conversation.append(message.to_dict())
            tokens = completion.usage.total_tokens
            display_output(f"\n􀪬  > {message.content}")
            display_output(f"\n􀤚  ({tokens})", color="magenta")

        except Exception as e:
            handle_error(e, verbose)
