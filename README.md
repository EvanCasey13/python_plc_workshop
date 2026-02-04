# Red Hat Python Workshop

A beginner-friendly Flask web application for teaching Python.

## Features

- **16 Interactive Lessons** covering Python basics through real AI tools
- **Run code in the browser** - see output instantly
- **Exercises with hints** - practice each concept
- **Scratch pad** - experiment with your own code
- **Quick reference** - cheat sheet for common syntax
- **Real AI tools** - TextBlob, scikit-learn

## Lessons

1. **Python Basics**
   - Hello World
   - Variables
   - Data Types
   - Operators
   - User Input

2. **Control Flow**
   - If Statements
   - For Loops
   - While Loops

3. **Data Structures**
   - Lists
   - Dictionaries

4. **Functions**
   - Defining Functions
   - Advanced Functions

5. **Real AI Tools**
   - Sentiment Analysis (TextBlob - detect emotions in text)
   - Spam Detector (scikit-learn - train a real ML model)
   - Text Analysis (Extract nouns, verbs, topics)
   - Movie Recommender (Build a Netflix-style system)

## Setup

Choose your operating system below and follow the instructions.

---

### Windows

#### Option 1: Command Prompt (cmd)

```cmd
# Check Python is installed
python --version

# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```

#### Option 2: PowerShell

```powershell
# Check Python is installed
python --version

# Create virtual environment
python -m venv venv

# Activate virtual environment
.\venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```

> **Note:** If you get a PowerShell execution policy error, run:
> `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

#### Windows Quick Start (one command)
```cmd
python -m venv venv && venv\Scripts\activate && pip install -r requirements.txt && python app.py
```

---

### macOS

```bash
# Check Python is installed
python3 --version

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```

#### macOS Quick Start (one command)
```bash
python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt && python app.py
```

> **Note:** macOS uses `python3` instead of `python`. If you don't have Python, install it with:
> `brew install python` (requires [Homebrew](https://brew.sh))

---

### Linux (Ubuntu/Debian)

```bash
# Install Python and venv if needed
sudo apt update
sudo apt install python3 python3-venv python3-pip

# Check Python is installed
python3 --version

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```

#### Linux Quick Start (one command)
```bash
python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt && python app.py
```

---

### Podman (Container)

Run the application in a container without installing Python dependencies locally.

#### Windows (PowerShell)

```powershell
# First time only - initialize and start the Podman machine
podman machine init
podman machine start

# Build and run
podman build -t python-workshop .
podman run -p 5000:5000 python-workshop
```

Quick start (after machine is running):
```powershell
podman build -t python-workshop . ; podman run -p 5000:5000 python-workshop
```

Then open http://localhost:5000

#### WSL (Windows Subsystem for Linux)

```bash
# Build the image
podman build -t python-workshop .

# Run with host networking (required for WSL)
podman run --network=host python-workshop
```

Then open http://localhost:5000

#### macOS

```bash
# First time only - initialize and start the Podman machine
podman machine init
podman machine start

# Build and run
podman build -t python-workshop . && podman run -p 5000:5000 python-workshop
```

Then open http://localhost:5000

#### Linux

```bash
# No machine needed - Podman runs natively
podman build -t python-workshop . && podman run -p 5000:5000 python-workshop
```

Then open http://localhost:5000

#### Run in Background

```bash
podman run -d -p 5000:5000 --name workshop python-workshop
podman logs workshop    # View logs
podman stop workshop    # Stop
podman rm workshop      # Remove
```

#### Different Port

```bash
podman run -p 8080:5000 python-workshop
```

Then open http://localhost:8080

---

### Deployment

Each student runs the workshop on their own laptop.

#### Using Python (venv)

**Windows:**
```powershell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

#### Using Podman

**Windows (PowerShell):**
```powershell
podman machine start
podman build -t python-workshop .
podman run -p 5000:5000 python-workshop
```

**macOS:**
```bash
podman machine start
podman build -t python-workshop . && podman run -p 5000:5000 python-workshop
```

**Linux:**
```bash
podman build -t python-workshop . && podman run -p 5000:5000 python-workshop
```

Then open http://localhost:5000

---

### After Setup

1. Open your browser to: **http://127.0.0.1:5000**
2. You'll see `(venv)` in your terminal when the virtual environment is active

### Deactivate Virtual Environment (when done)

```bash
deactivate
```

### Troubleshooting

| Problem | Solution |
|---------|----------|
| `python` not found | Try `python3` instead, or install Python from [python.org](https://python.org) |
| `venv` not found | Install with `sudo apt install python3-venv` (Linux) |
| PowerShell error | Run `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` |
| Port 5000 in use | Use a different port: `podman run -p 8080:5000 python-workshop` or set `FLASK_PORT=5001` |
| Podman not found | Install from [podman.io](https://podman.io/getting-started/installation) |
| Container won't start | Check logs with `podman logs <container-name>` |

## Project Structure

```
├── app.py              # Flask application
├── requirements.txt    # Python dependencies
├── Containerfile       # Podman/Docker container definition
├── .containerignore    # Files to exclude from container
├── templates/          # HTML templates
│   ├── index.html      # Home page
│   ├── lesson.html     # Lesson page
│   └── reference.html  # Quick reference
└── static/
    ├── style.css       # Styles
    └── images/         # Images (logo, etc.)
```

## Usage

1. Start at the home page to see all available lessons
2. Click a lesson to begin learning
3. Read the example code and explanations
4. Click "Run Code" to execute and see output
5. Modify the code and run again to experiment
6. Try the exercises using the scratch pad
7. Use hints if you get stuck
