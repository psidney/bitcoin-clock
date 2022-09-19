# Bitcoin price on screen


import requests
import time
import upstart

url = 'https://api.coindesk.com/v1/bpi/currentprice.json'


#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd2in7b
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

logging.basicConfig(level=logging.DEBUG)
def updateText(textToDisplay):
	try:

		epd = epd2in7b.EPD()

		logging.info("init and Clear")
		epd.init()
		epd.Clear()
		time.sleep(1)

		# Drawing on the image
		logging.info("Drawing")
		blackimage = Image.new('1', (epd.width, epd.height), 255)  # 255: clear the frame
		redimage = Image.new('1', (epd.width, epd.height), 255)  # 255: clear the frame

		font24 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)
		font18 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 18)

		# Drawing on the Horizontal image
		HBlackimage = Image.new('1', (epd.height, epd.width), 255)  # 298*126
		HRedimage = Image.new('1', (epd.height, epd.width), 255)  # 298*126    
		drawblack = ImageDraw.Draw(HBlackimage)
		drawred = ImageDraw.Draw(HRedimage)
		drawblack.text((10, 0), textToDisplay, font = font24, fill = 0)
		epd.display(epd.getbuffer(HBlackimage), epd.getbuffer(HRedimage))
		epd2in7b.epdconfig.module_exit()

		
	except IOError as e:
		logging.info(e)

	except KeyboardInterrupt:    
		logging.info("ctrl + c:")
		epd2in7b.epdconfig.module_exit()
		exit()



while True:
	#result = requests.get(url)
	#rate = result.json()['bpi']['USD']['rate'].replace(',','')

	rate = upstart.get_rate()	
	updateText(str(round(float(rate),2)))
	time.sleep(10)