import qrcode
data = input("Введимте данные для кодирования:")
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(data)
qr.make(fit=True)
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(data)
qr.make(fit=True)
image = qr.make_image(fill="black", back_color="white")
filename = "qrcode.png"
image.save(filename)
print(f"QR-код сохранен в файле {filename}.")
