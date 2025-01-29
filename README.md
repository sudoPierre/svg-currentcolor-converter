# SVG CurrentColor Converter for React

This Python script is designed to optimize and modify SVG files for use in React applications. It adjusts SVG attributes to make them compatible with React components and ensures a consistent appearance by using the `currentColor` property. Additionally, the script cleans up file names by removing spaces and capitalizing each word for improved organization.

## Features

- **Dynamic Color Handling**:
  - Replaces all `fill` and `stroke` attributes in SVG files with `currentColor` to allow color inheritance from parent components in React.

- **File Renaming**:
  - Removes spaces in file names and capitalizes each word for a cleaner naming convention.
  - Example: `my icon.svg` becomes `MyIcon.svg`.

- **Batch Processing**:
  - Processes all SVG files in the specified folder.
  - Skips files without changes and logs the result.

## Usage

### Prerequisites

- Python 3.x

### Instructions

1. Clone this repository or download the script file `svg_modifier_for_react.py`.

2. Place the script in the same directory as your SVG files or specify a custom folder path.

3. Run the script:

```bash
python svg_modifier_for_react.py
```

4. The script will process all SVG files in the specified directory, applying the changes and renaming files if needed.

### Customizing the Folder Path

By default, the script processes SVG files in the current directory (`./`). To specify a custom folder path, modify the `file_path` variable in the script:

```python
file_path = '/path/to/your/svg/files'
```

## Example Output

### Input
- File: `example icon.svg`
- Content:
  ```svg
  <svg fill="#000000" stroke="#FF5733">
  </svg>
  ```

### Output
- Renamed File: `ExampleIcon.svg`
- Modified Content:
  ```svg
  <svg fill="currentColor" stroke="currentColor">
  </svg>
  ```

## Logging

The script logs its operations:
- Files modified: `"Changes made to the file: \"ExampleIcon.svg\""`
- Files without changes: `"No changes made to the file: \"ExampleIcon.svg\""`
- Files renamed: `"Renamed: \"example icon.svg\" -> \"ExampleIcon.svg\""`

## Notes

- Ensure your SVG files are backed up before running the script.
- The script is case-insensitive when checking file extensions (e.g., `.SVG` is treated the same as `.svg`).

## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute this script.

---

For questions or contributions, feel free to open an issue or submit a pull request!

