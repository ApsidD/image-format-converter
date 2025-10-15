# Architecture Documentation

## Overview

The Image Format Converter is built with a modular, maintainable architecture following modern Python best practices.

## Design Principles

1. **Separation of Concerns**: UI logic is separated from business logic
2. **DRY (Don't Repeat Yourself)**: Reusable components and constants
3. **Type Safety**: Type hints throughout for better IDE support and error prevention
4. **Error Handling**: Custom exceptions for different error types
5. **Configuration Management**: Centralized constants and user settings

## Package Structure

### `image_converter/` - Main Package

#### `main.py` - Application Core
- **Class**: `ImageFormatConverter`
- **Responsibility**: Core application logic and state management
- **Inheritance**: Inherits from `UISetupMixin` to get UI setup methods
- **Key Methods**:
  - `load_image()`: Load and display images
  - `convert_and_save()`: Convert and save images
  - `update_file_size_preview()`: Calculate estimated output size
  - Config management methods

#### `constants.py` - Configuration
- **Purpose**: Centralize all configuration values
- **Contents**:
  - `COLORS`: Theme color scheme
  - `FORMATS`: Supported image formats
  - `WINDOW_DEFAULTS`: Default window settings
  - Quality settings
  - Application metadata

#### `ui/` - User Interface Components

##### `mixins.py` - UI Setup Mixin
- **Class**: `UISetupMixin`
- **Purpose**: Separate UI creation from business logic
- **Methods**: All `setup_*` methods for creating UI components
- **Benefit**: Keeps main class focused on logic, not layout

#### `utils/` - Utility Modules

##### `exceptions.py` - Custom Exceptions
- **Classes**:
  - `ImageConverterError`: Base exception
  - `ImageLoadError`: Image loading failures
  - `ImageSaveError`: Image saving failures
  - `ConfigError`: Configuration issues
- **Purpose**: Provide specific, meaningful error types

### `run.py` - Entry Point
- **Purpose**: Application launcher
- **Responsibility**: Window initialization and geometry setup
- **Pattern**: Keeps package clean by handling startup logic externally

## Data Flow

```
User Action (drag/drop/click)
    ↓
Event Handler (on_drop, browse_file)
    ↓
load_image() - Load and validate image
    ↓
Update UI (preview, enable buttons)
    ↓
User selects format/quality
    ↓
update_file_size_preview() - Calculate size
    ↓
User clicks Convert & Save
    ↓
convert_and_save() - Convert and save
    ↓
Success or Error Dialog
```

## State Management

### Instance Variables
- `source_image`: PIL Image object (current loaded image)
- `source_filename`: Original filename without extension
- `source_path`: Full path to source file
- `quality_var`: Tkinter IntVar for quality setting
- `format_var`: Tkinter StringVar for selected format
- `file_size_var`: Tkinter StringVar for size preview
- `config`: Dictionary with window geometry and settings

### Configuration Persistence
- Location determined by `appdirs` (platform-specific)
- Saved on window close
- Loaded on startup
- Contains window size and position

## UI Architecture

### Layout Manager: Grid
- **Why Grid**: Provides proportional scaling for resizable window
- **Structure**: Hierarchical grid with weight configurations
- **Scaling**: All components scale proportionally with window

### Component Hierarchy
```
Root Window
└── Main Frame (row 0, weight=1)
    ├── Header Frame (row 0, weight=0)
    │   ├── Title Label
    │   └── Subtitle Label
    ├── Drop Area Card (row 1, weight=1) ← Gets most space
    │   └── Image Preview Label
    ├── Format Selection Card (row 2, weight=0)
    ├── Quality Control Card (row 3, weight=0)
    ├── File Size Preview Card (row 4, weight=0)
    └── Convert Button (row 5, weight=0)
```

## Error Handling Strategy

1. **User-Facing Errors**: Use `messagebox.showerror()` with friendly messages
2. **Internal Errors**: Raise custom exceptions with detailed information
3. **Silent Failures**: Config save/load failures are ignored (use defaults)
4. **Validation**: Input validation before processing

## Extension Points

### Adding New Formats
1. Add format to `FORMATS` in `constants.py`
2. Update file type filters in dialogs if needed
3. Add quality control support if format supports it

### Adding New Features
1. Add UI in `ui/mixins.py`
2. Add logic in `main.py`
3. Add constants in `constants.py`
4. Add custom exceptions if needed

### Styling Changes
1. Update `COLORS` in `constants.py`
2. All UI components use these colors

## Dependencies

- **Pillow**: Image processing and format conversion
- **tkinterdnd2**: Drag and drop functionality
- **appdirs**: Platform-independent config directory location

## Performance Considerations

1. **Image Preview**: Thumbnails are created to avoid memory issues
2. **File Size Calculation**: Done in memory buffer, not saved to disk
3. **UI Updates**: Only when necessary (format change, quality change)

## Testing Strategy

### Manual Testing Checklist
- [ ] Load images via drag & drop
- [ ] Load images via file browser
- [ ] Convert to each supported format
- [ ] Adjust quality for JPEG/WEBP
- [ ] Resize window and verify layout
- [ ] Close and reopen (verify position saved)
- [ ] Test error cases (invalid files, permission errors)

### Future Automated Testing
- Unit tests for image conversion logic
- Integration tests for UI interactions
- Test fixtures for different image types

## Build Process

1. **Development**: Run with `python run.py`
2. **Distribution**: Build with PyInstaller using `.spec` file
3. **Output**: Standalone executable in `dist/` folder

## Future Improvements

1. **Batch Processing**: Convert multiple files at once
2. **Image Editing**: Basic crop, resize, rotate
3. **Presets**: Save favorite conversion settings
4. **History**: Track recently converted files
5. **Automated Tests**: Unit and integration tests
6. **Logging**: Detailed logging for debugging
7. **Progress Bar**: For large file conversions
8. **Compression Options**: More control over compression algorithms

