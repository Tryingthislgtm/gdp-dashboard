# :camera: Promotion Calculator

[![Tests](https://github.com/Tryingthislgtm/gdp-dashboard/actions/workflows/ci.yml/badge.svg)](https://github.com/Tryingthislgtm/gdp-dashboard/actions/workflows/ci.yml)

A real-time **Promotion & Plan Switching Calculator** for sales teams. Help your team communicate how promotions and plan changes impact customer bills — instantly, clearly, and in multiple formats (SMS, Email, Phone).

### Quick Start

1. **Install the requirements:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the app locally:**
   ```bash
   streamlit run streamlit_app.py
   ```

3. **Open in your browser:** http://localhost:8501

### Features

✅ **Real-time calculations** — Enter customer bill, promotion type, and amount; see final bill instantly
✅ **Plan switching** — Compare plans and show switch savings + additional promotions
✅ **Tax & fee handling** — Automatic taxes (8.5%) and processing fees
✅ **Multi-channel communication** — Ready-to-send SMS, email, and phone scripts
✅ **Promotion codes** — Track promotions with customer-facing codes
✅ **Effective dates** — Set when promotions take effect

### Deploy to Google Workspace

See [GOOGLE_WORKSPACE_DEPLOYMENT.md](GOOGLE_WORKSPACE_DEPLOYMENT.md) for:
- **Streamlit Cloud** (easiest, free)
- **Google Cloud Run** (enterprise-grade)
- **Embed in Google Sites** (for your team's internal site)

### Project Structure

```
gdp-dashboard/
├── streamlit_app.py                    # Main calculator app
├── pricing_plans_loader.py             # Load pricing plans
├── promotions_loader.py                # Load promo data
├── data/
│   ├── pricing_plans.csv              # 7 pre-configured plans
│   └── promotions.csv                 # Product promotions (example)
├── tests/
│   ├── test_gdp_loader.py
│   └── test_promotions_loader.py      # 7 unit tests
├── .github/workflows/ci.yml           # GitHub Actions CI/CD
├── Dockerfile                         # For Google Cloud Run
├── DEPLOYMENT.md                      # General deployment guide
└── GOOGLE_WORKSPACE_DEPLOYMENT.md     # Google Workspace setup
```

### Testing

```bash
# Run all tests
PYTHONPATH=. pytest -q

# Run specific tests
PYTHONPATH=. pytest tests/test_promotions_loader.py -v
```

### Tech Stack

- **Framework:** Streamlit (Python)
- **Data:** Pandas (CSV-based)
- **Testing:** Pytest
- **CI/CD:** GitHub Actions
- **Deployment:** Streamlit Cloud, Google Cloud Run, or self-hosted

### How Your Sales Team Will Use It

1. **Customer calls in** asking about savings
2. **Team brings up the app** (on Google Sites or direct link)
3. **Enters current bill amount** and promotion terms
4. **Instantly sees:** Final bill, savings, tax breakdown
5. **Reads phone script** to customer for confidence
6. **Sends SMS** with confirm code
7. **Follows up with email** (includes legal terms)

### Example Scenario

- Customer on **Professional Standard** ($199/mo)
- Switch to **Growth** ($149/mo) = $50 savings
- Add **15% loyalty promotion** = $22.35 more savings
- **Total:** Customer saves **$72.35/month** ($868/year!)
- **SMS/Email/Script** auto-generated and ready to send

### Support & Contributing

- See [DEPLOYMENT.md](DEPLOYMENT.md) for general deployment questions
- See [GOOGLE_WORKSPACE_DEPLOYMENT.md](GOOGLE_WORKSPACE_DEPLOYMENT.md) for Workspace integration
- Open a GitHub issue for bugs or feature requests

---

**Ready to deploy?** Start with [GOOGLE_WORKSPACE_DEPLOYMENT.md](GOOGLE_WORKSPACE_DEPLOYMENT.md) → Streamlit Cloud option (5-minute setup).

2. Run the app

   ```
   $ streamlit run streamlit_app.py
   ```
