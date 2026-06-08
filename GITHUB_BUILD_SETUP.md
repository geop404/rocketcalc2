# Rocketcalc - Android APK Builder Setup

## Quick Start: Build APK on GitHub (Recommended)

### Step 1: Create GitHub Account
- Go to https://github.com
- Sign up (free)

### Step 2: Create Repository
- Click "New" to create a new repository
- Name it: `rocketcalc`
- Choose "Public" (free tier)
- Click "Create repository"

### Step 3: Upload Your Project
You have two options:

**Option A: Git Command Line (if you have Git installed)**
```bash
cd c:\fgt2eth\projekt
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/rocketcalc.git
git push -u origin main
```

**Option B: GitHub Web Interface**
1. Go to your repository on GitHub
2. Click "Add file" → "Upload files"
3. Select all files from your `c:\fgt2eth\projekt` folder
4. Click "Commit changes"

### Step 4: Automatic Build Starts!
- GitHub Actions automatically starts building when you upload
- Go to the "Actions" tab to watch the build progress
- When done (5-15 minutes), click the latest workflow run
- Scroll down and download the APK from "Artifacts"

---

## What Gets Built

The APK will be ready to download from GitHub Actions artifacts:
- **Filename**: `rocketcalc-0.1-arm64-v8a-release.apk`
- **Size**: ~50-100 MB

---

## How to Install on Android

1. Transfer the APK to your Android phone (USB or email)
2. On your phone: Settings → Security → Enable "Unknown Sources"
3. Open file manager and tap the APK
4. Tap "Install"
5. Run the "Rocketcalc" app!

---

## Troubleshooting

**Build fails?**
- Check the build log in GitHub Actions → click the failed job
- Common issues are usually dependency-related
- Make sure `buildozer.spec` is correct

**APK too large?**
- Normal for Kivy apps (includes Python runtime)
- First builds are larger; subsequent builds cache dependencies

**App crashes on Android?**
- Check app permissions in `buildozer.spec`
- Ensure minimum Android API is 21+

---

## Questions?

Buildozer documentation: https://buildozer.readthedocs.io/
Kivy documentation: https://kivy.org/doc/stable/

Good luck building! 🚀
