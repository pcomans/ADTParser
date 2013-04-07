import urllib2
from lxml import etree

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
	open('adt.jpg', 'wb').write(imageData)

if __name__ == "__main__":
	main()