import os, sys

for filename in os.listdir(os.path.dirname(os.path.abspath(__file__))):
	base_file, ext = os.path.splitext(filename)
	if ext == ".a2fWF5NXu":
		os.rename(filename, base_file + ".mp3")