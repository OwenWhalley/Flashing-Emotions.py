from microbit import  *

while True:
    if button_a.is_pressed():
        for x in range(4):
            display.show(Image.HAPPY)
            sleep(400)
            display.clear()
            sleep(400)
    if button_b.is_pressed ():
        for x in range(4):
            display.show(Image.SAD)
            sleep(400)
            display.clear()
            sleep(400)
      