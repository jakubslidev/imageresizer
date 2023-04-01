import os
from PIL import Image

# set input and output directories
input_dir = ''
output_dir = ''

# set desired width and height for resized images
width = 2240
height = 3360

# create output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# iterate over all subdirectories in input directory
for dirpath, dirnames, filenames in os.walk(input_dir):
    # create corresponding subdirectory in output directory
    relpath = os.path.relpath(dirpath, input_dir)
    outpath = os.path.join(output_dir, relpath)
    if not os.path.exists(outpath):
        os.makedirs(outpath)
    # iterate over all image files in subdirectory
    for filename in filenames:
        if filename.lower().endswith('.jpg') or filename.lower().endswith('.jpeg') or filename.lower().endswith('.png'):
            # open image file
            filepath = os.path.join(dirpath, filename)
            with Image.open(filepath) as img:
                # resize image to desired dimensions
                img = img.resize((width, height))
                # save resized image to output directory
                outpath = os.path.join(output_dir, relpath, filename)
                img.save(outpath)