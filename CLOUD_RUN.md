# Deploy to Google Cloud Run (1 Command)

**Fastest enterprise deployment for Google Workspace teams.**

## Prerequisites (One-Time Setup)
1. Install Google Cloud CLI: https://cloud.google.com/sdk/docs/install
2. Create a Google Cloud project: https://console.cloud.google.com
3. Enable Cloud Run API

## Deploy (One Command)

```bash
gcloud run deploy promo-calculator \
  --source . \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated
```

That's it! Your app will be live at:
```
https://promo-calculator-XXXXXXX.run.app
```

## Share with Your Team

1. **Direct link:** Send the URL above
2. **Embed in Google Sites:** Use the iframe embed code
3. **Send via email:** https://promo-calculator-XXXXXXX.run.app

---

## Updates

Just push code and redeploy:
```bash
git add .
git commit -m "Update promo calculator"
git push origin main

gcloud run deploy promo-calculator --source .
```

---

## Cost
- **Free tier:** 2M requests/month
- **Low usage:** $0-5/month
- **Scale:** Auto-scales based on traffic

---

## Troubleshooting

**"gcloud not found"**
```bash
curl https://sdk.cloud.google.com | bash
exec -l $SHELL
gcloud init
```

**"Cloud Run API not enabled"**
```bash
gcloud services enable run.googleapis.com
```

**"Authentication failed"**
```bash
gcloud auth login
```

---

## Next Steps
1. Run the command above
2. Copy the URL from output
3. Share with your team
4. Done! 🎉
