# OpenAI API in Terminal

This is a Python 3 command line application that serves as an interface for the OpenAI API. The application provides the following CLI options:

## CLI Requirements
* The CLI should have an optional `-c/--chat` option to be used with an optional `-m/--model` option that takes in a model name as an argument (default `gpt-3.5-turbo`).
* The CLI should have an optional `-w/--whisper` option that takes in an audio file path as an argument.
* The CLI should have an optional `-t/--translate` option that takes in an audio file path as an argument.
* The CLI should have an optional `-i/--image` option that takes in a prompt as an argument.

## Development Requirements
* The application should have a `requirements.txt` file with the dependencies.
* The application should have a `README.md` file with a nice description and the instructions to install and run the application.
* The application should have a `.env` file for secrets like the API key.
* Use the `click` library for the command line interfaces (CLI).
* Use the `dotenv` library to read the `.env` file.
* Use the `openai` library to interact with the OpenAI API.

## CLI Options
### help
The 'help' option should print the help message with examples of how to use the CLI.
Please be very explicit and specific with the examples.

### chat
The 'chat' option should start an interactive chat with the AI.
Example code:
```python
completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": "Hello!"}
  ]
)
```

### image
Takes in a prompt and generates an image.
Example code:
```python
openai.Image.create(
  prompt="A cute baby sea otter",
  n=2,
  size="1024x1024"
)
```

### whisper
Takes in an audio file and generates a transcription.
Example code:
```python
audio_file = open(file_path, "rb")
transcript = openai.Audio.transcribe("whisper-1", audio_file)
```

### translate
Takes in an audio file and generates a translated transcription.
Example code:
```python
audio_file = open("german.m4a", "rb")
transcript = openai.Audio.translate("whisper-1", audio_file)
```

## Notes
* Please follow extended development guidelines, such as DRY (Don't Repeat Yourself) and try to write elegant code that is easy to read.
* Make sure to properly document your code.
* Make sure to properly handle errors, invalid options and arguments.
* Make sure to properly handle the API rate limits.

## Usage Examples
```bash
$ python main.py --chat --model gpt-3.5-turbo
# Enter your prompt and press enter
> please generate a haiku about poker
In smoky rooms, hearts,
Cards dance, fortunes ebbs and flows,
Poker faces know.
> ...
```

```bash
$ python main.py --whisper /path/to/audio/file.mp3
Below is the content of the given audio file in text form:
> Hello, how are you?
```

```bash
$ python main.py --translate /path/to/audio/file.mp3
Below is the translated content of the given audio file in text form:
> This is a sentence in German.
```

```bash
$ python main.py --image "A blue bottle in space"
> Here is your image: https://example.com/image.png
```
