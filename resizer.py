from PIL import Image
import os


def picList(searchDir):
	temp = os.listdir(searchDir)
	contents = filter(lambda x: ".jpg" in x.lower(), temp)
	return contents


def shrink(filename, ratio):
	im = Image.open(filename)
	(width, height) = im.size
	shrunk = im.resize((int(width*ratio), int(height*ratio)))
	shrunk.save(filename[:-4] + "_resized.jpg")
	print "Resized", filename, "to", ratio, "times original size"



def main():
	print "Enter the path to the directory containing the pictures you wish to resize:"
	searchDir = raw_input()
	pics = picList(searchDir)
	print "Found the following pictures:"
	print pics
	print "Enter the desired resize scale (ex: .5, 1.3, etc.):"
	ratio = float(raw_input())
	for image in pics:
		shrink(image, ratio) 

if __name__ == "__main__":
	main()