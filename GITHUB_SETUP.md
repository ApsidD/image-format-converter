# GitHub Setup Instructions

## 🚀 Quick Setup (After Installing Git)

### 1. Initialize Repository
```bash
git init
git add .
git commit -m "Initial commit: Image Format Converter v1.0.0"
```

### 2. Create GitHub Repository
1. Go to https://github.com/new
2. Repository name: `image-format-converter`
3. Description: `A modern, user-friendly desktop application for converting images between different formats`
4. Choose: **Public**
5. **DO NOT** initialize with README, .gitignore, or license (we already have them)
6. Click "Create repository"

### 3. Push to GitHub
```bash
git remote add origin https://github.com/YOUR_USERNAME/image-format-converter.git
git branch -M main
git push -u origin main
```

---

## 🎉 Automated Multi-Platform Releases

**Good news!** This project includes GitHub Actions that **automatically build installers for Windows, macOS, and Linux** when you create a release!

### How to Create a Release (with automatic builds):

1. **Make sure your code is pushed to GitHub** (see above)

2. **Create a new release tag locally:**
```bash
git tag v1.0.0
git push origin v1.0.0
```

3. **Create the release on GitHub:**
   - Go to your repository on GitHub
   - Click "Releases" → "Draft a new release"
   - Choose the tag you just pushed: `v1.0.0`
   - Release title: `Image Format Converter v1.0.0`
   - Description:
   ```markdown
   ## 🖼️ Image Format Converter v1.0.0

   A modern, user-friendly desktop application for converting images between different formats.

   ### ✨ Features
   - Convert between JPEG, PNG, BMP, TIFF, WEBP, and GIF
   - Drag & drop interface
   - Quality control for JPEG and WEBP
   - Live file size preview
   - Modern dark UI with saved preferences

   ### 📥 Installation
   Download the file for your operating system below:
   - **Windows**: `ImageFormatConverter-Windows.exe` - Just download and run!
   - **macOS**: `ImageFormatConverter-macOS.dmg` - Open and drag to Applications
   - **Linux**: `ImageFormatConverter-Linux.tar.gz` - Extract and run

   No Python installation required!

   ### 🆕 What's New
   - Initial release
   - Full drag & drop support
   - Multi-format conversion
   - Quality adjustment for lossy formats
   ```

4. **Click "Publish release"**

5. **Wait for builds to complete** (~10-15 minutes)
   - GitHub Actions will automatically build executables for all 3 platforms
   - The installers will be automatically attached to your release
   - You can watch the progress in the "Actions" tab

### Manual Build (Optional)

If you want to build locally for Windows:
```bash
pip install pyinstaller
pyinstaller ImageFormatConverter.spec
```

The executable will be in `dist/ImageFormatConverter.exe`

---

## 🔧 Troubleshooting

### Actions Not Running?
- Make sure the repository is public or you have GitHub Actions enabled
- Check the "Actions" tab for any errors
- Verify the workflow file exists at `.github/workflows/release.yml`

### Build Failing?
- Check the Actions logs for specific errors
- Most common issue: dependencies not installing correctly
- macOS builds sometimes fail on first try - just re-run them

---

## Quick Commands Reference

```bash
# Check status
git status

# Add changes
git add .

# Commit changes
git commit -m "Your message"

# Push changes
git push

# Create and push tag for release
git tag v1.0.0
git push origin v1.0.0
```

