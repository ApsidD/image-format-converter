"""Constants and configuration for the Image Format Converter."""
from typing import Dict, List, Final

# Color scheme
COLORS: Final[Dict[str, str]] = {
    'bg': '#0f172a',           # Dark blue-gray background
    'card': '#1e293b',         # Dark gray cards
    'primary': '#3b82f6',      # Blue primary
    'secondary': '#64748b',    # Gray secondary
    'success': '#10b981',      # Green success
    'warning': '#f59e0b',      # Orange warning
    'border': '#334155',       # Dark border
    'text': '#f1f5f9',         # Light text
    'text_light': '#94a3b8',   # Muted light text
    'input_bg': '#334155',     # Input background
    'hover_primary': '#2563eb', # Darker blue for hover
    'hover_success': '#059669'  # Darker green for hover
}

# Supported image formats
FORMATS: Final[Dict[str, List[str]]] = {
    "JPEG": [".jpg", ".jpeg"],
    "PNG": [".png"],
    "BMP": [".bmp"],
    "TIFF": [".tiff", ".tif"],
    "WEBP": [".webp"],
    "GIF": [".gif"]
}

# Window configuration
WINDOW_DEFAULTS: Final[Dict[str, int]] = {
    "min_width": 350,
    "min_height": 540,
    "default_width": 400,
    "default_height": 600,
}

# Quality settings
DEFAULT_QUALITY: Final[int] = 85
MIN_QUALITY: Final[int] = 1
MAX_QUALITY: Final[int] = 100

# Application info for config directory
COMPANY_NAME: Final[str] = "ImageFormatConverter"
APP_NAME: Final[str] = "ImageFormatConverter"

# UI Configuration
DROP_AREA_MIN_HEIGHT: Final[int] = 200  # Minimum height for image preview area

# File size formatting thresholds
BYTES_PER_KB: Final[int] = 1024
BYTES_PER_MB: Final[int] = 1024 * 1024
