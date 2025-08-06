import qrcode

# Data to be encoded
data = "https://example.com"  # Change this to any text or URL

# Create QR code instance
qr = qrcode.QRCode(
    version=1,  # controls size of the QR code
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # high error correction
    box_size=10,  # size of each box in pixels
    border=4,  # thickness of the border
)

# Add data to the QR code
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill_color="black", back_color="white")

# Save the image
img.save("qr_code.png")

print("QR code generated and saved as 'qr_code.png'")
