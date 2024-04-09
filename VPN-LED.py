import RPi.GPIO as GPIO
import subprocess
import time

# Set up GPIO pins
green_led_pin = 17  # Change to your green LED GPIO pin
red_led_pin = 18    # Change to your red LED GPIO pin
GPIO.setmode(GPIO.BCM)
GPIO.setup(green_led_pin, GPIO.OUT)
GPIO.setup(red_led_pin, GPIO.OUT)

# Function to check VPN connection status
def check_vpn_status():
    try:
        # Run command to check VPN status
        vpn_status = subprocess.check_output("YOUR_VPN_STATUS_COMMAND", shell=True)
        return True  # VPN is connected
    except subprocess.CalledProcessError:
        return False  # VPN is disconnected

# Main loop
while True:
    vpn_connected = check_vpn_status()
    if vpn_connected:
        # Turn on green LED and turn off red LED
        GPIO.output(green_led_pin, GPIO.HIGH)
        GPIO.output(red_led_pin, GPIO.LOW)
    else:
        # Turn off green LED and turn on red LED
        GPIO.output(green_led_pin, GPIO.LOW)
        GPIO.output(red_led_pin, GPIO.HIGH)
    time.sleep(1)  # Check VPN status every second
