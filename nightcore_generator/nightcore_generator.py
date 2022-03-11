from genericpath import isfile
import os
import subprocess

current_path = os.path.dirname(__file__)

# FFmpeg
FFMPEG_PATH = "PLACE YOUR FFMPEG PATH HERE"
if not isfile(FFMPEG_PATH):
    print("FFmpeg path is not valid")
    exit()

# Get music file path
while True:
    music_path = input("Music file path: ").replace('"', "").replace("'", "").strip()
    if not isfile(music_path):
        input("Music file path is not valid, press any key to continue...")
        continue
    break

# Get output music path
output_path = input("Output path:").replace('"', "").replace("'", "").strip()

command = [
    FFMPEG_PATH,
    "-y",  # Always overwrite
    "-i",
    music_path,
    "-filter:a",
    "asetrate=44100*1.265,aresample=44100",  # Increase sample rate and resample at original rate
    output_path,
]

print("Please wait...")
command_output = subprocess.run(command, stderr=subprocess.PIPE)
print("Music has been converted successfully!")
print(f"Path: {output_path}")
