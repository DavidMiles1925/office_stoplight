# Office Stoplight

## Project Decription

I work from home, and my workspace also happens to directly attatch to the garage. Because of this, my family often needs access to the garage, but does not know if I can be disturbed. This system will give them a definitive answer, by placing adjustable LEDs on the outside of the office and garage doors.

Please feel free to use everything here to build your own.

## Repo Contents

1. Project Diagram - This is meant to aid in the construction of the circuitry. Please feel free to reach out if you have questions.

2. Code - The "stoplight.py" file listed contains the code to run the program.

3. 3D Models - These contain print casings and mountings for the device.

4. Link to set up your Raspberry Pi zero, and get it running the program on startup: **[Click Here](https://github.com/DavidMiles1925/pi_zero_setup)**

## Hardware

### Components List

| Item                 | Quantity | Link        |
| -------------------- | -------- | ----------- |
| Raspberry Pi Zero    | 1        | Microcenter |
| Red LEDs             | 2        | Amazon      |
| Yellow LEDs          | 2        | Amazon      |
| Green LEDs           | 2        | Amazon      |
| BLue LED             | 1        | Amazon      |
| 220 Ohm Resistors    | 6        | Amazon      |
| 12mm Colored Buttons | 3        | Amazon      |
| Two-Prong Button     | 1        | Amazon      |

### Connections

| Purpose                  | Pin (BCM) |
| ------------------------ | --------- |
| Power Indicator          | 17        |
| Red LED - Desk           | 5         |
| Red LED - Hall           | 11        |
| Yellow LED - Desk        | 6         |
| Yellow LED - Hall        | 13        |
| Green LED - Desk         | 26        |
| Green LED - Hall         | 19        |
| Button - Lights OFF      | 12        |
| Button - Red Light ON    | 23        |
| Button - Yellow Light ON | 24        |
| Button - Green Light ON  | 25        |

## What the Lights Mean

- **RED:** DO NOT DISTURB
- **YELLOW:** You can come in, but be quiet.
- **GREEN:** Come on in!

## Description and Gallery

**Prototying**

![Prototype](./media/Prototyping.png)

**Main Unit - Final**

![Main Unit](./media/main_unit2.jpg)

**Door Unit - Final**

![Door Unit](./media/external_unit.jpg)
