import os
import subprocess
import time

totalstart = time.time()

# Define input and output folders (must be changed).
input_folder = 'INPUT FOLDER PATH'
output_folder = 'OUTPUT FOLDER PATH'

# Create output folder if it does not exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)


# Scan all files in the input folder.
for file in os.listdir(input_folder):
    start = time.time()
    if file.endswith('.dav'):
        input_file = os.path.join(input_folder, file)
        output_file = os.path.join(output_folder, file.replace('.dav', '.mp4'))

        # Convert files using the ffmpeg command
        print(f"{file} is currently under conversion")
        command = ['ffmpeg', '-i', input_file, output_file]
        subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    end = time.time()
    print(f"{file} - FINISH CONVERSION")
    print(f"TIME : {(end - start)/60}","\n")

totalend = time.time()
print("-----FULL CONVERT from DAV to MP4-----")
print(f"TOTAL TIME : {(totalend - totalstart)/60}")


