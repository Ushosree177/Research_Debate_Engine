# Research Debate Engine

A simple AI-powered research debate web app built using Python, Gradio, Gemini AI, and arXiv API.

This project allows users to enter any research topic and generate:

- Proponent Argument
- Skeptic Counter Argument
- Balanced Final Verdict

The app also searches real research papers from arXiv.

---

# Features

✅ Search research papers from arXiv  
✅ AI-generated academic debate  
✅ Simple web interface using Gradio  
✅ Uses Gemini AI API  
✅ Beginner-friendly Python project  

---

# Project Files

```text
app.py          -> Main Gradio web app
debate.py       -> Gemini AI debate logic
retriever.py    -> arXiv paper search
.env            -> Stores Gemini API key
README.md       -> Project documentation
```

---

# Technologies Used

- Python
- Gradio
- Google Gemini API
- arXiv API
- Requests
- Python Dotenv

---

# Step-by-Step Setup Guide

---

## Step 1: Install Python

Download Python from:

https://www.python.org/downloads/

During installation:

✅ Check "Add Python to PATH"

---

## Step 2: Create Project Folder

Create a folder:

```text
D:\AI
```

Put these files inside:

```text
app.py
debate.py
retriever.py
```

---

## Step 3: Open Terminal

Open CMD or VS Code terminal.

Go to project folder:

```bash
cd D:\AI
```

---

## Step 4: Create Virtual Environment

Run:

```bash
python -m venv venv
```

Activate virtual environment:

```bash
venv\Scripts\activate
```

After activation you will see:

```text
(venv)
```

in terminal.

---

## Step 5: Install Required Libraries

Run these commands:

```bash
pip install gradio
```

```bash
pip install requests
```

```bash
pip install python-dotenv
```

```bash
pip install google-generativeai
```

---

## Step 6: Create .env File

Inside `D:\AI` create a file named:

```text
.env
```

Add your Gemini API key:

```env
GEMINI_API_KEY=your_api_key_here
```

Example:

```env
GEMINI_API_KEY=AIzaSyXXXXXXX
```

---

## Step 7: Get Gemini API Key

Open:

https://aistudio.google.com/app/apikey

Create API key and copy it into `.env` file.

---

## Step 8: Small Code Fixes

### In `debate.py`

Change:

```python
GEMINI_MODEL = "gemini-flash-latest"
```

To:

```python
GEMINI_MODEL = "gemini-1.5-flash"
```

---

### In `app.py`

Change:

```python
with gr.Blocks(title="Research Debate Engine", theme=gr.themes.Soft()) as demo:
```

To:

```python
with gr.Blocks(title="Research Debate Engine") as demo:
```

---

Then change:

```python
demo.launch()
```

To:

```python
demo.launch(theme=gr.themes.Soft(), inbrowser=True)
```

---

# Run the Project

Run:

```bash
python app.py
```

If successful, terminal will show:

```text
Running on local URL: http://127.0.0.1:7860
```

Open this link in browser.

---

# How the Project Works

```text
User enters topic
        ↓
arXiv API searches papers
        ↓
Gemini generates Proponent argument
        ↓
Gemini generates Skeptic argument
        ↓
Gemini generates Final Verdict
        ↓
Results shown in Gradio web app
```

---

# Example Topics

- Does social media affect mental health?
- Can AI models reason?
- Does exercise improve academic performance?
- Is intermittent fasting effective?

---

# Common Errors

---

## 1. Module Not Found Error

Install missing package:

```bash
pip install package_name
```

---

## 2. Invalid API Key

Check `.env` file carefully.

---

## 3. Rate Limit Error

Free Gemini API limit exceeded.

Wait some time and try again.

---

## 4. App Not Opening

Use:

```python
demo.launch(inbrowser=True)
```

---

# Future Improvements

- Add PDF export
- Add citation links
- Add multiple AI models
- Add chat history
- Deploy online using Hugging Face or Render

---

# Author

Project by:

**U. Raha & Yazhini**

---

# License

This project is for educational purposes.
