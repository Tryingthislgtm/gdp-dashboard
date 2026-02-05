#!/bin/bash
# Quick Deploy Script for Streamlit Cloud
# Usage: bash deploy.sh

set -e

echo "🚀 Deploying Promotion Calculator to Streamlit Cloud..."
echo ""

# Check if git repo is clean
if ! git diff --quiet; then
    echo "⚠️  You have uncommitted changes. Committing now..."
    git add .
    git commit -m "Deploy: Promotion Calculator update $(date +%Y-%m-%d)"
else
    echo "✓ Git repo is clean"
fi

# Push to GitHub
echo "📤 Pushing to GitHub..."
git push origin main

echo ""
echo "✅ Code pushed to GitHub!"
echo ""
echo "Next steps:"
echo "1. Go to https://streamlit.io/cloud"
echo "2. Click 'Create app'"
echo "3. Select: Tryingthislgtm/gdp-dashboard"
echo "4. Branch: main"
echo "5. File: streamlit_app.py"
echo "6. Click 'Deploy'"
echo ""
echo "Your app will be live in 2-3 minutes at:"
echo "https://gdp-dashboard-[random-id].streamlit.app"
echo ""
echo "Share that URL with your Google Workspace team! 🎉"
