# 📤 How to Push to GitHub

Your local repository is ready! Follow these steps to upload to GitHub:

## Step 1: Create a GitHub Repository

1. Go to https://github.com/new
2. Enter repository name: **Ai-technical-dec-gen**
3. Add description: "AI Technical Documentation Generator"
4. Choose **Public** (or Private if preferred)
5. **DO NOT** check "Initialize with README" (we already have one)
6. Click **Create repository**

## Step 2: Push Your Code

After creating the repository on GitHub, run these commands in PowerShell:

```powershell
cd "c:\Users\RUPESH\OneDrive\Desktop\Gen Ai\Project"

# Add GitHub as remote
git remote add origin https://github.com/rupesh1820/Ai-technical-dec-gen.git

# Rename branch to main (if needed)
git branch -M main

# Push your code
git push -u origin main
```

## Step 3: GitHub Authentication

When pushing, you'll be prompted for authentication. Choose one:

### Option A: Personal Access Token (Recommended)
1. Go to https://github.com/settings/tokens
2. Click "Generate new token" → "Generate new token (classic)"
3. Give it a name: "Local Git Push"
4. Select scopes: ✅ repo (full control)
5. Click "Generate token"
6. Copy the token (you'll only see it once!)
7. Paste it when prompted for password in terminal

### Option B: SSH Key
1. Generate SSH key: `ssh-keygen -t ed25519`
2. Add to GitHub: https://github.com/settings/keys
3. Use SSH URL: `git@github.com:rupesh1820/Ai-technical-dec-gen.git`

### Option C: GitHub CLI (Easiest)
```powershell
# Install GitHub CLI
choco install gh

# Or download from: https://github.com/cli/cli

# Then authenticate
gh auth login

# Push code
git push -u origin main
```

---

## Complete Command Set

```powershell
cd "c:\Users\RUPESH\OneDrive\Desktop\Gen Ai\Project"
git remote add origin https://github.com/rupesh1820/Ai-technical-dec-gen.git
git branch -M main
git push -u origin main
```

---

## ✅ Verify Upload

After pushing, visit:
```
https://github.com/rupesh1820/Ai-technical-dec-gen
```

You should see:
- ✅ All your files
- ✅ README with instructions
- ✅ requirements.txt
- ✅ app.py
- ✅ templates/index.html

---

## 🔄 Future Updates

After initial push, use these simple commands:

```powershell
# Make changes, then:
git add .
git commit -m "Your description here"
git push
```

---

## ❓ Troubleshooting

### Authentication Failed
- Use GitHub CLI: `gh auth login`
- Or create Personal Access Token (more secure than password)

### Permission Denied (Public Key)
- Set up SSH keys: `ssh-keygen -t ed25519`
- Add to GitHub settings

### Repository Already Exists
```powershell
git remote remove origin
git remote add origin https://github.com/rupesh1820/Ai-technical-dec-gen.git
```

### Need to Change Remote URL
```powershell
git remote set-url origin https://github.com/rupesh1820/Ai-technical-dec-gen.git
```

---

## 📚 Learn More
- Git Documentation: https://git-scm.com/doc
- GitHub Docs: https://docs.github.com
