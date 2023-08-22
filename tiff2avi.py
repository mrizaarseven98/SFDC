import cv2
import os
import glob
from PIL import Image
import numpy as np
from tqdm import tqdm

input_folder = "../2023.8.4"

# Collect all TIF files from the specified directory
tif_files = glob.glob(os.path.join(input_folder, "*.tif"))

# Make sure we have some files to convert
if not tif_files:
    print("No TIF files found in the specified directory!")
    exit()

for tif_file in tqdm(tif_files):
    # Open the multipage TIF file with PIL
    tif = Image.open(tif_file)
    
    # Extract all frames/pages from the TIF file
    frames = []
    for i in range(tif.n_frames):
        tif.seek(i)
        frames.append(tif.copy())

    # Check the first frame to determine video dimensions
    frame = frames[0]
    width, height = frame.size
    size = (width, height)

    # Create output filename by replacing the .tif extension with .avi
    output_file = os.path.join(input_folder, os.path.basename(tif_file).replace('.tif', '.avi'))

    # Create an AVI video writer with XVID codec
    out = cv2.VideoWriter(output_file, cv2.VideoWriter_fourcc(*'XVID'), 1, size)

    # Convert each frame in the TIF to the AVI video
    for frame in frames:
        frame_cv2 = cv2.cvtColor(np.array(frame), cv2.COLOR_RGB2BGR)
        out.write(frame_cv2)

    out.release()

    print(f"Saved {tif_file} as {output_file}")

print("Conversion completed!")
