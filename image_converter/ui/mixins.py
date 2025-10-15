"""UI setup mixins for the Image Format Converter."""
import tkinter as tk
from tkinter import ttk
from tkinterdnd2 import DND_FILES
from typing import Any

from ..constants import COLORS, DROP_AREA_MIN_HEIGHT

class UISetupMixin:
    """Mixin class containing UI setup methods.
    
    This mixin provides methods for setting up different parts of the UI.
    It expects to be mixed into a class that has the following attributes:
        - root: The main Tkinter window
        - colors: Color scheme dictionary
        - formats: Supported formats dictionary
        - quality_var: Quality IntVar
        - format_var: Format StringVar
        - file_size_var: File size StringVar
    """
    
    def setup_ui(self: Any) -> None:
        """Set up the main UI components."""
        # Main frame with modern styling
        main_frame = tk.Frame(self.root, bg=self.colors['bg'], padx=10, pady=10)
        main_frame.grid(row=0, column=0, sticky='nsew')
        
        # Configure root window grid
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        
        # Configure grid weights for vertical scaling
        main_frame.grid_rowconfigure(1, weight=1)  # Drop area gets most space
        main_frame.grid_rowconfigure(2, weight=0)  # Format selection
        main_frame.grid_rowconfigure(3, weight=0)  # Quality settings
        main_frame.grid_rowconfigure(4, weight=0)  # File size preview
        main_frame.grid_rowconfigure(5, weight=0)  # Convert button
        main_frame.grid_columnconfigure(0, weight=1)
        
        # Header
        self.setup_header(main_frame)
        
        # Main components
        drop_frame = self.setup_drop_area(main_frame)
        drop_frame.grid(row=1, column=0, sticky='nsew', padx=5, pady=5)
        
        format_frame = self.setup_format_selection(main_frame)
        format_frame.grid(row=2, column=0, sticky='ew', padx=5, pady=5)
        
        quality_frame = self.setup_quality_control(main_frame)
        quality_frame.grid(row=3, column=0, sticky='ew', padx=5, pady=5)
        
        size_frame = self.setup_file_size_preview(main_frame)
        size_frame.grid(row=4, column=0, sticky='ew', padx=5, pady=5)
        
        self.setup_convert_button(main_frame)
    
    def setup_header(self: Any, parent: tk.Widget) -> None:
        """Set up the header with title and subtitle."""
        header_frame = tk.Frame(parent, bg=self.colors['bg'])
        header_frame.grid(row=0, column=0, sticky='ew', pady=(0, 5))
        
        header_frame.grid_columnconfigure(0, weight=1)
        header_frame.grid_rowconfigure(0, weight=0)
        header_frame.grid_rowconfigure(1, weight=0)
        
        title_label = tk.Label(
            header_frame,
            text="🖼️ Image Format Converter",
            font=("Segoe UI", 16, "bold"),
            fg=self.colors['text'],
            bg=self.colors['bg']
        )
        title_label.grid(row=0, column=0, sticky='ew')
        
        subtitle_label = tk.Label(
            header_frame,
            text="Convert images between different formats with ease",
            font=("Segoe UI", 9),
            fg=self.colors['text_light'],
            bg=self.colors['bg']
        )
        subtitle_label.grid(row=1, column=0, sticky='ew', pady=(2, 0))
    
    def setup_drop_area(self: Any, parent: tk.Widget) -> tk.Frame:
        """Set up the drop area for images."""
        # Drop area frame with modern card styling
        drop_frame = tk.Frame(parent, bg=self.colors['card'], relief='flat', bd=0)
        drop_frame.grid_columnconfigure(0, weight=1)
        drop_frame.grid_rowconfigure(1, weight=1)
        
        # Card title
        title_frame = tk.Frame(drop_frame, bg=self.colors['card'])
        title_frame.grid(row=0, column=0, sticky='ew', padx=8, pady=(8, 4))
        
        title_frame.grid_columnconfigure(0, weight=1)
        title_label = tk.Label(
            title_frame,
            text="📁 Upload Image",
            font=("Segoe UI", 12, "bold"),
            fg=self.colors['text'],
            bg=self.colors['card']
        )
        title_label.grid(row=0, column=0, sticky='w')
        
        # Content frame
        content_frame = tk.Frame(drop_frame, bg=self.colors['card'])
        content_frame.grid(row=1, column=0, sticky='nsew', padx=8, pady=(0, 8))
        content_frame.grid_columnconfigure(0, weight=1)
        content_frame.grid_rowconfigure(0, weight=1)
        
        # Container frame for drop area
        self.drop_container = tk.Frame(content_frame, bg=self.colors['input_bg'])
        self.drop_container.grid(row=0, column=0, sticky='nsew')
        self.drop_container.grid_rowconfigure(0, weight=1)
        self.drop_container.grid_columnconfigure(0, weight=1)
        
        # Make container maintain minimum height
        def maintain_ratio(event):
            width = event.width
            self.drop_container.configure(height=DROP_AREA_MIN_HEIGHT)
            if hasattr(self, 'source_image') and self.source_image:
                self.load_image(None, reloading=True)
        
        self.drop_container.bind('<Configure>', maintain_ratio)
        
        # Drop area label
        self.drop_area = tk.Label(
            self.drop_container,
            text="📤 Drag and drop an image file here\nor click to browse",
            bg=self.colors['input_bg'],
            relief='flat',
            bd=2,
            font=("Segoe UI", 11),
            fg=self.colors['text_light'],
            cursor="hand2"
        )
        self.drop_area.grid(row=0, column=0, sticky='nsew')
        
        # Bind drag and drop
        self.drop_area.drop_target_register(DND_FILES)
        self.drop_area.dnd_bind('<<Drop>>', self.on_drop)
        self.drop_area.bind('<Button-1>', self.browse_file)
        
        return drop_frame
    
    def setup_format_selection(self: Any, parent: tk.Widget) -> tk.Frame:
        """Set up the format selection area."""
        # Format selection frame with modern card styling
        format_frame = tk.Frame(parent, bg=self.colors['card'], relief='flat', bd=0)
        format_frame.grid_columnconfigure(0, weight=1)
        
        # Card title
        title_frame = tk.Frame(format_frame, bg=self.colors['card'])
        title_frame.grid(row=0, column=0, sticky='ew', padx=8, pady=(8, 4))
        
        title_frame.grid_columnconfigure(0, weight=1)
        title_label = tk.Label(
            title_frame,
            text="⚙️ Output Format",
            font=("Segoe UI", 12, "bold"),
            fg=self.colors['text'],
            bg=self.colors['card']
        )
        title_label.grid(row=0, column=0, sticky='w')
        
        # Content frame
        content_frame = tk.Frame(format_frame, bg=self.colors['card'])
        content_frame.grid(row=1, column=0, sticky='ew', padx=8, pady=(0, 8))
        content_frame.grid_columnconfigure(1, weight=1)
        
        format_label = tk.Label(
            content_frame,
            text="Select format:",
            font=("Segoe UI", 11),
            fg=self.colors['text'],
            bg=self.colors['card']
        )
        format_label.grid(row=0, column=0, padx=(0, 10))
        
        # Modern combobox styling
        format_combo = ttk.Combobox(
            content_frame,
            textvariable=self.format_var,
            values=list(self.formats.keys()),
            state="readonly",
            font=("Segoe UI", 10)
        )
        format_combo.grid(row=0, column=1, sticky='ew')
        format_combo.bind('<<ComboboxSelected>>', self.on_format_change)
        
        return format_frame
    
    def setup_quality_control(self: Any, parent: tk.Widget) -> tk.Frame:
        """Set up the quality control area."""
        # Quality control frame with modern card styling
        self.quality_frame = tk.Frame(parent, bg=self.colors['card'], relief='flat', bd=0)
        self.quality_frame.grid_columnconfigure(0, weight=1)
        
        # Card title
        title_frame = tk.Frame(self.quality_frame, bg=self.colors['card'])
        title_frame.grid(row=0, column=0, sticky='ew', padx=8, pady=(8, 4))
        
        title_frame.grid_columnconfigure(0, weight=1)
        title_label = tk.Label(
            title_frame,
            text="🎚️ Quality Settings",
            font=("Segoe UI", 12, "bold"),
            fg=self.colors['text'],
            bg=self.colors['card']
        )
        title_label.grid(row=0, column=0, sticky='w')
        
        # Content frame
        content_frame = tk.Frame(self.quality_frame, bg=self.colors['card'])
        content_frame.grid(row=1, column=0, sticky='ew', padx=8, pady=(0, 8))
        content_frame.grid_columnconfigure(1, weight=1)
        
        # Quality label
        quality_label = tk.Label(
            content_frame,
            text="Quality:",
            font=("Segoe UI", 11),
            fg=self.colors['text'],
            bg=self.colors['card']
        )
        quality_label.grid(row=0, column=0, padx=(0, 10))
        
        # Quality slider
        self.quality_slider = ttk.Scale(
            content_frame,
            from_=1,
            to=100,
            variable=self.quality_var,
            orient='horizontal',
            command=self.on_quality_change
        )
        self.quality_slider.grid(row=0, column=1, sticky='ew', padx=(0, 10))
        
        # Quality input field
        self.quality_entry = tk.Entry(
            content_frame,
            textvariable=self.quality_var,
            width=4,
            font=("Segoe UI", 10),
            relief='flat',
            bd=1,
            bg=self.colors['input_bg'],
            fg=self.colors['text'],
            insertbackground=self.colors['text']
        )
        self.quality_entry.grid(row=0, column=2)
        self.quality_entry.bind('<KeyRelease>', self.on_quality_entry_change)
        
        # Quality percentage label
        quality_percent_label = tk.Label(
            content_frame,
            text="%",
            font=("Segoe UI", 11),
            fg=self.colors['text'],
            bg=self.colors['card']
        )
        quality_percent_label.grid(row=0, column=3, padx=(3, 0))
        
        # Initially hide quality controls
        self.quality_frame.grid(row=3, column=0, sticky='ew', padx=5, pady=5)
        self.hide_quality_controls()
        
        return self.quality_frame
    
    def setup_file_size_preview(self: Any, parent: tk.Widget) -> tk.Frame:
        """Set up the file size preview area."""
        # File size preview frame with modern card styling
        size_frame = tk.Frame(parent, bg=self.colors['card'], relief='flat', bd=0)
        size_frame.grid_columnconfigure(0, weight=1)
        
        # Card title
        title_frame = tk.Frame(size_frame, bg=self.colors['card'])
        title_frame.grid(row=0, column=0, sticky='ew', padx=8, pady=(8, 4))
        
        title_frame.grid_columnconfigure(0, weight=1)
        title_label = tk.Label(
            title_frame,
            text="📊 File Size Preview",
            font=("Segoe UI", 12, "bold"),
            fg=self.colors['text'],
            bg=self.colors['card']
        )
        title_label.grid(row=0, column=0, sticky='w')
        
        # Content frame
        content_frame = tk.Frame(size_frame, bg=self.colors['card'])
        content_frame.grid(row=1, column=0, sticky='ew', padx=8, pady=(0, 8))
        content_frame.grid_columnconfigure(1, weight=1)
        
        size_label = tk.Label(
            content_frame,
            text="Estimated output size:",
            font=("Segoe UI", 11),
            fg=self.colors['text'],
            bg=self.colors['card']
        )
        size_label.grid(row=0, column=0, padx=(0, 10))
        
        self.size_value_label = tk.Label(
            content_frame,
            textvariable=self.file_size_var,
            font=("Segoe UI", 11, "bold"),
            fg=self.colors['primary'],
            bg=self.colors['card']
        )
        self.size_value_label.grid(row=0, column=1, sticky='ew')
        
        return size_frame
    
    def setup_convert_button(self: Any, parent: tk.Widget) -> None:
        """Set up the convert and save button."""
        self.convert_button = tk.Button(
            parent,
            text="💾 Convert & Save",
            command=self.convert_and_save,
            state="disabled",
            font=("Segoe UI", 12, "bold"),
            bg=self.colors['success'],
            fg='black',
            disabledforeground='black',
            activebackground=self.colors['hover_success'],
            activeforeground='black',
            relief='flat',
            bd=0,
            padx=20,
            pady=10,
            cursor="hand2"
        )
        self.convert_button.grid(row=5, column=0, sticky='ew', padx=5, pady=5)
        
        # Set up hover effects
        self.convert_button.bind(
            '<Enter>',
            lambda e: self.convert_button.configure(
                bg=self.colors['hover_success'],
                fg='black'
            )
        )
        self.convert_button.bind(
            '<Leave>',
            lambda e: self.convert_button.configure(
                bg=self.colors['success'],
                fg='black'
            )
        )