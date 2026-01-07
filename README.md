# Google Gemini Agent Starter

Python project demonstrating a simple AI chatbot/agent
using the Google Gemini API.

Designed to clone and run locally by supplying your own API key.

> Tested on Windows with Python 3.12 (compatible with Python 3.9+)

---

## Features
- Simple CLI chat interface
- Clean provider abstraction
- Safe credential handling via `.env`
- Coaching-focused system prompt

---

## Requirements
- Python 3.9+
- Google Gemini API key (Google AI Studio)

---

## Setup (Windows / PowerShell)

### 1) Create virtual environment
```powershell
python -m venv .venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
