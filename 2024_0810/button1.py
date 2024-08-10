import signal
from gpiozero import Button

def user_release():
    print("使用者放開按鈕")

def user_press():
    print("使用者按下按鈕")

def user_held():
    print("使用者按著按鈕")
    

if __name__ == '__main__' :
    button = Button(pin=18)
    button.when_released = user_release
    button.when_pressed = user_press
    button.when_held = user_held

    signal.pause()