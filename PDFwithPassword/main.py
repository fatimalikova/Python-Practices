# pip install pypdf

from pypdf import PdfReader, PdfWriter
reader = PdfReader("PEBBLE.pdf")
writer = PdfWriter()

writer.append(reader)
writer.encrypt("kaist")

with open("protected.pdf", "wb") as file : writer.write(file)