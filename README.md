# Room Sense Sensor

This is an example of an MicroPython implementation for [Raspberry Pi Pico W](https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html) which can read from a DHT22 sensor and send it's readings to [Room Sense Api](https://github.com/MrLogEN/room-sense-api).

## Setup and Prerequisites

1. You need a [Raspberry Pi Pico W](https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html) and a DHT22.
2. Connect the the DHT22 to the [Raspberry Pi Pico W](https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html) you can find the schema in the [Assmebly](#Assembly) section.
3. Prepare the [Raspberry Pi Pico W](https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html) for [MicroPython](https://www.raspberrypi.com/documentation/microcontrollers/micropython.html#what-is-micropython).
5.  Clone this repository.
```shell
git clone https://github.com/MrLogEN/room-sense-sensor.git
```
6. Edit the `main.py`'s constants such as `SSID`, `PASSWORD` or `API_URL` to match your setup.
7. Upload the `main.py` script from the clone repository to the [Raspberry Pi Pico W](https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html) using [ampy](https://pypi.org/project/adafruit-ampy/) command line tool or [Thonny IDE](https://thonny.org/).


## Assembly

### Pins
This table shows, how you should connect your DHT22 sensor to a [Raspberry Pi Pico W](https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html).

|DHT22 Pin| Raspberry Pin |
|---------|---------------|
|VCC (Pin 1)| 3V3 (Pin 36) |
|Data (Pin 2) | GP15 (Pin 20) |
|GND (Pin 4) | GND (Pin 38) |

You can use any `GND` pin for ground or any `GP` pin for reading data. If you are not sure which pin is which, you can refer to the official [pinout](https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html#pinout-and-design-files) docs.

