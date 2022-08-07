from wordcloud import WordCloud
import matplotlib.pyplot as plt


def create_wordcloud(text, width = 800, height = 600, bg_color = 'white', font_path = 'C:\Windows\Fonts\msgothic.ttc',filename = None,show = False):
    wdcloud = WordCloud(width = width, height = height, background_color = bg_color, font_path = font_path,collocations = False).generate(text)
    plt.figure(figsize=(12,10))
    plt.imshow(wdcloud)
    if filename != None:
       wdcloud.to_file(filename)
    if show:
        plt.show()

