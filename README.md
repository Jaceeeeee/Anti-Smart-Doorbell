# Anti-Smart-Doorbell

A reverse doorbell - That instead of alarming the person inside the house that someone rang it, it alarms the one who rang the doorbell!

## Features

-💡 Flashing LED's (to trigger epilepsy)

-🥸 Decoy Button (for maximum security)

-☢️ Fake Nuclear Symbol (to stay away from the house)

-🟢 Coloured Stickers (to camouflage especially from colorblind thieves)

-📡 Antenna (shows expertism)

## Hardware

- Arduino Leonardo
- Button
- Jumper Wires
- LEDs
- Resistors
- Breadboard

## How to run

1. Upload `main.ino` to the Arduino
2. Connect the Arduino to the computer, make sure to close the arduino ide after uploading the code to make sure the serial port is free for the python to monitor
3. Install prerequisites for the python script

```sh
pip install requirements.txt
```

4. Run the python script

```sh
python main.py
```

5. Scroll down to the shortcuts automation section

Other more instructions r in the `main.py` file

## How it works

An Arduino is hooked up to a simple push button, and when you press that button, the Arduino prints the message “Doorbell Pressed” over its serial output.

On your Mac, a Python script constantly monitors the serial port for that exact message. The moment it sees “Doorbell Pressed,” it calls an AppleScript command that tells the Mac’s Messages app to send an iMessage to a preset recipient (your iPhone)

Over on the iPhone side, a custom Shortcut automation is set up to trigger as soon as it receives a new message from the Mac. That Shortcut then plays random audio files from the phone’s library while popping up a picture from the gallery.

# The shortcuts automation

[Visit this](https://github.com/Jaceeeeee/Anti-Smart-Doorbell/blob/main/automation/setup.md)
