import signal
from gpiozero import Button,LED
from datetime import datetime

def user_release():
    print("使用者按了按鈕")
    #led.off()
    led.toggle()
    now = datetime.now()
    now_str = now.strftime('%Y-%m-%d %H:%M:%S')
    print(now_str)
    if led.is_lit:
        print("燈是開的")
    else:
        print("燈是關的")

#def user_press():
#   print("使用者按下按鈕")
    #led.on()

#def user_held():
#    print("使用者按著按鈕")



if __name__ == '__main__' :
    button = Button(pin=18) #GPIO的pin代號  不是實體pin
    button.when_released = user_release
#    button.when_pressed = user_press
#    button.when_held = user_held
    led = LED(pin=25)

    signal.pause()