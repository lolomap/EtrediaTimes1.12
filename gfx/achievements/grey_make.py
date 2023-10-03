from PIL import Image
import sys

img = Image.open(sys.argv[1] + '.png')
blackAndWhite = img.convert("L")
blackAndWhite.save(sys.argv[1] + '_grey.png')
blackAndWhite.save(sys.argv[1] + '_not_eligible.png')