# CodeAlpha Task 3 — JPG File Organizer

A small Python desktop utility that organizes `.jpg` and `.jpeg` files from a selected folder into a `JPG_Files` subfolder.

## Features
- Browse and select a folder using a graphical interface.
- Find JPG/JPEG files directly inside the selected folder.
- Create `JPG_Files` automatically and move matching files into it.
- Avoid overwriting files by generating a numbered filename when a duplicate exists.
- Show progress and errors in an activity log.
- Reset the activity log.

## Requirements
- Python 3.9 or later
- Tkinter (usually included with standard Python installations)

No third-party Python packages are required.

## Run
1. Install Python if it is not already installed.
2. Download or clone this repository.
3. Open a terminal in this folder.
4. Run:

```bash
python file_organizer.py
```

On some systems, use `python3 file_organizer.py` instead.

## How to use
1. Click **Browse** and choose a folder.
2. Click **Organize JPG Files**.
3. The app moves `.jpg` and `.jpeg` files from the selected folder into `JPG_Files`.
4. Review the activity log for the result.

**Important:** This tool moves files rather than copying them. Test it with sample files first and keep backups of important images. It processes files directly in the selected folder, not recursively through nested subfolders.

## Project structure

```text
CodeAlpha_Task3_JPG_Automator/
├── file_organizer.py
├── README.md
├── requirements.txt
├── .gitignore
└── sample_images/
```

## Internship project
Created as a Python programming task for the CodeAlpha internship. Update this section with your own completion details and screenshots before submission.
