import matplotlib.pyplot as plt
from wordcloud import WordCloud

def printwordCloud(text):
	wordcloud = WordCloud().generate(text)
	img=plt.imshow(wordcloud)
	plt.axis("off")
	plt.show()
	 
	#or save as png
	img.write_png("wordcloud.png")