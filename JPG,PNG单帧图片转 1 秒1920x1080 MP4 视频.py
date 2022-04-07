import os, shutil, subprocess, json
from PIL import Image

def translate_items(scanfilter):
	for root, dirs, files in os.walk(scanfilter):
		if root != scanfilter:
			continue

		for d in dirs:
			translate_items(scanfilter + "/" + d)

		for file in files:
			extname = file[-4:].lower()

			if extname != ".jpg" and extname != ".png" and extname != "jpeg":
				continue

			extlen = 4
			if extname == "jpeg":
				extlen = 5

			srcfile = scanfilter + "/" + file
			tmpfile = scanfilter + "/" + "temp_" + file
			dstfile = scanfilter + "/" + file[0:-extlen] + ".mp4"

			img = Image.open(srcfile)
			out = img.resize((1920, 1080))
			try:
				out.save(tmpfile)		
			except:
				tmpfile += ".png"
				out.save(tmpfile)
				
			os.system("ffmpeg -r 25 -loop 1  -i %s -pix_fmt yuv420p -r 25 -t 1 %s" % (tmpfile, dstfile))
			os.remove(tmpfile)

if __name__ == "__main__":
	translate_items(".")