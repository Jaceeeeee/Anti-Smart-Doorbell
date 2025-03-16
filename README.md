# Anti-Smart-Doorbell
A reverse doorbell - That instead of alarming the person inside the house that someone rang it, it alarms the one who rang the doorbell!
## Features
  -💡 Flashing LED's (to trigger epilepsy) 
  -🥸 Decoy Button (for maximum security) 
  -☢️ Fake Nuclear Symbol (to stay away from the house) 
  -🟢 Coloured Stickers (to camouflage) 
  -📡 Antenna (shows expertism) 

# Hardware
 

## How it works

An Arduino is hooked up to a simple push button, and when you press that button, the Arduino prints the message “Doorbell Pressed” over its serial output.

On your Mac, a Python script constantly monitors the serial port for that exact message. The moment it sees “Doorbell Pressed,” it calls an AppleScript command that tells the Mac’s Messages app to send an iMessage to a preset recipient (your iPhone)

Over on the iPhone side, a custom Shortcut automation is set up to trigger as soon as it receives a new message from the Mac. That Shortcut then plays random audio files from the phone’s library while popping up a picture from the gallery.
