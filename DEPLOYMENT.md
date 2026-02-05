# Deployment & Setup Guide

This guide covers deploying both the **Streamlit GDP Dashboard** and the **Google Sheets Promotion Add-on** to your organization.

## Part 1: Streamlit GDP Dashboard

### Local Development

**Prerequisites:** Python 3.9+

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Tryingthislgtm/gdp-dashboard.git
   cd gdp-dashboard
   ```

2. **Create a virtual environment and install dependencies:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Run the app locally:**
   ```bash
   streamlit run streamlit_app.py
   ```
   The app will open at `http://localhost:8501`.

### Deploy to Streamlit Cloud

1. **Push your repo to GitHub** (you're already there!)

2. **Go to [Streamlit Cloud](https://streamlit.io/cloud)** and sign in with your GitHub account.

3. **Click "Create App"** and select:
   - Repository: `Tryingthislgtm/gdp-dashboard`
   - Branch: `main`
   - Main file path: `streamlit_app.py`

4. **Deploy** — Streamlit will install `requirements.txt` and run the app automatically.

5. Your app will be live at `https://gdp-dashboard-<deployment-name>.streamlit.app`.

### Run Tests Locally & in CI

**Run tests manually:**
```bash
PYTHONPATH=. pytest -q
```

**GitHub Actions CI:** Tests run automatically on every push and pull request to `main`. Monitor status in the **Actions** tab on GitHub or from the README badge.

---

## Part 2: Google Sheets Promotion Add-on

### Option A: Manual Installation (Recommended for Testing)

**In Google Sheets:**

1. Open a Google Sheet.
2. Go to **Extensions** → **Apps Script**.
3. Create a new project (or open an existing one).
4. Copy the code from three files in `gs_addon/`:
   - [`Code.gs`](gs_addon/Code.gs) → paste into `Code.gs` in Apps Script editor
   - [`sidebar.html`](gs_addon/sidebar.html) → create a new file, paste, and save as `sidebar.html`
   - [`appsscript.json`](gs_addon/appsscript.json) → copy content into the manifest

5. **Save** the project.
6. Return to your spreadsheet; you'll see a new **Promotions** menu.
7. Click **Promotions** → **Open Promotion Tool** to use the sidebar.

**Usage:**
- Select a range of numeric cells (prices, invoice amounts, etc.).
- Open the sidebar and enter a promotion (percentage or flat discount).
- Click **Preview impact** to see the calculation.
- Click **Apply promotion to sheet** to update cells.

### Option B: Deploy via `clasp` (Command Line)

**Prerequisites:** Node.js 14+

1. **Install clasp:**
   ```bash
   npm install -g @google/clasp
   ```

2. **Authenticate:**
   ```bash
   clasp login
   ```

3. **Create or link an Apps Script project:**
   ```bash
   cd gs_addon
   clasp create --type sheets
   ```

4. **Push code to Apps Script:**
   ```bash
   clasp push
   ```

5. **Open in the browser:**
   ```bash
   clasp open
   ```

### Publish as an Organization Add-on (Advanced)

To distribute the add-on to all Google Workspaces users in your organization:

1. **Configure your `appsscript.json`** with your organization name and description.

2. **Deploy as an add-on** in the Apps Script editor:
   - Click **Deploy** → **New deployment** → **Add-on** → **Create**.

3. **Submit to Google Workspace Marketplace** (admin approval required).

4. **Domain administrators** can install it for all users in Settings → Google Workspace Cloud Marketplace.

See [Google's official guide](https://developers.google.com/workspace/add-ons/how-tos/building#workspace-marketplace) for details.

---

## Project Structure

```
gdp-dashboard/
├── streamlit_app.py          # Main Streamlit app
├── gdp_loader.py             # Testable GDP data loader module
├── requirements.txt          # Python dependencies
├── data/
│   └── gdp_data.csv          # World Bank GDP data
├── gs_addon/
│   ├── Code.gs               # Apps Script backend
│   ├── sidebar.html          # UI for the sidebar
│   ├── appsscript.json       # Manifest with permissions
│   └── README.md             # Sheets add-on specific docs
├── tests/
│   └── test_gdp_loader.py    # Unit tests
├── .github/workflows/
│   └── ci.yml                # GitHub Actions CI
├── README.md                 # Project overview
└── DEPLOYMENT.md             # This file
```

---

## Troubleshooting

### Streamlit App Issues

- **Port already in use:** Change the port with `streamlit run streamlit_app.py --server.port=8502`.
- **Module not found error:** Ensure you're in the virtual environment: `. .venv/bin/activate`.
- **Data file not found:** Verify `data/gdp_data.csv` exists in the repo root.

### Sheets Add-on Issues

- **Apps Script authorization:** Grant permissions when first running the add-on.
- **Non-numeric cells:** The add-on silently skips text values; select only numeric ranges.
- **Changes not saved:** Make sure you click **Apply promotion** (Preview doesn't modify the sheet).

### CI/CD Issues

- **Tests fail in GitHub Actions:** Check that `PYTHONPATH` is set. See [`.github/workflows/ci.yml`](.github/workflows/ci.yml).
- **Dependencies not installing:** Verify `requirements.txt` has no syntax errors; run `pip check` locally.

---

## Next Steps & Enhancements

### For the Streamlit App:
- [ ] Add filters by region/continent.
- [ ] Display year-over-year growth percentage.
- [ ] Export chart as PNG or CSV.
- [ ] Caching optimization for large datasets.

### For the Sheets Add-on:
- [ ] Audit log: store original values before applying promotions.
- [ ] Tiered promotions (e.g., X% for first $1000, Y% above).
- [ ] Integration with Google Sheets scripts for batch updates.
- [ ] Email notifications after applying promotions.

### For the Project:
- [ ] Add an E2E test suite for the Streamlit app.
- [ ] Set up pre-commit hooks (linting, formatting).
- [ ] Document API endpoints if building a REST API version.
- [ ] Create Docker container for standardized deployments.

---

## Support & Feedback

For questions or issues:
1. Check [README.md](README.md) for quick reference.
2. Review test files in `tests/` for example usage.
3. Open a GitHub issue or discussion.

Happy deploying! 🚀
