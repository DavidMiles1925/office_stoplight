import RPi.GPIO as GPIO
from time import sleep

INDICATOR_LED_PIN = 12

RED_LED_PIN = 5
YELLOW_LED_PIN = 6
GREEN1_LED_PIN = 13
GREEN2_LED_PIN = 19
GREEN3_LED_PIN = 26

BLUE_BUTTON_PIN = 22
RED_BUTTON_PIN = 18
YELLOW_BUTTON_PIN = 23
GREEN_BUTTON_PIN = 24

def setup_pins():
    # Board Mode: BCM
    GPIO.setmode(GPIO.BCM)

    # Disable Warnings
    GPIO.setwarnings(False)

    # LEDs
    GPIO.setup(INDICATOR_LED_PIN, GPIO.OUT)
    GPIO.output(INDICATOR_LED_PIN, GPIO.LOW)

    GPIO.setup(RED_LED_PIN, GPIO.OUT)
    GPIO.output(RED_LED_PIN, GPIO.LOW)

    GPIO.setup(YELLOW_LED_PIN, GPIO.OUT)
    GPIO.output(YELLOW_LED_PIN, GPIO.LOW)

    GPIO.setup(GREEN1_LED_PIN, GPIO.OUT)
    GPIO.output(GREEN1_LED_PIN, GPIO.LOW)

    GPIO.setup(GREEN2_LED_PIN, GPIO.OUT)
    GPIO.output(GREEN2_LED_PIN, GPIO.LOW)

    GPIO.setup(GREEN3_LED_PIN, GPIO.OUT)
    GPIO.output(GREEN3_LED_PIN, GPIO.LOW)

    # Buttons
    GPIO.setup(BLUE_BUTTON_PIN, GPIO.IN)
    GPIO.setup(RED_BUTTON_PIN, GPIO.IN)
    GPIO.setup(YELLOW_BUTTON_PIN, GPIO.IN)
    GPIO.setup(GREEN_BUTTON_PIN, GPIO.IN)


def all_leds(status):

    if status == "on" or status == "ON":
        GPIO.output(RED_LED_PIN, GPIO.HIGH)
        GPIO.output(YELLOW_LED_PIN, GPIO.HIGH)
        GPIO.output(GREEN1_LED_PIN, GPIO.HIGH)
        GPIO.output(GREEN2_LED_PIN, GPIO.HIGH)
        GPIO.output(GREEN3_LED_PIN, GPIO.HIGH)

    else:
        GPIO.output(RED_LED_PIN, GPIO.LOW)
        GPIO.output(YELLOW_LED_PIN, GPIO.LOW)
        GPIO.output(GREEN1_LED_PIN, GPIO.LOW)
        GPIO.output(GREEN2_LED_PIN, GPIO.LOW)
        GPIO.output(GREEN3_LED_PIN, GPIO.LOW)

def led_on(pin):
    all_leds("off")

    GPIO.output(pin, GPIO.HIGH)

def green_on():
    all_leds("off")
    GPIO.output(GREEN1_LED_PIN, GPIO.HIGH)
    GPIO.output(GREEN2_LED_PIN, GPIO.HIGH)
    GPIO.output(GREEN3_LED_PIN, GPIO.HIGH)
    


if __name__ == "__main__":
    setup_pins()

    GPIO.output(INDICATOR_LED_PIN, GPIO.HIGH)

    try:
        while True:

            if GPIO.input(GREEN_BUTTON_PIN) == False and GPIO.input(YELLOW_BUTTON_PIN) == False:
                print("Light show!")

                lightshow_on = True
                loop_sleep_time = 0.1

                all_leds("on")
                sleep(0.5)
                all_leds("off")

                while lightshow_on == True:

                    led_on(RED_LED_PIN)
                    sleep(loop_sleep_time)

                    led_on(YELLOW_LED_PIN)
                    sleep(loop_sleep_time)

                    green_on()
                    sleep(loop_sleep_time)

                    if GPIO.input(GREEN_BUTTON_PIN) == False and GPIO.input(YELLOW_BUTTON_PIN) == False:
                        lightshow_on = False
                        sleep(0.5)



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
                led_on(RED_LED_PIN)
                sleep(0.2)

            elif GPIO.input(YELLOW_BUTTON_PIN) == False:
                print("YELLOW")
                led_on(YELLOW_LED_PIN)
                sleep(0.2)

            elif GPIO.input(GREEN_BUTTON_PIN) == False:
                print(f"GREEN")
                green_on()
                sleep(0.2)


    except KeyboardInterrupt:
        print("DONE")
        GPIO.cleanup()
        exit()


        


