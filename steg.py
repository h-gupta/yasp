from stegano import lsb,exifHeader,lsbset
import sys,os,subprocess
from stegano.lsbset import generators

f = open(sys.argv[1],'r')
print ("1->Image")
ch = input()
if(ch == 1):
	print("1.)JPEG or TIFF\n2.)PNG")
	n=input()
	if(n == 1 ):
		print("1.Hide data\n2.Reveal Data")
		i = input()
		if(i == 1):
			print("Enter the full path to the JPEG or TIFF image file")
			p1=raw_input()
			secret = exifHeader.hide(p1,"/root/Desktop/out1.jpg",secret_message=f.read().strip())

		if(i == 2):
			print("Enter the path to the image")
			p2 = raw_input()
			print(exifHeader.reveal(p2))

	if(n == 2):
		print("1.Hide data\n2.Reveal Data")
		i1=input()
		if(i1 == 1):
			print("Enter the full path to PNG image")
			p3=raw_input()
			secret_message=f.read().strip()
			secret_image = lsbset.hide(p3,secret_message,generators.eratosthenes())
			secret_image.save("/root/Desktop/image.png")
		
		if(i1 == 2):
			print("enter the path of PNG image")
			p4=raw_input()
			message = lsbset.reveal(p4, generators.eratosthenes())
			print message
