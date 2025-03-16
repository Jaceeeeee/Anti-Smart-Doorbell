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
2. Install prerequisites for the python script
3. Run the python script

## How it works

An Arduino is hooked up to a simple push button, and when you press that button, the Arduino prints the message “Doorbell Pressed” over its serial output.

On your Mac, a Python script constantly monitors the serial port for that exact message. The moment it sees “Doorbell Pressed,” it calls an AppleScript command that tells the Mac’s Messages app to send an iMessage to a preset recipient (your iPhone)

Over on the iPhone side, a custom Shortcut automation is set up to trigger as soon as it receives a new message from the Mac. That Shortcut then plays random audio files from the phone’s library while popping up a picture from the gallery.

# Shorcuts Automation

It’s pretty simple, and because iOS doesn’t allow automation sharing, we’re a bit too lazy to convert it into a shareable Shortcut. Therefore, we won’t be providing a link to it.

Here are the images of the autoamtion:

1. ![IMG_1960](https://github.com/user-attachments/assets/dc16123a-71e0-45bb-b3ea-c699d8f340d3)
2. ![IMG_1961](https://github.com/user-attachments/assets/73065162-7d9a-4b36-93b3-9b0f9a12e4e5)
3. ![IMG_1962](https://github.com/user-attachments/assets/1868b342-4561-4d38-9348-7c8b4ca97c4c)
4. ![IMG_1963](https://github.com/user-attachments/assets/765281b6-0bbc-4b85-9582-4dfca6d8908d)
5. ![IMG_1964](https://github.com/user-attachments/assets/f85c8c18-775e-4133-9307-d10afd437915)
6. ![IMG_1965](https://github.com/user-attachments/assets/aafc2c7e-93cf-40bf-b4bf-d84e877aeb48)
7. ![IMG_1966](https://github.com/user-attachments/assets/d73e232c-5c95-4812-a876-2cc704a38b59)



