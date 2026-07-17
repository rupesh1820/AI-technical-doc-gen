# 🚀 Deployment Guide

Your AI Technical Documentation Generator can be deployed to the cloud in minutes!

## 📋 Deployment Options

### 1. **Render.com** (⭐ RECOMMENDED - Free & Easy)
- Free tier available
- Auto-deploys from GitHub
- No credit card needed
- Perfect for beginners

### 2. **Railway.app** (Free with GitHub)
- Simple deployment
- $5/month free credits
- Good performance

### 3. **Heroku** (Paid only now)
- Industry standard
- Reliable
- Easy setup

### 4. **PythonAnywhere** (Free tier available)
- Python-specific hosting
- Simple web interface

### 5. **AWS/Google Cloud/Azure** (Advanced)
- Production-grade
- More complex setup
- Free tier available

---

## 🎯 Deploy on Render.com (Easiest!)

### Step 1: Connect GitHub
1. Go to https://render.com
2. Click **Sign up** → GitHub signup
3. Authorize Render to access your repositories

### Step 2: Create Web Service
1. Click **New +** → **Web Service**
2. Select your repository: `AI-technical-doc-gen`
3. Fill in the form:
   - **Name**: `ai-technical-doc-gen`
   - **Region**: Choose your closest region
   - **Branch**: `main`
   - **Runtime**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python app.py`

### Step 3: Add Environment Variables
1. Click **Environment** tab
2. Click **Add Environment Variable**
3. Add:
   - **Key**: `OPENAI_API_KEY`
   - **Value**: Your OpenAI API key (from https://platform.openai.com/api-keys)

### Step 4: Deploy
1. Click **Create Web Service**
2. Wait 2-5 minutes for deployment
3. Get your live URL: `https://ai-technical-doc-gen.onrender.com`

---

## 🚂 Deploy on Railway.app (Very Easy!)

### Step 1: Connect GitHub
1. Go to https://railway.app
2. Click **Start Project** → **Deploy from GitHub**
3. Select your repository

### Step 2: Configure
1. Railway will detect your Python app
2. Add environment variable:
   - **Key**: `OPENAI_API_KEY`
   - **Value**: Your OpenAI API key

### Step 3: Deploy
1. Click **Deploy**
2. Wait for deployment to complete
3. Your app is live!

---

## 🐍 Deploy on PythonAnywhere (Free Tier)

### Step 1: Create Account
1. Go to https://www.pythonanywhere.com
2. Sign up (free tier available)

### Step 2: Clone Repository
1. Go to **Consoles** → **Bash**
2. Run:
```bash
git clone https://github.com/rupesh1820/AI-technical-doc-gen.git
cd AI-technical-doc-gen
pip install -r requirements.txt
```

### Step 3: Create Web App
1. Go to **Web** → **Add a new web app**
2. Choose **Python 3** and **Flask**
3. Configure:
   - **Source code**: `/home/yourusername/AI-technical-doc-gen`
   - **WSGI file**: Update with your app path

### Step 4: Set Environment Variables
1. Go to **Web** → **Reload web app**
2. Edit WSGI file to include:
```python
import os
os.environ['OPENAI_API_KEY'] = 'your-api-key'
```

---

## ☁️ Deploy on Heroku (Paid)

### Step 1: Install Heroku CLI
```bash
# Windows - Download from:
# https://devcenter.heroku.com/articles/heroku-cli

# Or use scoop:
scoop install heroku
```

### Step 2: Login to Heroku
```bash
heroku login
```

### Step 3: Create Heroku App
```bash
cd "c:\Users\RUPESH\OneDrive\Desktop\Gen Ai\Project"
heroku create ai-technical-doc-gen
```

### Step 4: Set Environment Variables
```bash
heroku config:set OPENAI_API_KEY=your_api_key_here
```

### Step 5: Deploy
```bash
git push heroku main
```

### Step 6: View Your App
```bash
heroku open
```

---

## 📝 Create Procfile for Better Deployment

Add a `Procfile` file to your project root:

```
web: python app.py
```

This helps cloud providers understand how to run your app.

---

## 🔒 Important Security Notes

### Never Commit API Keys!
❌ **Bad**: Committing `.env` file
✅ **Good**: Using `.gitignore` (already done!)

### For Production:
1. Use environment variables (not hardcoded)
2. Rotate API keys regularly
3. Use strong API key restrictions on OpenAI

---

## ✅ After Deployment

### Test Your Live App
1. Visit your deployed URL
2. Test the documentation generator
3. Verify copy/download features work

### Monitor Performance
- Check logs for errors
- Monitor API usage
- Set up alerts for downtime

### Update Your GitHub
After choosing a deployment method, update your `README.md`:

```markdown
## 🌐 Live Demo
Try it online: [https://your-deployed-url.com](https://your-deployed-url.com)
```

---

## 📊 Comparison Table

| Platform | Cost | Setup Time | Free Tier | Best For |
|----------|------|-----------|-----------|----------|
| Render | Free | 5 min | Yes | Beginners |
| Railway | $5/mo | 5 min | Yes (credits) | Easy deployment |
| PythonAnywhere | Free | 10 min | Yes | Python apps |
| Heroku | $7+/mo | 10 min | No | Teams |
| AWS/Azure | Variable | 30 min | Yes | Enterprise |

---

## 🆘 Troubleshooting

### App Crashes After Deploy
- Check logs for errors
- Verify `requirements.txt` has all dependencies
- Check if API key is set correctly

### Timeout Errors
- OpenAI requests can take 30+ seconds
- Increase timeout in your deployment settings

### 404 Errors
- Make sure Flask is running on port 5000 (or configured port)
- Check `Start Command` is correct

### API Key Not Working
- Verify key is valid on OpenAI dashboard
- Check for typos in environment variable
- Ensure API key has correct permissions

---

## 🚀 Recommended Next Steps

1. **Deploy on Render** (easiest, free)
2. **Add custom domain** (optional)
3. **Set up CI/CD** (auto-deploy on push)
4. **Add analytics** (track usage)
5. **Monitor errors** (use logging service)

---

## 📚 Useful Links

- **Render Docs**: https://render.com/docs
- **Railway Docs**: https://docs.railway.app
- **PythonAnywhere Docs**: https://help.pythonanywhere.com
- **Heroku Docs**: https://devcenter.heroku.com
- **Flask Deployment**: https://flask.palletsprojects.com/deployment

---

## 💬 Need Help?

If deployment fails:
1. Check the logs on your platform
2. Verify API key is correct
3. Ensure all dependencies are in `requirements.txt`
4. Test locally: `python app.py`

Happy deploying! 🎉
