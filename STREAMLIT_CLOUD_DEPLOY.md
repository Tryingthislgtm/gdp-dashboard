# Deploy to Streamlit Cloud in 5 Minutes

This is the **fastest and easiest way** to get your Promotion Calculator live for your Google Workspace team.

## Prerequisites

- GitHub account (you already have this!)
- Streamlit account (free)

## Step-by-Step

### 1. Ensure Your Code is Pushed to GitHub (2 minutes)

```bash
cd /workspaces/gdp-dashboard
git add .
git commit -m "Release: Promotion Calculator v1.0 for sales teams"
git push origin main
```

### 2. Go to Streamlit Cloud (1 minute)

- Open https://streamlit.io/cloud
- Click **"Create app"**

### 3. Connect Your GitHub Repo (1 minute)

1. Click **"Connect"** to link your GitHub account
2. Select repository: **Tryingthislgtm/gdp-dashboard**
3. Select branch: **main**
4. Set main file path: **streamlit_app.py**
5. Click **"Deploy"**

**Streamlit will now build and deploy your app automatically.** This takes ~2-3 minutes.

### 4. Get Your Live URL (1 minute)

Once deployed, your app will be available at:

```
https://gdp-dashboard-RANDOMID.streamlit.app
```

Copy this URL.

### 5. Share with Your Team (1 minute)

**Option A: Direct Link**
```
Send this link to your team:
https://gdp-dashboard-RANDOMID.streamlit.app
```

**Option B: Embed in Google Sites** (Recommended)

1. Go to your Google Workspace Site
2. Click **Edit** → **Insert** → **Embed code**
3. Paste:
   ```html
   <iframe 
     src="https://gdp-dashboard-RANDOMID.streamlit.app" 
     width="100%" 
     height="1200" 
     frameborder="0">
   </iframe>
   ```
4. Click **Insert**

5. **Publish** your site

Now your team can access the calculator directly from Google Sites! 🎉

---

## Optional: Add Google Workspace Authentication

To restrict access to only your workspace team:

1. In Streamlit Cloud app settings, click **Secrets**
2. Add your workspace OAuth credentials (follow Streamlit's docs)
3. Update `streamlit_app.py` to check authentication

Or just share the link with your team privately.

---

## Future Updates

Whenever you make changes:

1. **Push to GitHub:**
   ```bash
   git add .
   git commit -m "Update: [your change description]"
   git push origin main
   ```

2. **Streamlit Cloud automatically redeploys** your app within 1-2 minutes

3. **Your team sees the updates instantly**

No manual redeployment needed!

---

## Troubleshooting

### "Deploy is stuck or failed"
- Check GitHub is connected properly
- Verify `streamlit_app.py` is in repo root
- Check for Python/dependency errors in logs

### "App loads but shows errors"
- Check `requirements.txt` has all dependencies
- Verify CSV files exist in `data/` folder
- Check file paths are correct (should use relative paths)

### "Slow to load"
- Streamlit Cloud free tier is slower than paid
- Consider upgrading to Streamlit Cloud **Pro** ($5/mo) for faster performance
- Or use Google Cloud Run (see GOOGLE_WORKSPACE_DEPLOYMENT.md)

---

## Cost

- **Streamlit Cloud Free:** $0/month (1 app, limited resources)
- **Streamlit Cloud Pro:** $5/month (faster, better performance)
- **Google Cloud Run:** $0-20/month (depending on usage)

---

## Done! 🎉

Your calculator is now live and your sales team can access it from anywhere, on any device, right from Google Workspace!

**Next:** 
- Customize the pricing plans in `data/pricing_plans.csv`
- Share the link with your team
- Start closing more deals with instant, professional quotes
