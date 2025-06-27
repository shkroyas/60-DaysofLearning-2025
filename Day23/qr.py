import qrcode
from PIL import Image
qr=qrcode.QRCode(version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10,
                border=4,)
qr.add_data("https://docs.google.com/forms/d/e/1FAIpQLSfXxdP4wT5oAkiO3zzQcKY1wrlkEnkieG-IbXG3F4-me81ByQ/viewform")
qr.make(fit=True)
img=qr.make_image(fill_color="orange", back_color="white")
img.save("LSPP.png")