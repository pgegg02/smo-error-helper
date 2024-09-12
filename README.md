# Setup Guide
## Overview
The smo utility is a command-line tool designed to run Python scripts and provide error analysis using OpenAI's API. It allows you to run scripts from anywhere in your system and get detailed troubleshooting tips for any errors encountered.

## Components
smo.py: The Python script that handles error analysis and communicates with OpenAI's API.
smo: A shell script that invokes smo.py with the required arguments.
Installation

## 1. Clone the Repository
First, clone the repository containing the smo.py and smo files:

## 2. Place smo.py and smo Scripts
Move smo.py to the desired directory:

Place smo.py in a directory where you want to keep your scripts, for example: ```/Users/yourusername/Developer/util_scripts/```

## 3. Create the smo script:

Save the following content into a file named smo in a directory that is in your system's PATH, for example: ```/Users/yourusername/Developer/```

```
#!/bin/zsh
# This script calls your smo.py script with the necessary arguments.
python3 /Users/yourusername/Developer/util_scripts/smo.py "$@"
```
Replace ```/Users/yourusername/Developer/util_scripts/``` with the path where you placed smo.py.

### Make the smo script executable:

```
chmod +x /Users/yourusername/Developer/smo
```

## 3. Update Your Shell Configuration
Add the directory containing the smo script to your PATH in your shell configuration file (.zshrc for zsh users, .bashrc or .bash_profile for bash users). Open your shell configuration file and add the following line:

```
export PATH="$PATH:/Users/yourusername/Developer"
```
Replace /Users/yourusername/Developer with the path where you placed the smo script.

After adding this line, reload your shell configuration:

```
source ~/.zshrc
```

## 4. Install Dependencies
Ensure you have Python 3 and the necessary Python packages installed. You can install the required packages using pip:

```
pip install openai
```

5. Set Up OpenAI API Key
For smo.py to work, you need to set your OpenAI API key as a environment variable.

```export OPENAI_API_KEY='your_openai_api_key'```

# Usage
You can now use the smo command to run Python scripts and get error analysis. For example:

```
smo /path/to/your/script.py
```
If the script produces errors, smo will provide a detailed error message and an analysis from OpenAI's API.

![Alt text](exampleusage.jpg)
