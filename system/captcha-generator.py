# from captcha.image import ImageCaptcha
# from PIL import Image
#
# def generate_captcha(length=6):
#     import string
#     import random
#     return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
#
# def generate_image(image_width=300, image_height=100, captcha_length=6, save_path='captcha_img.png'):
#     image = ImageCaptcha(width=image_width, height=image_height)
#     captcha_text = generate_captcha(captcha_length)
#     data = image.generate(captcha_text)
#     image.write(captcha_text, save_path)
#     return captcha_text
#
# if __name__ == "__main__":
#     captcha_text = generate_image()
#     print("Captcha text: ", captcha_text)
#
# Image.open('captcha_img.png')

from captcha.image import ImageCaptcha
from PIL import Image

def generate_captcha(length=6):
    import string
    import random
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def generate_image(image_width=300, image_height=100, captcha_length=6, save_path='captcha_img.png'):
    image = ImageCaptcha(width=image_width, height=image_height)
    captcha_text = generate_captcha(captcha_length)
    data = image.generate(captcha_text)
    image.write(captcha_text, save_path)
    return captcha_text

if __name__ == "__main__":
    captcha_length = int(input("Enter captcha length: "))
    image_width = int(input("Enter image width: "))
    image_height = int(input("Enter image height: "))
    captcha_text = generate_image(image_width, image_height, captcha_length)
    print("Captcha text:", captcha_text)
    Image.open('captcha_img.png').show()

