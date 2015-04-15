import pandas as pd
import re
import matplotlib.pyplot as plt

df = pd.io.json.read_json("./data.json")
def word_in_text(word, text):
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)
    return bool(match)

multicategories = {"motor": ['motor', 'car', 'truck'],
"fashion": ['fashion', 'watch', 'jawelry'], 
"electronic" : ['electronic', 'camera', 'photo'],
"art" : ['art', 'collectible'],
"sport" : ['sport', 'fitness', 'excercise', 'run']}

for category in multicategories.values():
    df[category[0]] = df['text'].apply(
        lambda tweet: any(word_in_text(word, tweet) for word in category))

counts = pd.melt(df[multicategories.keys()]).groupby('variable').sum()
counts.sort('value', inplace=True)
counts.plot(kind='bar')
plt.show()

