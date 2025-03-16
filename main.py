#  _____________________
# < Works on MacOS only! >
#  ---------------------
#         \   ^__^
#          \  (oo)\_______
#             (__)\       )\/\
#                 ||----w |
#                 ||     ||

import serial
import subprocess

baud = "9600"

# too lazy to do cowsay here

# To get the port, run the following command in terminal:
# ls /dev/tty.usbmodem*
# Look for a port that starts with /dev/tty.usbmodem
# Example: /dev/tty.usbmodem214101

port = "/dev/tty.usbmodem214101"

#  ________________________________________
# / Replace with recipient's phone number  \
# | with country code.                     |
# |                                        |
# | Make sure iMessage is enabled on the   |
# | mac running this python code           |
# |                                        |
# | And the recipient's phone              |
# | number is associated with iMessage.    | 
# |                                        |
# | If it still doesn't work, try adding   |
# | the recipient to your contacts (with   |
# | country code) and manually start a     |
# | conversation with them in the Messages |
# \ app.                                   /
#  ----------------------------------------
#         \   ^__^
#          \  (oo)\_______
#             (__)\       )\/\
#                 ||----w |
#                 ||     ||

phone_number = "+66xxxxx8046"

def main():
    with serial.Serial(port, baud, timeout=1) as ser:
        print("Listening on serial port", port)
        
        while True:
            line = ser.readline().decode('utf-8', errors='ignore').strip()
            if line:
                print("Received from Arduino:", line)
                
                if "Doorbell Pressed" in line:
                    send_imessage()

def send_imessage():
    # print("Sent")
    script = f'''
    tell application "Messages"
        send "Doorbell Pressed" to buddy "{phone_number}" of (first service whose service type = iMessage)
    end tell
    '''
  
    subprocess.run(["osascript", "-e", script])

if __name__ == "__main__":
    main()