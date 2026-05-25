import string
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
from nltk.sentiment.vader import SentimentIntensityAnalyzer


#read the text file

t=open('read.txt',encoding='utf-8').read()


#convert into lower case

lower=t.lower()


#removing punctuation

clean=lower.translate(str.maketrans('','',string.punctuation))


#split the word from text

taken=clean.split()



final =[]
for word in taken:
    if word not in stopwords.words('english'):
        final.append(word)




#count emotion

el=[]
with open('emotion.txt','r') as file:
    for line in file:
        clears=line.replace("\n",'').replace(",",'').replace("'",'').strip()
        word,emotion=clears.split(':')
        if word in final:
            el.append(emotion)
    print(el)
w=Counter(el)
print(w)



#detect the text as positive , negative or neutral

def sentimnet_analyser(sentiment_text):
    s=SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    neg=s['neg']
    pos=s['pos']
    if neg>pos:
        print("Negative Sentiment")
    elif pos>neg:
        print("Positive Sentiment")
    else:
        print("Neutral Sentiment")

sentimnet_analyser(clean)




#plot graph

fig , ax1 =plt.subplots()
ax1.bar(w.keys(),w.values())
fig.autofmt_xdate()
plt.savefig('graph.png')
plt.show()


