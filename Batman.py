from wordcloud import WordCloud, STOPWORDS ,ImageColorGenerator
# to get the color of our image
import numpy as np
# to load our image
from PIL import Image
# to display our wordcloud
import matplotlib.pyplot as plt

# content-related
text = open("batman.txt",'r').read()
stopword = set(STOPWORDS)

# Appearance-related
custom_mask = np.array(Image.open("batman.png"))
wc=WordCloud(
    background_color='white',
    stopwords=stopword,
    mask =custom_mask,
    contour_width=3,
    contour_color='black'
)
wc.generate(text)
Image_colors =ImageColorGenerator(custom_mask)
wc.recolor(color_func=Image_colors)

# plotting
# plt.imshow(wc, interpolation = 'bilinear')
# plt.axis('off')
# plt.show()

wc.to_file('Batman_WordCloud.png')
