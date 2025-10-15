# 🖼️ Image Format Converter

[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc/4.0/)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey)](https://github.com/ApsidD/image-format-converter/releases)

A modern, user-friendly desktop application for converting images between different formats with ease.

![App Screenshot](assets/converter_icon_256.png)

## 📥 Download

**[Download the latest release for your platform](https://github.com/ApsidD/image-format-converter/releases/latest)**

- 🪟 **Windows**: `ImageFormatConverter-Windows.exe`
- 🍎 **macOS**: `ImageFormatConverter-macOS.dmg`
- 🐧 **Linux**: `ImageFormatConverter-Linux.tar.gz`

No Python installation required - just download and run!

## Features

- **Multiple Format Support**: Convert between JPEG, PNG, BMP, TIFF, WEBP, and GIF
- **Drag & Drop Interface**: Simply drag and drop images into the application
- **Quality Control**: Adjust quality settings for JPEG and WEBP formats
- **Live Preview**: See file size estimates before saving
- **Smart Defaults**: Automatically suggests output filename and location
- **Resizable Interface**: Window size and position are remembered between sessions
- **Modern Dark UI**: Beautiful, professional-looking interface

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Setup

1. Clone or download this repository

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

### Running the Application

```bash
python run.py
```

## Building an Executable

To create a standalone executable:

```bash
pyinstaller ImageFormatConverter.spec
```

The executable will be created in the `dist` folder.

## Usage

1. **Load an Image**:
   - Drag and drop an image file into the drop area, or
   - Click the drop area to browse for a file

2. **Select Output Format**:
   - Choose your desired format from the dropdown menu

3. **Adjust Quality** (optional):
   - For JPEG and WEBP formats, adjust the quality slider
   - Higher quality = larger file size

4. **Convert & Save**:
   - Click "Convert & Save"
   - The save dialog will open with a suggested filename in the source folder
   - Choose your save location and click Save

## Project Structure

```
image_converter/
├── image_converter/          # Main package
│   ├── __init__.py          # Package initialization
│   ├── constants.py         # Application constants and configuration
│   ├── main.py              # Main application logic
│   ├── ui/                  # UI components
│   │   ├── __init__.py
│   │   └── mixins.py        # UI setup mixin
│   └── utils/               # Utility modules
│       ├── __init__.py
│       └── exceptions.py    # Custom exceptions
├── run.py                   # Application entry point
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## Configuration

The application stores its configuration in a platform-specific location:
- **Windows**: `%APPDATA%\ImageFormatConverter\config.json`
- **macOS**: `~/Library/Application Support/ImageFormatConverter/config.json`
- **Linux**: `~/.config/ImageFormatConverter/config.json`

This configuration includes:
- Window size and position
- Last used settings

## Development

### Code Quality

The codebase follows modern Python best practices:
- **Type Hints**: Used throughout for better code clarity
- **Docstrings**: Comprehensive documentation for all classes and methods
- **Modular Design**: Separated concerns with proper package structure
- **Error Handling**: Custom exceptions for different error types
- **Constants Management**: Centralized configuration

### Contributing

1. Follow PEP 8 style guidelines
2. Add type hints to all function signatures
3. Include docstrings for new classes and methods
4. Test thoroughly before submitting changes

## 📄 License

This project is licensed under the Creative Commons Attribution-NonCommercial 4.0 International License - see the [LICENSE](LICENSE) file for details.

**⚠️ Non-Commercial Use Only**: This software may NOT be sold, distributed for money, or used in paid subscriptions or commercial services.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 🐛 Bug Reports

Found a bug? Please [open an issue](https://github.com/ApsidD/image-format-converter/issues) with:
- Description of the bug
- Steps to reproduce
- Expected behavior
- Screenshots (if applicable)
- Your OS and Python version

## ⭐ Show Your Support

Give a ⭐️ if this project helped you!

## Acknowledgments

- Built with [Tkinter](https://docs.python.org/3/library/tkinter.html)
- Drag & drop powered by [tkinterdnd2](https://github.com/pmgagne/tkinterdnd2)
- Image processing with [Pillow](https://python-pillow.org/)

