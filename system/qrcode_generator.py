# install necessary libraries
import qrcode
# accepting parameter text
def create_qr(text):
    qr = qrcode.QRCode(
        # format of the qr code, can be modified...
        version=2,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=8,
        border=2,
    )
    qr.add_data(text)
    qr.make(fit=True)
    # default color
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("generatedqr_code.png")

link = input("Enter your link: ")
create_qr(link)