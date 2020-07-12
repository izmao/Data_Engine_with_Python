# -*- coding:utf-8 -*-
# 词云展示
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize

# 生成词云
def create_word_cloud(f):
	print('根据词频，开始生成词云!')

	cut_text = word_tokenize(f)
	print(cut_text)
	cut_text = ",".join(cut_text)
	wc = WordCloud(
		max_words=10,
		width=2000,
		height=1200,
    )
	wordcloud = wc.generate(cut_text)
	# 写词云图片

	wordcloud.to_file("wordcloud.jpg")
	# 显示词云文件
	plt.imshow(wordcloud)
	plt.axis("off")
	plt.show()

# header=None，不将第一行作为head

with open('./Market_Basket_Optimisation.csv') as f:
    s = f.read().replace('\n',',') # add trailing new line character
print(s)
all_word = s
# 生成词云
create_word_cloud(all_word)
