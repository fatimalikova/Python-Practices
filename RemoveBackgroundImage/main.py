# ilk once terminala  === pip install "rembg[cpu]" pillow ===  yazib press enter

from rembg import remove
from PIL import Image

input = Image.open("mercedes.jpg")
output = remove(input)

output.save("output.png")

# terminala === python main.py === press enter