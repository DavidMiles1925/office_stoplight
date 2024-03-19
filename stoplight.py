import RPi.GPIO as GPIO
from time import sleep

INDICATOR_LED_PIN = 17

RED1_LED_PIN = 5
RED2_LED_PIN = 11
YELLOW1_LED_PIN = 6
YELLOW2_LED_PIN = 13
GREEN1_LED_PIN = 26
GREEN2_LED_PIN = 19

BLUE_BUTTON_PIN = 12
RED_BUTTON_PIN = 23
YELLOW_BUTTON_PIN = 24
GREEN_BUTTON_PIN = 25

LED_PIN_ARRAY = [INDICATOR_LED_PIN, RED1_LED_PIN, RED2_LED_PIN, YELLOW1_LED_PIN, YELLOW2_LED_PIN, GREEN1_LED_PIN, GREEN2_LED_PIN]
BUTTON_PIN_ARRAY = [BLUE_BUTTON_PIN, RED_BUTTON_PIN, YELLOW_BUTTON_PIN, GREEN_BUTTON_PIN]

def setup_pins():
    # Board Mode: BCM
    GPIO.setmode(GPIO.BCM)

    # Disable Warnings
    GPIO.setwarnings(False)

    for x in range(len(LED_PIN_ARRAY)):
        GPIO.setup(LED_PIN_ARRAY[x], GPIO.OUT)
        GPIO.output(LED_PIN_ARRAY[x], GPIO.LOW)
    # LEDs
    # GPIO.setup(INDICATOR_LED_PIN, GPIO.OUT)
    # GPIO.output(INDICATOR_LED_PIN, GPIO.LOW)

    # GPIO.setup(RED_LED_PIN, GPIO.OUT)
    # GPIO.output(RED_LED_PIN, GPIO.LOW)

    # GPIO.setup(YELLOW_LED_PIN, GPIO.OUT)
    # GPIO.output(YELLOW_LED_PIN, GPIO.LOW)

    # GPIO.setup(GREEN1_LED_PIN, GPIO.OUT)
    # GPIO.output(GREEN1_LED_PIN, GPIO.LOW)

    # GPIO.setup(GREEN2_LED_PIN, GPIO.OUT)
    # GPIO.output(GREEN2_LED_PIN, GPIO.LOW)

    for x in range(len(BUTTON_PIN_ARRAY)):
        GPIO.setup(BUTTON_PIN_ARRAY[x], GPIO.OUT)
    # Buttons
    # GPIO.setup(BLUE_BUTTON_PIN, GPIO.IN)
    # GPIO.setup(RED_BUTTON_PIN, GPIO.IN)
    # GPIO.setup(YELLOW_BUTTON_PIN, GPIO.IN)
    # GPIO.setup(GREEN_BUTTON_PIN, GPIO.IN)


def all_leds(status):

    if status == "on" or status == "ON":
        for x in range(len(LED_PIN_ARRAY)):
            GPIO.output(LED_PIN_ARRAY[x], GPIO.HIGH)
        # GPIO.output(RED_LED_PIN, GPIO.HIGH)
        # GPIO.output(YELLOW_LED_PIN, GPIO.HIGH)
        # GPIO.output(GREEN1_LED_PIN, GPIO.HIGH)
        # GPIO.output(GREEN2_LED_PIN, GPIO.HIGH)

    else:
        for x in range(len(LED_PIN_ARRAY)):
            GPIO.output(LED_PIN_ARRAY[x], GPIO.LOW)
        # GPIO.output(RED_LED_PIN, GPIO.LOW)
        # GPIO.output(YELLOW_LED_PIN, GPIO.LOW)
        # GPIO.output(GREEN1_LED_PIN, GPIO.LOW)
        # GPIO.output(GREEN2_LED_PIN, GPIO.LOW)

def led_on(pin):
    all_leds("off")

    GPIO.output(INDICATOR_LED_PIN, GPIO.HIGH)
    GPIO.output(pin, GPIO.HIGH)

def green_on():
    all_leds("off")
    GPIO.output(GREEN1_LED_PIN, GPIO.HIGH)
    GPIO.output(GREEN2_LED_PIN, GPIO.HIGH)

def light_show():
    print("Light show!")

    # lightshow_on = True
    lightshow_on = 0
    loop_sleep_time = 0.1

    all_leds("on")
    sleep(0.5)
    all_leds("off")

    while lightshow_on < 7:

        led_on(RED1_LED_PIN)
        led_on(RED2_LED_PIN)
        sleep(loop_sleep_time)

        led_on(YELLOW1_LED_PIN)
        led_on(YELLOW2_LED_PIN)
        sleep(loop_sleep_time)

        green_on()
        sleep(loop_sleep_time)

        # if GPIO.input(GREEN_BUTTON_PIN) == False and GPIO.input(YELLOW_BUTTON_PIN) == False:
        #     lightshow_on = False
        #     sleep(0.5)

        lightshow_on = lightshow_on + 1

    led_on(RED1_LED_PIN)
    led_on(RED2_LED_PIN)
    

def check_buttons():
    if GPIO.input(RED_BUTTON_PIN) == False and GPIO.input(YELLOW_BUTTON_PIN) == False:
        light_show()


    if GPIO.input(BLUE_BUTTON_PIN) == False and GPIO.input(RED_BUTTON_PIN) == False:
        print("DONE")
        GPIO.cleanup()
        exit()

        
    if GPIO.input(BLUE_BUTTON_PIN) == False:
        all_leds("off")
        print("OFF")
        sleep(0.2)

    elif GPIO.input(RED_BUTTON_PIN) == False:
        print("RED")
        led_on(RED1_LED_PIN)
        led_on(RED2_LED_PIN)
        sleep(0.2)

    elif GPIO.input(YELLOW_BUTTON_PIN) == False:
        print("YELLOW")
        led_on(YELLOW1_LED_PIN)
        led_on(YELLOW2_LED_PIN)
        sleep(0.2)

    elif GPIO.input(GREEN_BUTTON_PIN) == False:
        print(f"GREEN")
        green_on()
        sleep(0.2)


if __name__ == "__main__":
    setup_pins()

    GPIO.output(INDICATOR_LED_PIN, GPIO.HIGH)

    light_show()

    try:
        while True:
            check_buttons()

    except KeyboardInterrupt:
        print("DONE")
        GPIO.cleanup()
        exit()


        


