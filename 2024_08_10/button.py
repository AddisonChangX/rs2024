from gpiozero import Button
import signal

button = Button(pin=18)

while True:
    if button.is_pressed:
        print("Button is pressed")
        signal.pause()
    else:
        print("Button is not pressed")