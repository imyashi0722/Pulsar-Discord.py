import webcolors

class search:
	def closest_colour(requested_colour):
		min_colours = {}
		for key, name in webcolors.CSS3_HEX_TO_NAMES.items():
			r_c, g_c, b_c = webcolors.hex_to_rgb(key)
			rd = (r_c - requested_colour[0]) ** 2
			gd = (g_c - requested_colour[1]) ** 2
			bd = (b_c - requested_colour[2]) ** 2
			min_colours[(rd + gd + bd)] = name
		return min_colours[min(min_colours.keys())]

class naming:
	def get_colour_name(requested_colour):
		RGB = requested_colour
		try:
			closest_name = actual_name = webcolors.rgb_to_name(requested_colour)
		except ValueError:
			closest_name = search.closest_colour(RGB)
			actual_name = None
		return actual_name, closest_name