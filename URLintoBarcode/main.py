#pip install python barcode pillow
import barcode
from barcode.writer import ImageWriter

data = input("Enter code, text or url: ")

barcode.get("code128", data, writer=ImageWriter()).save("barcode")

print("Barcode created!")