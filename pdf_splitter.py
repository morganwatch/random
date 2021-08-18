## Written by Morgan Waters
## Date: 8/18/21
## Image Splitter
## Convert pdf to png.
## run the process.
## Merge the files in the file folder and export as a pdf.

from PIL import Image
import os
import glob
import numpy as np

name = input("What is the name of your file? ")
print("Hello, %s." % name)
name2 = (""" + name + """)

def crop(im, height, width):
    # im = Image.open(infile)
    imgwidth, imgheight = im.size
    rows = np.int64(imgheight/height)
    cols = np.int64(imgwidth/width)
    for i in range(rows):
        for j in range(cols):
            # print (i,j)
            box = (j*width, i*height, (j+1)*width, (i+1)*height)
            yield im.crop(box)


if __name__ == '__main__':
    # change the path and the base name of the image files
    imgdir = '.'
    basename = name
    filelist = glob.glob(os.path.join(imgdir, basename))
    for filenum, infile in enumerate(filelist):
        infile=name
        print(f'file no = {filenum}')  # keep the numbers for the future
        print(f'name is {infile}')
        im = Image.open(infile)
        imgwidth, imgheight = im.size
        print(('Image size is: %d x %d ' % (imgwidth, imgheight)))
        # If you need to change the size change the number at the end depending on how many pieces you want it in.
        height = np.int64(imgheight/3)
        width = np.int64(imgwidth)
        start_num = 0
        for k, piece in enumerate(crop(im, height, width)):
            # print k
            # print piece
            #img = Image.new('L', (width,height), 255) with
            img=Image.new('RGB', (width,height), 255)
            # print img
            assert isinstance(img.paste, object)
            img.paste(piece)
            path = os.path.join("%d-%d.png" % (int(k+1),filenum))
            img.save(path)
            os.rename(path, os.path.join("%d-%d.png" % (int(k+1), filenum)))
