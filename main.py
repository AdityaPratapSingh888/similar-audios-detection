import os
import librosa # librosa do not work with python 3.11 version so use 3.10 
import numpy as np
from pathlib import Path
from hashlib import sha1
import win32com.client
from tqdm import tqdm

target_sr = 22050

dir_path = input("Enter directory path : ")

audio_hashes = {}

duplicates_dir = os.path.join(dir_path, "duplicates")
if not os.path.exists(duplicates_dir):
    os.makedirs(duplicates_dir)

for audio_filename in tqdm(list(Path(dir_path).rglob('*'))):
    if audio_filename.suffix.lower() in ('.mp3', '.wav', '.flac', '.m4a'):
        try:
            audio, sr = librosa.load(audio_filename, sr=None)
            audio_resampled, _ = librosa.load(audio_filename, sr=target_sr)
            rms = np.sqrt(np.mean(audio_resampled ** 2))
            audio_hash = sha1(audio.tobytes()).hexdigest()

            if audio_hash in audio_hashes:
                duplicate_file_path = os.path.join(duplicates_dir, audio_filename.name)
                os.rename(audio_filename, duplicate_file_path)
                print(f"Duplicate audio file found and moved: {audio_filename} -> {duplicate_file_path}")

                file_path = audio_hashes[audio_hash]
                path=str(audio_filename)
                new_path = f"{path[:-3]}lnk"
                shell = win32com.client.Dispatch("WScript.Shell")
                shortcut = shell.CreateShortCut(new_path)
                shortcut.Targetpath = file_path
                shortcut.save()

            else:
                audio_hashes[audio_hash] = str(audio_filename)
                print(f"Audio file processed: {audio_filename}")
        except Exception as e:
                print(f"Error processing audio file {audio_filename}: {str(e)}")

