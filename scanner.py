import cv2
from pyzbar import pyzbar
import time

scanned_qr_data ={1}

def scan_qr_code():
    # Initialize the webcam
    cap = cv2.VideoCapture(0)
    print("Scanner Onned please Scan")

    while True:
        # Read frames from the webcam
        ret, frame = cap.read()

        # Find and decode QR codes in the frame
        qr_codes = pyzbar.decode(frame)

        # Process each detected QR code
        for qr_code in qr_codes:
            # Extract the data from the QR code
            data = qr_code.data.decode('utf-8')

            # Check if the data is already in the set
            if data in scanned_qr_data:
                print("QR code data is already present in the set.")
            else:
                # Add the data to the set
                scanned_qr_data.add(data)
                print(f"New QR code data scanned: {data}")
            
            print("Data entered ")
            time.sleep(5)
            print("Scanner is ready to scan again")

        # Display the frame
        cv2.imshow('QR Code Scanner', frame)
       
        # Exit if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
    

    # Release the webcam and close windows
    cap.release()
    cv2.destroyAllWindows()

# Example usage
scan_qr_code()
