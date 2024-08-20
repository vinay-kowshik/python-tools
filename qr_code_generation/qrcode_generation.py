import qrcode
from qrcode.main import QRCode

gmap_location = "https://maps.app.goo.gl/grvxa2hixrhiC56w7"     # The data to encode in the QR code

qr = QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4)

qr.add_data(gmap_location)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save(".\\wedding_location_qr_code.png")
