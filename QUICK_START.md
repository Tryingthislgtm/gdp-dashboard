# ⚡ QUICK START: Deploy in 5 Minutes

This is the **absolute fastest** way to get your calculator live for your team.

## Option A: Streamlit Cloud (Recommended - Easiest)

### Step 1: Push Your Code
```bash
git add .
git commit -m "Deploy promotion calculator"
git push origin main
```

### Step 2: Deploy
1. Go to **https://streamlit.io/cloud**
2. Sign up (free) if needed
3. Click **"Create app"**
4. Select repo: **Tryingthislgtm/gdp-dashboard**
5. Select branch: **main**
6. Set file: **streamlit_app.py**
7. Click **"Deploy"**

### Step 3: Share the Link
After 2-3 minutes, you'll get a URL like:
```
https://gdp-dashboard-XXXX.streamlit.app
```

**Send this link to your team!** They can open it in any browser. ✅

---

## Option B: Instant Google Sheets Version
If you just want to test it immediately without setup:

1. Open this Google Colab notebook: *(coming soon - alternative)*
2. Click **"Open in Colab"**
3. Click **"Run All"**
4. Share the link with your team

---

## Option C: Self-Hosted (Advanced)
If you want to run on your own server:

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

Then use a service like ngrok to create a shareable link.

---

## That's it! 🎉

Your team can now:
- ✅ Instantly calculate bill savings
- ✅ See SMS/Email/Phone script templates  
- ✅ Share promo codes with customers
- ✅ Close deals faster

---

## Need Help?

- **Streamlit Cloud stuck?** Check [STREAMLIT_CLOUD_DEPLOY.md](STREAMLIT_CLOUD_DEPLOY.md)
- **Google Workspace integration?** See [GOOGLE_WORKSPACE_DEPLOYMENT.md](GOOGLE_WORKSPACE_DEPLOYMENT.md)
- **Want to customize?** Edit `data/pricing_plans.csv`
