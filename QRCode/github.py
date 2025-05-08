import qrcode 

import qrcode.constants

qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_H,
                   box_size=10,border=5,)

qr.add_data("https://github.com/Tejaswinipaunikar")
qr.make(fit=True)

img=qr.make_image(fill_color="purple",back_color="white")

img.save("Tejaswini_GitHub.png")