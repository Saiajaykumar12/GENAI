# GenAI - LangChain + OpenAI Notebook

This repo contains a learning notebook exploring LangChain with OpenAI/GenAI.

Files
- `1_basic_langchain_openai.ipynb` — main notebook demo (remove secrets before publishing).
- `requirements.txt` — dependencies.

Quick start
1. Create and activate a Python environment.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

2. Create a `.env` file in the repo root with your API key (DO NOT commit this file):

```
OPENAI_API_KEY=sk-...
```

3. Run the notebook (open `1_basic_langchain_openai.ipynb` in Jupyter/VS Code) or convert to script.

Security
- `.env` is ignored by `.gitignore`. Ensure no keys are committed. If you accidentally committed secrets, rotate them and remove from git history.

How to push to GitHub
1. Create an empty repo on GitHub (via website or `gh repo create`).
2. Initialize git and push:

```powershell
git init
git add .
git commit -m "Initial commit: add notebook and requirements"
# replace <your-repo-url> with the repo HTTPS/SSH URL
git remote add origin <your-repo-url>
git branch -M main
git push -u origin main
```

If `.env` was accidentally committed:

```powershell
# stop tracking and remove from index
git rm --cached .env
git commit -m "Remove .env"
# to purge from history use the BFG or git filter-branch (advanced)
```

Contact / Next steps
- I can clean the notebook outputs, add a small demo script, or push these changes for you if you provide the GitHub repo URL or allow me to create it via `gh`.
