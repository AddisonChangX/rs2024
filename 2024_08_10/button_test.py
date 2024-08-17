import signal
from gpiozero import Button,LED
from datetime import datetime

def user_release():
    now = datetime.now()
    now_str = now.strftime('%Y-%m-%d %H:%M:%S')
    print(now_str + "使用者放開按鈕")
    led.off()
    #led.toggle()
    print(now_str + "燈是關的")
     

def user_press():
    now = datetime.now()
    now_str = now.strftime('%Y-%m-%d %H:%M:%S')
    print(now_str + "使用者按下按鈕")
    led.on()
    print(now_str + "燈是開的")

def user_held():
    now = datetime.now()
    now_str = now.strftime('%Y-%m-%d %H:%M:%S')
    print(now_str + "使用者按著按鈕")



if __name__ == '__main__' :
    button = Button(pin=18) #GPIO的pin代號  不是實體pin
    button.when_released = user_release
    button.when_pressed = user_press
    button.when_held = user_held
    led = LED(pin=25)

    signal.pause()