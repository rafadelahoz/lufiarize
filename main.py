import sys, os
# import imageio.v3 as iio
import imageio as iio
from PIL import Image
import PIL.ImageOps 

if (len(sys.argv) > 0):
    filename = sys.argv[1]
else:
    filename = "enemy.png"
print("Input " + filename)

pimg = Image.open(filename)
# Prepare inverse
iimg = PIL.ImageOps.invert(pimg)
iimg.save(".inverse.png")
iimg = None
# Prepare flip
fimg = PIL.ImageOps.mirror(pimg)
fimg.save(".flip.png")
fimg = None

# Write the gif
img = iio.imread(filename)
iimg = iio.imread(".inverse.png")
fimg = iio.imread(".flip.png")
os.remove(".inverse.png")
os.remove(".flip.png")

iio.mimwrite("output.gif", [img, iimg, img, iimg, img, img, img, img, fimg, fimg, img, img, fimg, fimg, img, img], format='.gif', fps=240)

