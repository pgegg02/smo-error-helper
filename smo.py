import subprocess
import sys
import openai
import os

# Retrieve the API key from the environment variable
openai_api_key = os.getenv('OPENAI_API_KEY')
if not openai_api_key:
    raise ValueError("API key not found. Set the OPENAI_API_KEY environment variable.")

client = openai.Client(api_key=openai_api_key)

class colors:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'


def get_gpts_fix(error: str):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are an AI Extension, that is sent Traceback errors"
                           "from people who's code isn't working right. Try to give back"
                           "working code as good as you can, and also if you explain the"
                           "error please keep it short. Don't Use Markdown for Code, just write Code:"
                           "and then in the next line write the fixed code and leave a line empty again. Thanks A lot"
            },
            {
                "role": "user",
                "content": error,
            }
        ],
        model="gpt-3.5-turbo",
    )

    for choice in chat_completion.choices:
        actual_response = choice.message.content

    return actual_response


def trace_errors(command):
    try:
        # Check if the command is a file path and exists
        if os.path.isfile(command[0]):
            # Execute the command as a script
            process = subprocess.Popen(f"python3 {command[0]}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        else:
            # Execute the command as a regular shell command
            process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        stdout, stderr = process.communicate()

        if stderr:
            error_message = stderr.decode('utf-8')
            print(colors.RED + "Error occurred:" + colors.RESET)
            print(colors.RED + error_message + colors.RESET)
            print(colors.GREEN + "Chat-GPTS Solution: \n\n" + colors.RESET)
            print(colors.GREEN + get_gpts_fix(error_message) + colors.RESET)

        else:
            output_message = stdout.decode('utf-8')
            print(colors.GREEN + "Code executed successfully:" + colors.RESET)
            print(output_message)

    except Exception as e:
        print("An error occurred while running the command:", e)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: smo <script-to-run>")
        sys.exit(1)
    command_to_run = sys.argv[1:]
    trace_errors(command_to_run)
