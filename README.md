# Duplicate Audio Detection Script

## Introduction

This Python script is designed to identify and move duplicate audio files within a specified directory. It utilizes the `librosa` library for audio processing, calculates the root mean square (RMS) of resampled audio, and generates SHA-1 hashes to identify duplicates. Duplicate audio files are moved to a "duplicates" directory, and shortcuts to the original files are created.

**Note:** The script uses `librosa`, which may not be compatible with Python 3.11. It is recommended to use Python 3.10.

## Usage

1. **Installation of Dependencies:**
    - Ensure you have the necessary dependencies installed. You can install them using the following:
        ```bash
        pip install librosa numpy tqdm pywin32
        ```

2. **Script Configuration:**
    - Update the `dir_path` variable with the path of the directory containing audio files you want to process.

3. **Running the Script:**
    - Execute the script in a Python 3.10 environment:
        ```bash
        python main.py
        ```
    - The script will process audio files, identify duplicates, move them to the "duplicates" directory, and create shortcuts to the original files.

## Notes

- The script supports various audio formats such as MP3, WAV, FLAC, and M4A.
- Duplicate audio files are identified based on SHA-1 hashes calculated from the root mean square of resampled audio.

## Additional Information

- This script uses the `win32com.client` library to create shortcuts in Windows.
- The `tqdm` library provides a progress bar to track the processing of audio files.

## Disclaimer

- Use this script responsibly and ensure you have a backup of your data before running it.
- The script may not handle all edge cases, and it is recommended to review the results in the "duplicates" directory.

Feel free to customize the script based on your specific requirements or contribute to its improvement.
