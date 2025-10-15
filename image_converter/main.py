"""Main application module for the Image Format Converter."""
import os
import json
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinterdnd2 import TkinterDnD
from PIL import Image, ImageTk
import io
import appdirs
from typing import Optional, Dict, Any

from .constants import (
    COLORS,
    FORMATS,
    WINDOW_DEFAULTS,
    DEFAULT_QUALITY,
    MIN_QUALITY,
    MAX_QUALITY,
    COMPANY_NAME,
    APP_NAME,
    BYTES_PER_KB,
    BYTES_PER_MB
)
from .ui import UISetupMixin
from .utils.exceptions import ImageLoadError, ImageSaveError, ConfigError

class ImageFormatConverter(UISetupMixin):
    """Main application class for converting image formats.
    
    This class handles the main application logic including:
    - Loading and displaying images
    - Converting between different formats
    - Saving converted images
    - Managing window state and configuration
    
    The UI setup methods are provided by the UISetupMixin.
    """
    
    def __init__(self, root: TkinterDnD.Tk) -> None:
        """Initialize the application.
        
        Args:
            root: The main Tkinter window
        """
        self.root = root
        self.root.title("🖼️ Image Format Converter")
        self.root.resizable(True, True)
        
        # Load or create config
        self.config = self.load_config()
        
        # Bind window events
        self.root.bind('<Configure>', self.on_window_configure)
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        # Set up theme colors
        self.colors = COLORS
        self.root.configure(bg=self.colors['bg'])
        
        # Initialize variables
        self.source_image: Optional[Image.Image] = None
        self.source_filename: Optional[str] = None
        self.source_path: Optional[str] = None
        self.quality_var = tk.IntVar(value=DEFAULT_QUALITY)
        self.format_var = tk.StringVar(value="JPEG")
        self.file_size_var = tk.StringVar(value="No file selected")
        
        # Store supported formats
        self.formats = FORMATS
        
        # Set up UI
        self.setup_ui()
    
    def get_config_path(self) -> str:
        """Get the path to the config file.
        
        Returns:
            The full path to the config file.
            
        Raises:
            ConfigError: If the config directory cannot be created.
        """
        try:
            config_dir = appdirs.user_config_dir(APP_NAME, COMPANY_NAME)
            os.makedirs(config_dir, exist_ok=True)
            return os.path.join(config_dir, "config.json")
        except Exception as e:
            raise ConfigError(f"Could not create config directory: {e}")
    
    def load_config(self) -> Dict[str, Any]:
        """Load configuration from file or return defaults.
        
        Returns:
            A dictionary containing the configuration.
        """
        config_path = self.get_config_path()
        defaults = {
            "window": {
                "width": WINDOW_DEFAULTS["default_width"],
                "height": WINDOW_DEFAULTS["default_height"],
                "x": None,
                "y": None
            }
        }
        
        try:
            if os.path.exists(config_path):
                with open(config_path, 'r') as f:
                    config = json.load(f)
                    defaults["window"].update(config.get("window", {}))
        except Exception:
            pass  # Use defaults if config cannot be loaded
        
        return defaults
    
    def save_config(self) -> None:
        """Save current configuration to file."""
        try:
            config_path = self.get_config_path()
            with open(config_path, 'w') as f:
                json.dump(self.config, f, indent=4)
        except Exception:
            pass  # Silently ignore config save errors
    
    def on_window_configure(self, event: Optional[tk.Event] = None) -> None:
        """Handle window resize/move events.
        
        Args:
            event: The window configure event
        """
        if event and event.widget == self.root:
            self.config["window"].update({
                "width": self.root.winfo_width(),
                "height": self.root.winfo_height(),
                "x": self.root.winfo_x(),
                "y": self.root.winfo_y()
            })
    
    def on_closing(self) -> None:
        """Handle window closing event."""
        self.save_config()
        self.root.destroy()
    
    def load_image(self, file_path: str, reloading: bool = False) -> None:
        """Load and display an image.
        
        Args:
            file_path: Path to the image file
            reloading: Whether this is a reload of an existing image
            
        Raises:
            ImageLoadError: If the image cannot be loaded or displayed
        """
        try:
            if not reloading:
                self.source_image = Image.open(file_path)
                self.source_path = file_path
                self.source_filename = os.path.splitext(os.path.basename(file_path))[0]
            
            container_width = self.drop_container.winfo_width()
            container_height = self.drop_container.winfo_height()
            
            if container_width > 0 and container_height > 0:
                # Calculate aspect ratio
                img_ratio = self.source_image.width / self.source_image.height
                container_ratio = container_width / container_height
                
                if img_ratio > container_ratio:
                    new_width = container_width
                    new_height = int(container_width / img_ratio)
                else:
                    new_height = container_height
                    new_width = int(container_height * img_ratio)
                
                # Resize image maintaining aspect ratio
                preview_image = self.source_image.copy()
                preview_image.thumbnail((new_width, new_height), Image.Resampling.LANCZOS)
                
                photo = ImageTk.PhotoImage(preview_image)
                self.drop_area.configure(image=photo, text="")
                self.drop_area.image = photo
            
            self.convert_button.configure(state="normal")
            self.update_file_size_preview()
            self.on_format_change()
            
        except Exception as e:
            raise ImageLoadError(f"Could not load image: {e}")
    
    def convert_and_save(self) -> None:
        """Convert and save the image in the selected format."""
        if not self.source_image:
            messagebox.showerror("Error", "Please select an image first")
            return
        
        try:
            format_name = self.format_var.get()
            
            # Convert image
            converted_image = (
                self.source_image.convert('RGB')
                if format_name == "JPEG"
                else self.source_image.copy()
            )
            
            # Get file extension and prepare save dialog
            extensions = self.formats[format_name]
            default_ext = extensions[0]
            
            # Prepare default filename
            default_filename = f"{self.source_filename} {format_name}{default_ext}"
            
            # Get the directory of the source file
            initial_dir = (
                os.path.dirname(self.source_path)
                if self.source_path
                else None
            )
            
            # Ask for save location
            file_path = filedialog.asksaveasfilename(
                title="Save Converted Image",
                defaultextension=default_ext,
                initialfile=default_filename,
                initialdir=initial_dir,
                filetypes=[
                    (f"{format_name} files", f"*{default_ext}"),
                    ("All files", "*.*")
                ]
            )
            
            if file_path:
                # Save with appropriate settings
                save_kwargs = {}
                if format_name in ["JPEG", "WEBP"]:
                    save_kwargs["quality"] = self.quality_var.get()
                
                try:
                    converted_image.save(
                        file_path,
                        format=format_name,
                        **save_kwargs
                    )
                except (IOError, OSError) as e:
                    raise ImageSaveError(f"Could not save the image: {e}")
                
        except ImageSaveError as e:
            messagebox.showerror("Save Error", str(e))
        except Exception as e:
            messagebox.showerror(
                "Error",
                f"An unexpected error occurred:\n{str(e)}"
            )
    
    def update_file_size_preview(self) -> None:
        """Update the file size preview."""
        if not self.source_image:
            self.file_size_var.set("No file selected")
            return
        
        try:
            temp_buffer = io.BytesIO()
            format_name = self.format_var.get()
            
            save_kwargs = {}
            if format_name in ["JPEG", "WEBP"]:
                save_kwargs["quality"] = self.quality_var.get()
            
            if format_name == "JPEG":
                self.source_image.convert('RGB').save(
                    temp_buffer,
                    format=format_name,
                    **save_kwargs
                )
            else:
                self.source_image.save(
                    temp_buffer,
                    format=format_name,
                    **save_kwargs
                )
            
            size_bytes = temp_buffer.tell()
            size_str = self._format_file_size(size_bytes)
            self.file_size_var.set(size_str)
            
        except Exception:
            self.file_size_var.set("Error calculating size")
    
    def on_drop(self, event: tk.Event) -> None:
        """Handle file drop events.
        
        Args:
            event: The drop event containing file paths
        """
        files = self.root.tk.splitlist(event.data)
        if files:
            try:
                self.load_image(files[0])
            except ImageLoadError as e:
                messagebox.showerror("Error", str(e))
    
    def browse_file(self, event: tk.Event) -> None:
        """Handle file browse events.
        
        Args:
            event: The click event
        """
        file_path = filedialog.askopenfilename(
            title="Select Image File",
            filetypes=[
                ("Image files", "*.jpg *.jpeg *.png *.bmp *.tiff *.tif *.webp *.gif"),
                ("All files", "*.*")
            ]
        )
        if file_path:
            try:
                self.load_image(file_path)
            except ImageLoadError as e:
                messagebox.showerror("Error", str(e))
    
    def on_format_change(self, event: Optional[tk.Event] = None) -> None:
        """Handle format selection changes.
        
        Args:
            event: The combobox selection event (optional)
        """
        format_name = self.format_var.get()
        
        if format_name in ["JPEG", "WEBP"]:
            self.quality_frame.grid()
        else:
            self.quality_frame.grid_remove()
        
        if self.source_image:
            self.update_file_size_preview()
    
    def on_quality_change(self, value: str) -> None:
        """Handle quality slider changes.
        
        Args:
            value: The slider value as a string
        """
        self.quality_var.set(int(float(value)))
        if self.source_image:
            self.update_file_size_preview()
    
    def on_quality_entry_change(self, event: tk.Event) -> None:
        """Handle quality entry changes.
        
        Validates the quality value and updates the preview if valid.
        """
        try:
            value = int(self.quality_entry.get())
            if MIN_QUALITY <= value <= MAX_QUALITY:
                self.quality_var.set(value)
                if self.source_image:
                    self.update_file_size_preview()
        except ValueError:
            pass  # Invalid input, ignore
    
    def show_quality_controls(self) -> None:
        """Show the quality control panel for formats that support quality settings."""
        self.quality_frame.grid()
    
    def hide_quality_controls(self) -> None:
        """Hide the quality control panel for formats that don't support quality settings."""
        self.quality_frame.grid_remove()
    
    def _format_file_size(self, size_bytes: int) -> str:
        """Format file size in bytes to human-readable string.
        
        Args:
            size_bytes: Size in bytes
            
        Returns:
            Formatted size string (e.g., "1.5 MB", "234 KB", "789 B")
        """
        if size_bytes < BYTES_PER_KB:
            return f"{size_bytes} B"
        elif size_bytes < BYTES_PER_MB:
            return f"{size_bytes / BYTES_PER_KB:.1f} KB"
        else:
            return f"{size_bytes / BYTES_PER_MB:.1f} MB"
