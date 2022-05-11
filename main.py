import sys, os
import imageio as iio
from PIL import Image
import PIL.ImageOps 

if (len(sys.argv) > 1):
    filename = sys.argv[1]
else:
    raise Exception("Please provide an image filename")

pimg = Image.open(filename)
# Prepare inverse
iimg = PIL.ImageOps.invert(pimg)
iimg.save(".inverse.png")
iimg = None
# Prepare flip
fimg = PIL.ImageOps.mirror(pimg)
fimg.save(".flip.png")
fimg = None

# Read the things
img = iio.imread(filename)
iimg = iio.imread(".inverse.png")
fimg = iio.imread(".flip.png")

# Cleanup
os.remove(".inverse.png")
os.remove(".flip.png")

# Write the gif
iio.mimwrite("output.gif", [img, iimg, img, iimg, img, img, img, img, fimg, img, fimg, img, img], format='.gif', fps=240)

