# ZipMergeUtility

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
Suppose you have a large file named `project_files.zip` stored on Google Drive, and it contains the following directory structure:

```
project_files.zip
├── documents/
│   ├── report.docx
│   ├── presentation.pptx
│   └── notes.txt
├── code/
│   ├── main.py
│   ├── utils.py
│   └── tests/
│       ├── test_main.py
│       └── test_utils.py
└── resources/
    ├── images/
    │   ├── logo.png
    │   └── background.jpg
    └── data/
        ├── dataset.csv
        └── config.json
```

When you download this file from Google Drive, it might be compressed into multiple zip files due to its size. Let's say it's split into three zip files:

`project_files_part1.zip`, `project_files_part2.zip`, and `project_files_part3.zip` which each file will contain the same directories but the other half of files.

After running the script to merge these zip files, the main working directory will contain:

```
main_directory/
├── documents/
│   ├── report.docx
│   ├── presentation.pptx
│   └── notes.txt
├── code/
│   ├── main.py
│   ├── utils.py
│   └── tests/
│       ├── test_main.py
│       └── test_utils.py
└── resources/
    ├── images/
    │   ├── logo.png
    │   └── background.jpg
    └── data/
        ├── dataset.csv
        └── config.json
```


## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
This script was developed with inspiration from various file management utilities.
