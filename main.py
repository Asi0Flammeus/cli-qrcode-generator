import pyqrcode
import sys
import subprocess

def generate_qr_code(data):
    # Generate the QR code
    qr = pyqrcode.create(data)
    qr.png('temp_qr.png', scale=4)  # Adjust scale to desired image size

    # Open the QR code using an external viewer
    subprocess.run(['eog', 'temp_qr.png'])

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Take input from command line argument
        input_data = ' '.join(sys.argv[1:])
    else:
        # Or ask the user to enter the data
        input_data = input("Enter the text for the QR code: ")

    generate_qr_code(input_data)

