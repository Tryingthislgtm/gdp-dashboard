# Deploying to Google Workspace

This guide covers deploying your Promotion Calculator to be used by your Google Workspace team.

## Option 1: Streamlit Cloud (Easiest - Recommended for quick deployment)

**Pros:**
- Free tier available
- Automatic deploys from GitHub
- Shareable URL
- Built-in authentication

**Steps:**

1. **Push code to GitHub** (you're already there!)
   ```bash
   git add .
   git commit -m "Add plan switching calculator"
   git push origin main
   ```

2. **Go to [Streamlit Cloud](https://streamlit.io/cloud)**
   - Click "Create App"
   - Connect your GitHub account
   - Select: `Tryingthislgtm/gdp-dashboard`
   - Branch: `main`
   - Main file: `streamlit_app.py`

3. **Configure with Gmail authentication** (optional, recommended for workspace)
   - In Streamlit Cloud settings, enable Google OAuth
   - This restricts access to your workspace users only

4. **Share the URL with your team**
   - Example: `https://gdp-dashboard-promo.streamlit.app`
   - Embed in Google Sites (see below)

---

## Option 2: Google Cloud Run (Enterprise-grade)

**Pros:**
- More control
- Better for sensitive data
- Can integrate with Workspace better
- Supports custom domain

**Prerequisites:**
- Google Cloud account
- `gcloud` CLI installed
- Billing enabled on GCP

**Steps:**

1. **Create a Dockerfile:**
   ```dockerfile
   FROM python:3.11-slim
   
   WORKDIR /app
   
   COPY requirements.txt .
   RUN pip install --no-cache-dir -r requirements.txt
   
   COPY . .
   
   EXPOSE 8080
   
   CMD streamlit run streamlit_app.py \
       --server.port=8080 \
       --server.address=0.0.0.0 \
       --server.headless=true
   ```

2. **Build and push to Container Registry:**
   ```bash
   gcloud auth configure-docker
   
   docker build -t gcr.io/YOUR-PROJECT-ID/promo-calculator:latest .
   
   docker push gcr.io/YOUR-PROJECT-ID/promo-calculator:latest
   ```

3. **Deploy to Cloud Run:**
   ```bash
   gcloud run deploy promo-calculator \
     --image gcr.io/YOUR-PROJECT-ID/promo-calculator:latest \
     --platform managed \
     --region us-central1 \
     --allow-unauthenticated
   ```

4. **Configure IAM for workspace users** (optional)
   - Restrict access to Google Workspace members only
   - Use Cloud IAM identity

---

## Option 3: Embed in Google Sites (Best UX)

**After deploying to Streamlit Cloud or Cloud Run:**

1. **Go to [Google Sites](https://sites.google.com)**

2. **Open your team's workspace site**

3. **Click Insert → Embed URL**
   - Paste your Streamlit Cloud URL or Cloud Run URL
   - Example: `https://gdp-dashboard-promo.streamlit.app`

4. **Adjust size** as needed:
   - Width: 100%
   - Height: 1200px (or as needed)

5. **Publish**

Now your team can access the calculator directly from Google Sites!

---

## Option 4: Google Workspace Add-on (Most Integrated)

**Pros:**
- Appears in Gmail/Sheets/Docs
- Seamless workspace integration
- Can read/write to Google Sheets
- Custom UI

**Cons:**
- More complex to build
- Requires Apps Script + backend

This would require extending the existing `gs_addon/` code with the calculator logic. Contact us if you want to pursue this.

---

## Recommended Setup

**For immediate team use:**

1. **Deploy to Streamlit Cloud**
   ```bash
   git push origin main
   ```

2. **Create Streamlit Cloud app** (5 minutes)
   - Go to streamlit.io/cloud
   - Connect GitHub repo
   - Add Google OAuth for workspace security

3. **Embed in Google Sites** (5 minutes)
   - Go to your team's Google Site
   - Insert → Embed URL
   - Paste the Streamlit URL

**Result:** Your sales team can access the calculator from Google Sites, authenticates with their workspace Gmail, and can use it on any device.

---

## Sharing with Your Team

Once deployed, share this link:
```
[Your Workspace Site] → [Promotion Calculator Tab] → Calculator appears embedded
```

Or direct link:
```
https://gdp-dashboard-promo.streamlit.app
```

---

## Updating the Calculator

After deployment, whenever you make changes:

1. **For Streamlit Cloud:** Just push to main via Git → Auto-redeploys
2. **For Cloud Run:** Rebuild Docker image and redeploy
3. **Changes appear instantly** on your team's site/link

---

## Troubleshooting

### "My team can't access it"
- Check Streamlit Cloud/Cloud Run is deployed and running
- Ensure authentication is configured correctly
- Share the URL directly if embed doesn't work

### "Embed is blank/not loading"
- Some embedding tools require HTTPS (both options provide this)
- Try opening the direct URL first
- Check browser console for CORS issues

### "Slow performance"
- Streamlit Cloud free tier has resource limits
- Cloud Run scales automatically
- Consider upgrading Streamlit Cloud tier if needed

---

## Cost Breakdown

| Option | Cost | Setup Time |
|--------|------|-----------|
| Streamlit Cloud (free) | Free | 5 min |
| Streamlit Cloud (pro) | $5-100/mo | 5 min |
| Google Cloud Run | $0-20/mo | 15 min |
| Cloud Run + custom domain | $12-40/mo | 20 min |

---

## Next Steps

**Choose your preferred option and let me know:**
1. Streamlit Cloud (easiest)
2. Google Cloud Run (most control)
3. Both (redundancy)

I can help with setup and configuration!
