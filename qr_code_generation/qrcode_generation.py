import qrcode
from qrcode.main import QRCode

class QRCodeGenerator:
    def __init__(self, box_size: int, border: int, fill_color: str, back_color: str, version=1):
        """
        Constructor to initialize QR code properties

        Args:
            box_size (int): The size of each box in the QR code.
            border (int): The border size of the QR code.
            fill_color (str): The fill color of the QR code.
            back_color (str): The background color of the QR code.
            version (int): The version of the QR code.
        """
        self.box_size = box_size
        self.border = border
        self.fill_color = fill_color
        self.back_color = back_color
        self.version = version

    def generate_qr_code(self, data_to_encode: str, img_file_path: str):
        """
        Generates a QR code and saves it to a file

        Args:
            data_to_encode (str): The data to encode in the QR code.
            img_file_path (str): The path where the QR code image will be saved.
        """
        try:
            qr = QRCode(
                    version=self.version,
                    error_correction=qrcode.constants.ERROR_CORRECT_H,
                    box_size=self.box_size,
                    border=self.border)

            qr.add_data(data_to_encode)
            qr.make(fit=True)

            img = qr.make_image(fill_color=self.fill_color, back_color=self.back_color)
            img.save(img_file_path)
            print(f"QR Code saved to {img_file_path}")
        except Exception as e:
            print(f"Error occured while generating QR code: {e}")

def main():
    import os
    from pathlib import Path

    gmap_location = "https://maps.app.goo.gl/grvxa2hixrhiC56w7"     # The data to encode in the QR code
    img_save_location = os.path.join(Path(__file__).parent.resolve(), "wedding_location_qr_code.png")    # ".\\qr_code_generation\\wedding_location_qr_code.png"
    QRCodeGenerator(box_size=10, border=4, fill_color="black", back_color="white").generate_qr_code(data_to_encode=gmap_location, img_file_path=img_save_location)

if __name__ == "__main__":
    main()
