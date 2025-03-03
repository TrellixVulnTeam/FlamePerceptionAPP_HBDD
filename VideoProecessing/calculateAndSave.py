from PIL import Image
import numpy as np
import glob
import sys
from pathlib import Path

# https://stackoverflow.com/questions/57562178/calculate-the-ratio-of-area-of-different-colors-in-an-image
# https://stackoverflow.com/questions/3345336/save-results-to-csv-file-with-python

sys.stdout = open("data.txt", "w")
# print(f" frame, Area, Percentage  ")

def processLog(filename):
    # print(f"Processing log: {filename}")
    p=Path(f"{filename}")
    # print(f"{p.stem}")
    # Open this image and make a Numpy version for easy processing
    im   = Image.open(filename).convert('RGBA').convert('RGB')
    imnp = np.array(im)
    h, w = imnp.shape[:2]

    # Get list of unique colours...
    # Arrange all pixels into a tall column of 3 RGB values and find unique rows (colours)
    colours, counts = np.unique(imnp.reshape(-1,3), axis=0, return_counts=1)
    # Get area and portion of black color
    SumCount=0
    SumProportion=0

    # Iterate through unique colours
    for index, colour in enumerate(colours):
        count = counts[index]
        proportion = (100 * count) / (h * w)
        # print(f"   Colour: {colour}, count: {count}, proportion: {proportion:.2f}%")
        if index<=20:
          SumCount=SumCount+count
          SumProportion=SumProportion+proportion
    # print(f"   sumcount: {SumCount}")
    # print(f"   SumProportion: {SumProportion}")
    print(f" {p.stem}, {SumCount}, {SumProportion}  ")

# Iterate over all images called "log*png" in current directory
for filename in glob.glob("/Users/wangmeijie/ALLImportantProjects/FlameDetectionAPP/WebApplication/static/img/Area/*.jpg"):
    processLog(filename)

sys.stdout.close()