# pip install qrcode[pil]

import qrcode

data = "KAIST"
qr = qrcode.make(data)
qr.save("qrcode.png")

print("QR code created successfully")