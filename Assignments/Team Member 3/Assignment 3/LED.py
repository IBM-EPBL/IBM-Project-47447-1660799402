from gpiozero import Button, LED
led=LED[25]
while True:
    button.wait_for_press()
    led.on()
    button.wait_for_release()
    led.off()
