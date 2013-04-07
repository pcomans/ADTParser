import urllib2
from lxml import etree
from PIL import Image

class ADTParser:
	def __init__(self, url):
		page = self.readURL(url)

		myparser = etree.HTMLParser(encoding="utf-8")
		tree = etree.HTML(page, parser=myparser)

		adtElement = tree.find(".//div[@id='mw-content-text'].p")
		self.title = adtElement.find("b/a").get("title")

		smallElement = adtElement.find("small")
		adtElement.remove(smallElement)
		self.text = etree.tostring(adtElement, method='text', encoding="utf-8").strip()

		adtImage = tree.find(".//div[@id='mw-content-text']//img")
		self.imageURL = "http:" + adtImage.get("src").strip()

	def readURL(self, url):
		opener = urllib2.build_opener()
		opener.addheaders = [('User-agent', 'Mozilla/5.0')]
		return opener.open(url).read()

	def getADTImage(self):
		return self.readURL(self.imageURL)

def main():
	adtparser = ADTParser('http://de.wikipedia.org/wiki/Benutzer:Volton/ADTTest')
	print(adtparser.title)
	print(adtparser.text)
	print(adtparser.imageURL)

	imageData = adtparser.getADTImage()
	open('adt.png', 'wb').write(imageData)

	#The ADT image might have a transparent background which would show up black in the BW image
	#Create an entirely white image and paste the ADT image on top
	adtImage = Image.open("adt.png")
	
	if (adtImage.mode == "RGBA"):
		whiteBG = Image.new("RGB", adtImage.size, "white")
		#Note that if you paste an "RGBA" image, the alpha band is ignored.
		#You can work around this by using the same image as both source image and mask.
		whiteBG.paste(adtImage, (0,0), adtImage)
	else:
		whiteBG = adtImage
	
	adtImageBW = whiteBG.convert("1")
	adtImageBW.save('adt_bw.png')

if __name__ == "__main__":
	main()