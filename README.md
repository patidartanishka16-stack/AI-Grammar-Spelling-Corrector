# AI Grammar & Spelling Correction Tool

An AI-powered text proofreading tool that detects common grammar and spelling errors and provides correction suggestions using LanguageTool and Streamlit.

## Features

- Detects grammar errors
- Detects spelling mistakes
- Provides correction suggestions
- Generates corrected text
- Shows original and corrected text
- Handles multiple errors and paragraphs
- Handles empty and error-free input

## Tech Stack

- Python
- LanguageTool
- Streamlit

## How It Works

```text
User Input
    ↓
Streamlit
    ↓
LanguageTool
    ↓
Error Detection
    ↓
Suggestions + Corrected Text
  
## Installation:

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run app.py

## Project Structure

```text
AI-Grammar-Spelling-Corrector/
│
├── app.py
├── test.py
├── requirements.txt
├── test_cases.txt
├── README.md
└── .gitignore

## Usage

1. Run the Streamlit application using:

```bash
streamlit run app.py
Enter a sentence or paragraph in the text input box.
Click the Check Text button.
The application displays the original text and corrected text.
Detected grammar and spelling errors are shown with their categories and possible suggestions.
If no errors are found, the application displays a success message.
If the input is empty, the application asks the user to enter some text.


### Simple flow:

```text
Enter Text
    ↓
Click "Check Text"
    ↓
Detect Errors
    ↓
View Suggestions
    ↓
View Corrected Text

### Limitation

Automated correction may not always be contextually perfect. LanguageTool can provide multiple suggestions, so the application displays suggestions along with the automatically corrected text.

1.Future Improvements
2.Better error highlighting
3.User-selectable corrections
4.Support for more languages
5.More context-aware correction

### Testing

The application was tested for:

1.Grammar errors
2.Spelling errors
3.Multiple errors
4.Correct sentences
5.Multiple sentences/paragraphs
6.Empty input

Detailed test cases are available in test_cases.txt.




