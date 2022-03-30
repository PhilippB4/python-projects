import qrcode

data = "youtube.com/philippb4"

qr = qrcode.QRCode(version=1,
                   border=0)

qr.add_data(data)
img = qr.make_image(fill_color="blue",
                    back_color="white")
img.save("philippb4QR.png")
