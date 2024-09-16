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

# This functions turns ALL LEDs "ON" or "OFF" depending on the status parameter

def all_leds(status):

    if status == "on" or status == "ON":
        for x in range(len(LED_PIN_ARRAY)):
            GPIO.output(LED_PIN_ARRAY[x], GPIO.HIGH)

    else:
        for x in range(len(LED_PIN_ARRAY)):
            GPIO.output(LED_PIN_ARRAY[x], GPIO.LOW)

    GPIO.output(INDICATOR_LED_PIN, GPIO.HIGH)



def led_on(pin):
    GPIO.output(pin, GPIO.HIGH)


def setup_pins():
    # Board Mode: BCM
    GPIO.setmode(GPIO.BCM)

    # Disable Warnings
    GPIO.setwarnings(False)

    for x in range(len(LED_PIN_ARRAY)):
        GPIO.setup(LED_PIN_ARRAY[x], GPIO.OUT)
        GPIO.output(LED_PIN_ARRAY[x], GPIO.LOW)
        print(f"Pin {LED_PIN_ARRAY[x]} enabled as output")

    for x in range(len(BUTTON_PIN_ARRAY)):
        GPIO.setup(BUTTON_PIN_ARRAY[x], GPIO.IN)
        print(f"Pin {BUTTON_PIN_ARRAY[x]} enabled as input")


def handle_error(e, msg):
    print(msg)
    print(f"Error: {e}")
    GPIO.cleanup()
    exit()


def check_buttons():
    try:
        if GPIO.input(RED_BUTTON_PIN) == False and GPIO.input(YELLOW_BUTTON_PIN) == False:
            light_show()


        if GPIO.input(BLUE_BUTTON_PIN) == False and GPIO.input(RED_BUTTON_PIN) == False:
            print("Blue and Red Buttons Pressed. Program Terminated.")
            print("DONE")
            GPIO.cleanup()
            exit()

            
        if GPIO.input(BLUE_BUTTON_PIN) == False:
            all_leds("off")
            print("OFF")
            sleep(0.2)

        elif GPIO.input(RED_BUTTON_PIN) == False:
            print("RED")
            all_leds("off")
            led_on(RED1_LED_PIN)
            led_on(RED2_LED_PIN)
            sleep(0.2)

        elif GPIO.input(YELLOW_BUTTON_PIN) == False:
            print("YELLOW")
            all_leds("off")
            led_on(YELLOW1_LED_PIN)
            led_on(YELLOW2_LED_PIN)
            sleep(0.2)

        elif GPIO.input(GREEN_BUTTON_PIN) == False:
            print(f"GREEN")
            all_leds("off")
            led_on(GREEN1_LED_PIN)
            led_on(GREEN2_LED_PIN)
            sleep(0.2)

    except Exception as e:
        handle_error(e, "The check_buttons function failed")


def light_show():
    try:
        print("Light show!")

        # lightshow_on = True
        lightshow_on = 0
        loop_sleep_time = 0.1

        all_leds("on")
        sleep(0.5)
        all_leds("off")

        while lightshow_on < 7:

            all_leds("off")
            led_on(RED1_LED_PIN)
            led_on(RED2_LED_PIN)
            sleep(loop_sleep_time)

            all_leds("off")
            led_on(YELLOW1_LED_PIN)
            led_on(YELLOW2_LED_PIN)
            sleep(loop_sleep_time)

            all_leds("off")
            led_on(GREEN1_LED_PIN)
            led_on(GREEN2_LED_PIN)
            sleep(loop_sleep_time)

            lightshow_on = lightshow_on + 1

        all_leds("off")
        led_on(RED1_LED_PIN)
        led_on(RED2_LED_PIN)

    except Exception as e:
        handle_error(e, "The light_show function failed")
    


if __name__ == "__main__":
    setup_pins()

    GPIO.output(INDICATOR_LED_PIN, GPIO.HIGH)

    light_show()

    try:
        while True:
            check_buttons()

    except Exception as e:
        handle_error(e, "The main function failed")

    except KeyboardInterrupt:
        print("Ctrl+C pressed. Program Terminated")
        GPIO.cleanup()
        exit()


        


