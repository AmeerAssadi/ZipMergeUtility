# Zip Merge Utility

This Python script provides a utility for merging the contents of multiple zip files intelligently. It extracts the contents of each zip file into a temporary directory and then moves or merges the extracted files and directories into a main working directory, handling conflicts and duplicates intelligently.

## Features
- Extracts and merges the contents of multiple zip files into a single directory.
- Handles conflicts and duplicates by renaming files and merging directories intelligently.
- Provides a customizable framework for further enhancements and modifications.

## Usage
1. Place all the zip files you want to merge in the same directory as the script.
2. Run the script, which will create a main working directory and merge the contents of the zip files into it.
3. Check the main working directory for the merged files and directories.

## Requirements
- Python 3.x
- `shutil` and `zipfile` standard libraries
  
## Example
Suppose you have three zip files:
- `file1.zip` containing:
  - `folder1/`
    - `file1_1.txt`
- `file2.zip` containing:
  - `folder1/`
    - `file1_2.txt`
  - `file2.txt`
- `file3.zip` containing:
  - `folder2/`
    - `file3_1.txt`

After running the script, the main working directory will contain:
- `folder1/`
  - `file1_1.txt`
  - `file1_2.txt`
- `folder2/`
  - `file3_1.txt`
- `file2.txt`

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
This script was developed with inspiration from various file management utilities.

