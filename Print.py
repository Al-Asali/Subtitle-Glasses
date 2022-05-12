import time
import board
import busio
import digitalio

from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

import subprocess


def Display(lines):
	# Define the Reset Pin
	oled_reset = digitalio.DigitalInOut(board.D4)

	# Display Parameters
	WIDTH = 128
	HEIGHT = 64
	BORDER = 5

	# Use for I2C.
	i2c = board.I2C()
	oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c, addr=0x3C, reset=oled_reset)

	# Clear display.
	oled.fill(0)
	oled.show()

	# Create blank image for drawing.
	# Make sure to create image with mode '1' for 1-bit color.
	image = Image.new("1", (oled.width, oled.height))

	# Get drawing object to draw on image.
	draw = ImageDraw.Draw(image)

	# Draw a white background
	draw.rectangle((0, 0, oled.width, oled.height), outline=255, fill=255)

	try:
		font = ImageFont.truetype('PixelOperator.ttf', 16)
	except:
		font = ImageFont.load_default()

    # Draw a black filled box to clear the image.
	draw.rectangle((0, 0, oled.width, oled.height), outline=0, fill=0)
	line1 = lines[0]
	line2 = lines[1]
	line3 = lines[2]
	line4 = lines[3]
	
    # Pi Stats Display
	draw.text((0, 00), line1, font=font, fill=255)
	draw.text((0, 16), line2, font=font, fill=255)
	draw.text((0, 32), line3, font=font, fill=255)
	draw.text((0, 48), line4, font=font, fill=255)
        
    # Display image
	oled.image(image)
	oled.show()
	time.sleep(.1)

if __name__=="__main__":
	Display(["W"*21,"M"*21,"a","test"])
