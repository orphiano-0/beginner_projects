import qrcode
import uuid

def create_qr(text, filename):
    qr = qrcode.QRCode(
        version=2,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=8,
        border=2,
    )
    qr.add_data(text)
    qr.make(fit=True)
    # default color
    img = qr.make_image(fill_color="#6aff9b", back_color="black")
    img.save(filename)

link = input("Enter your link: ")
# generate a unique filename using uuid
filename = str(uuid.uuid4()) + ".png"
create_qr(link, filename)
print(f"QR code generated and saved as: {filename}")
