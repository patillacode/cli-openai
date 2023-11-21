from openai import OpenAI
from rich.console import Console

from utils import display_output, handle_error

client = OpenAI()


def transcribe_audio(audio_file, verbose=False):
    """
    Generate a transcription from an audio file.

    Args:
        audio_file (str): The path to the audio file.
        verbose (bool, optional): Whether to display verbose output. Defaults to False.
    """
    try:
        console = Console()
        with console.status("[bold green]transcribing..."):
            transcript = client.audio.transcribe("whisper-1", open(audio_file, "rb"))
        display_output(
            "Below is the content of the given audio file in text form:\n", "yellow"
        )
        display_output(f"{transcript.text}\n")
    except Exception as e:
        handle_error(e, verbose)


def translate_audio(audio_file, verbose=False):
    """
    Generate a translated transcription from an audio file.

    Args:
        audio_file (str): The path to the audio file.
        verbose (bool, optional): Whether to display verbose output. Defaults to False.
    """
    try:
        console = Console()
        with console.status("[bold green]translating..."):
            translation = client.audio.translate("whisper-1", open(audio_file, "rb"))
        display_output(
            "Below is the translated content of the given audio file in text form:\n",
            "yellow",
        )
        display_output(f"{translation.text}\n")
    except Exception as e:
        handle_error(e, verbose)
