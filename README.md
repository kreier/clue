# Adafruit clue nRF52840 Express

<img src="docs/clue_i2c.jpg" width="30%" align="right">

Programs and experiments with the Adafruit CLUE NRF52840 Express. It has several sensors directly included, a bright TFT display to give feedback and show data, and a Stemma QT connector for further i2c periferals. Just Wifi is missing. It has

- Nordic nRF52840 Bluetooth LE processor - 1 MB of Flash, 256KB RAM, 64 MHz Cortex M4 processor
- 1.3″ 240×240 Color IPS TFT display for high resolution text and graphics
- Two A / B user buttons and one reset button
- 2 MB internal flash storage for datalogging, images, fonts or CircuitPython code
- Hardware SPI, UART, I2C, and I2S on any pins
- Buzzer/speaker for playing tones and beeps
- Two bright white LEDs in front for illumination / color sensing.
- Qwiic / STEMMA QT connector for adding more sensors, motor controllers, or disp

### Sensors

- ST Micro series 9-DoF motion - LSM6DS33 Accel/Gyro + LIS3MDL magnetometer
- APDS9960 Proximity, Light, Color, and Gesture Sensor
- PDM Microphone sound sensor
- SHT Humidity
- BMP280 temperature and barometric pressure/altitude
- RGB NeoPixel indicator LED

Here is it with some sensors connected and running an i2c_scanner.py:

![Clue with i2c periferals](docs/clue_i2c_2.jpg)

## Comparison Clue with TFT Gizmo and CircuitPlayground Express

Both have 240x240 pixel displays. And we have one Hallowing M0 with 128x128.
