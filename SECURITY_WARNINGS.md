# 🛡️ About Security Warnings

When users download your Windows executable, they may see browser warnings like:
> "ImageFormatConverter-Windows.exe isn't commonly downloaded. Make sure you trust ImageFormatConverter-Windows.exe before you open it."

**This is normal for unsigned open-source software.** Here's why it happens and what you can do about it.

---

## 🤔 Why Does This Happen?

Modern browsers and Windows show warnings for executables that aren't **digitally signed** with a trusted code signing certificate. This is a security feature to protect users from malware.

Your app is safe, but browsers can't verify that automatically without a signature.

---

## ✅ Solutions

### **Option 1: Add Documentation** (✅ DONE - Free)
We've added a warning notice in the README explaining this is normal. Users who read the README will understand.

### **Option 2: Get a Code Signing Certificate** ($100-400/year)
This is the most professional solution but costs money.

**Popular Certificate Providers:**
- **DigiCert** - ~$400/year (most trusted)
- **Sectigo (Comodo)** - ~$200/year
- **GlobalSign** - ~$300/year
- **SignPath Foundation** - FREE for open-source projects! (https://signpath.org/)

**How it works:**
1. Purchase certificate and verify your identity
2. Receive certificate file (.pfx)
3. Sign your .exe during the build process
4. Browsers and Windows will trust the file

**To implement code signing in GitHub Actions:**
```yaml
- name: Sign Windows executable
  run: |
    # Store certificate as GitHub Secret
    signtool sign /f certificate.pfx /p ${{ secrets.CERT_PASSWORD }} /tr http://timestamp.digicert.com /td sha256 /fd sha256 dist/ImageFormatConverter.exe
```

### **Option 3: Build Reputation Over Time** (Free - Slow)
As more people download and use your app safely, Microsoft SmartScreen learns it's safe. After enough downloads, the warnings may reduce.

**Typical timeline:** 100-1000+ downloads needed

### **Option 4: Create a Proper Installer** (Free - Better UX)
Instead of distributing a raw .exe, create an installer using:

**Installer Tools:**
- **NSIS** (Nullsoft Scriptable Install System) - Free, popular
- **Inno Setup** - Free, easy to use
- **WiX Toolset** - Free, Microsoft's standard

**Benefits:**
- Looks more professional
- Can add to Start Menu, Desktop
- Proper uninstaller
- Still unsigned, but feels more "legitimate"

**Example with Inno Setup:**
```iss
[Setup]
AppName=Image Format Converter
AppVersion=1.0.0
DefaultDirName={autopf}\ImageFormatConverter
OutputBaseFilename=ImageFormatConverter-Setup
Compression=lzma2
SolidCompression=yes

[Files]
Source: "dist\ImageFormatConverter.exe"; DestDir: "{app}"

[Icons]
Name: "{autoprograms}\Image Format Converter"; Filename: "{app}\ImageFormatConverter.exe"
```

### **Option 5: Distribute via Microsoft Store** (Free - Most Trusted)
Apps from Microsoft Store are automatically trusted.

**Pros:**
- No code signing needed
- Automatic updates
- Built-in trust

**Cons:**
- Requires Microsoft Developer account ($20 one-time)
- App review process
- More complex setup

### **Option 6: Use VirusTotal Scan** (Free)
Upload your releases to VirusTotal and share the scan results. This shows users that major antivirus engines trust your app.

1. Go to https://www.virustotal.com
2. Upload your .exe
3. Add the scan link to your release notes

---

## 📊 Recommendation by Budget

| Solution | Cost | Effort | Effectiveness |
|----------|------|--------|---------------|
| Documentation (✅ Done) | Free | Low | Medium |
| SignPath (Open Source) | Free | Medium | High |
| VirusTotal Scans | Free | Low | Medium |
| Create Installer | Free | Medium | Medium-High |
| Build Reputation | Free | None (just wait) | Medium (slow) |
| Buy Certificate | $200-400/year | High | Very High |
| Microsoft Store | $20 one-time | High | Very High |

---

## 🎯 Recommended Path

### **Immediate** (Already Done ✅)
- Added warning documentation in README
- Users now know what to expect

### **Short-term** (Free)
1. Apply for **SignPath Foundation** (free for open source)
   - Visit: https://signpath.org/
   - Fill out application
   - If approved, integrate into GitHub Actions

2. Upload releases to **VirusTotal**
   - Scan each release
   - Add scan link to release notes

### **Long-term** (If Project Grows)
- Consider purchasing a code signing certificate ($200-400/year)
- Or submit to Microsoft Store ($20 one-time)

---

## 🔐 For Users: How to Verify Safety

Users can verify your app is safe by:

1. **Check the source code** - It's all visible in this GitHub repo
2. **Scan with VirusTotal** - Upload the file to virustotal.com
3. **Review the GitHub Actions logs** - See exactly how the build happened
4. **Check the repository history** - See all changes over time

Your app is open source, so anyone can audit it!

---

## 📝 Next Steps

If you want to implement code signing:

1. **Try SignPath Foundation first** (free for open source)
   - https://signpath.org/
   
2. **Or create an installer** with Inno Setup
   - https://jrsoftware.org/isinfo.php

3. **Or buy a certificate** if you prefer
   - Start with Sectigo (~$200/year)

Let me know if you want help implementing any of these solutions!

