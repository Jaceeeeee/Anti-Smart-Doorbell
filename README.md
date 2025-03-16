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

1. ![IMG_1960](https://github.com/user-attachments/assets/0d57920f-baa3-4efa-af7f-03000f991b5a)
2. ![IMG_1961](https://github.com/user-attachments/assets/e658dd0a-2bce-4dcd-93f9-f97134f9c647)
3. ![IMG_1962](https://github.com/user-attachments/assets/d5cb35f2-4b42-494e-a0fa-77516211670e)
4. ![IMG_1963](https://github.com/user-attachments/assets/c540af31-db81-4a8f-b810-a9fe5c5bfcc2)
5. ![IMG_1964](https://github.com/user-attachments/assets/81461890-735c-4dd2-bc57-d92d4774a853)
6. ![IMG_1965](https://github.com/user-attachments/assets/1ecba9eb-2125-4eac-a4b8-298cdc3b0d2d)
7. ![IMG_1966](https://github.com/user-attachments/assets/9e1f974a-5955-4892-804b-d0ad22c0403b)

