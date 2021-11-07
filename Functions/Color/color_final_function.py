import random
import cv2
from .color_square import cv_draw
from .color_naming import naming
from webcolors import name_to_hex

class conversions:
	def rgb_to_hex(R, G, B):
		hex_Hash = '#%02x%02x%02x' % (R, G, B)
		hex = '0x%02x%02x%02x' % (R, G, B)
		hexa = int(hex, (16))
		return hex_Hash, hexa
		
	def hex_to_rgb(hex):
		hex = hex.replace('#', '')
		rgb = tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))
		return rgb

class color_main:
	def RandRGB(discord_Embed, discord_Author, discord_Author_Avatar, discord_File):
		R = random.randint(0, 255)
		G = random.randint(0, 255)
		B = random.randint(0, 255)
		RGB = R, G, B
		Hex, Hex_C = conversions.rgb_to_hex(R, G, B)
		Hex = Hex.upper()

		img = cv_draw.draw_square(RGB, 360)
		img_cornered = cv_draw.add_corners(img, 10, 1, RGB)
		cv2.imwrite('c.png', img_cornered)
		
		actual_name, closest_name = naming.get_colour_name(RGB)
		
		if actual_name != None:
			name = actual_name.upper()
			in_hex = name_to_hex(actual_name)
			in_rgb = conversions.hex_to_rgb(in_hex)
		else:
			name = closest_name.upper()
			in_hex = name_to_hex(closest_name)
			in_rgb = conversions.hex_to_rgb(in_hex)
		
		embed=discord_Embed(
			title = name, 
			color = Hex_C, 
			description = f'**RGB : {in_rgb}\nHEX : {in_hex.upper()}**'
		)
		file = discord_File("c.png", filename="c.png")
		embed.set_thumbnail(url="attachment://c.png")
		
		return file, embed