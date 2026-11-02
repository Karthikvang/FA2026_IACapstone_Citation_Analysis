# FA2026_IACapstone_Citation_Analysis
Fall 2026 Bachelors in Information Analysis Capstone project presented by the University of Michigan's Institute of Social Research.

---

## First-time setup

You need [Git](https://git-scm.com/downloads) and [Python 3](https://www.python.org/downloads/). Run these in a terminal (Mac: Terminal, Windows: PowerShell).

**1. Download the project**
```bash
git clone https://github.com/Karthikvang/FA2026_IACapstone_Citation_Analysis.git
cd FA2026_IACapstone_Citation_Analysis
```

**2. Create a virtual environment and install packages**

Mac / Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Windows:
```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

**3. Create your `.env` file (your private API keys)**

Mac / Linux:
```bash
cp .env.example .env
```

Windows:
```powershell
copy .env.example .env
```

Open `.env` and replace the placeholder values with your real keys. **Copy** the template, don't rename it, so `.env.example` stays in the repo for everyone else.

**4. Confirm Git is ignoring your keys**
```bash
git check-ignore .env
```
If it prints `.env`, you're safe. If it prints nothing, stop and ask the team before committing anything.

---

## Using keys in code

Never paste a key directly into a `.py` or notebook file. Import it instead:

```python
from config import API_KEY, API_EMAIL
```

Adding a new key:
1. Add it to your own `.env` with the real value.
2. Add the same name to `.env.example` with a placeholder value, so teammates know it exists.
3. Load it in `config.py` with `os.getenv("NEW_KEY_NAME")`.
4. Send the real value to teammates privately (text, Slack DM), never through GitHub.

---

## Everyday workflow

Each time you sit down to work:
```bash
source .venv/bin/activate      # Windows: .venv\Scripts\activate
git pull                       # get your teammates' latest changes
```

When you're ready to share your changes:
```bash
git status                     # check what changed. .env should NOT appear here
git add <file1> <file2>        # add the files you changed
git commit -m "Short description of what you did"
git pull                       # grab anything new before pushing
git push
```

If `git push` gets rejected, someone pushed before you. Run `git pull`, then `git push` again.

If someone added a package to `requirements.txt`, run `pip install -r requirements.txt` again after pulling.

---

## If a key gets pushed by accident

Deleting the file afterward doesn't help, because the key is still in Git history. Instead:
1. Go to the API provider's site and **revoke/regenerate the key immediately**.
2. Put the new key in your `.env`.
3. Tell the team.
