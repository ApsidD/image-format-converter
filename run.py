"""Entry point for the Image Format Converter application."""
from tkinterdnd2 import TkinterDnD
from image_converter import ImageFormatConverter
from image_converter.constants import WINDOW_DEFAULTS

def main():
    """Run the Image Format Converter application."""
    # Create main window
    root = TkinterDnD.Tk()
    
    # Set minimum window size
    root.minsize(
        WINDOW_DEFAULTS["min_width"],
        WINDOW_DEFAULTS["min_height"]
    )
    
    # Create application instance
    app = ImageFormatConverter(root)
    
    # Apply saved window geometry
    if app.config["window"]["x"] is not None:
        # Use saved position
        geometry = (
            f"{app.config['window']['width']}x{app.config['window']['height']}"
            f"+{app.config['window']['x']}+{app.config['window']['y']}"
        )
    else:
        # First run - center the window
        width = app.config["window"]["width"]
        height = app.config["window"]["height"]
        x = (root.winfo_screenwidth() - width) // 2
        y = (root.winfo_screenheight() - height) // 2
        geometry = f"{width}x{height}+{x}+{y}"
    
    root.geometry(geometry)
    root.mainloop()

if __name__ == "__main__":
    main()
