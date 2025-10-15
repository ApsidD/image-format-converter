"""Custom exceptions for the Image Format Converter."""

class ImageConverterError(Exception):
    """Base exception for image converter errors."""
    pass

class ImageLoadError(ImageConverterError):
    """Raised when an image cannot be loaded."""
    pass

class ImageSaveError(ImageConverterError):
    """Raised when an image cannot be saved."""
    pass

class ConfigError(ImageConverterError):
    """Raised when there's an error with configuration."""
    pass
