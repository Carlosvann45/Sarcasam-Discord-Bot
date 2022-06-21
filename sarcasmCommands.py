import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import BernoulliNB


class SarcasmCommands:
    def __init__(self):
        self.fileName = 'Sarcasm.json'
        self.model = BernoulliNB()
        self.cv = CountVectorizer()

    def train_bernoulli_model(self):
        # reads json from file nad sets it up for model
        data = pd.read_json(self.fileName, lines=True)
        data["is_sarcastic"] = data["is_sarcastic"].map({0: "Not Sarcasm", 1: "Sarcasm"})
        data = data[["headline", "is_sarcastic"]]
        x = np.array(data["headline"])
        y = np.array(data["is_sarcastic"])

        # Trains model on values based from Bernoulli's algorithm
        x = self.cv.fit_transform(x)  # Fit the Data
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=42)
        self.model.fit(x_train, y_train)

    def check_model_prediction(self, message):
        # checks trained model with phrase sent through request
        data = self.cv.transform([message.content]).toarray()
        output = self.model.predict(data)

        if output[0].lower() == 'sarcasm':
            await message.channel.send(f'{message.author.mention}that\'s sarcastic! Stop it!')
