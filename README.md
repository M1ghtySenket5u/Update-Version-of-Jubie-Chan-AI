## Jubie-Chan – Your Linux Mint AI Buddy

Jubie-Chan is a small Python-based AI buddy you can run from the terminal on Linux Mint.
She answers questions, explains concepts, and offers helpful tips in a friendly, clear way.

### 1. Requirements

- Python 3.9+ (check with `python3 --version`)
- pip (Python package manager)
- An OpenAI API key

### 2. Setup on Linux Mint

From the folder containing `jubie_chan.py`:

```bash
cd /home/jubei-chan

# (Optional but recommended) create a virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Configure your API key

You can either:

- **Use a `.env` file** (recommended):

  ```bash
  cp .env.example .env
  # then edit .env and put your real key:
  # OPENAI_API_KEY=sk-...
  ```

  The app will load this automatically via `python-dotenv`.

- **Or export the variable in your shell**:

  ```bash
  export OPENAI_API_KEY="sk-..."
  ```

### 4. Run Jubie-Chan

```bash
python3 jubie_chan.py
```

You’ll see a short welcome banner. Then you can:

- Ask questions (`How do I check disk space on Linux Mint?`)
- Request explanations (`Explain git branches in simple terms`)
- Ask for tips (`Any tips for organizing a coding project?`)

Type `exit` or `quit`, or just press Enter on an empty line, to leave the chat.

### 5. Customize Jubie-Chan’s personality

Open `jubie_chan.py` and edit the `JUBIE_SYSTEM_PROMPT` string.
You can change her tone, add constraints, or give extra instructions about how she should respond.

