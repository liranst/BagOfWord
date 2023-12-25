import pandas as pd


class BagOfWord:
    """
    program that reads all the samples in the dataset into a
    bag of word data structure with only the 20 most common words in the whole dataset,
    Ignoring the stopwords
    """

    def __init__(self, data: str, stopwords: str):
        """
        The path address for the stop words, data.
        """
        self.data = data
        self.stopwords = stopwords
        self.reviews = None
        self.stopwords_set = None

    def read(self):
        """
        :return: reading the 'stopwords' and data.
        """
        self.data = pd.read_csv(self.data, index_col=0)
        self.stopwords = open(self.stopwords, "r")

    def Processing(self):
        """        Turn the data into a vector of words.
        In addition, it removes the stop words, punctuation marks
        """
        self.read()
        self.stopwords_set = set([word.strip() for word in self.stopwords])
        self.reviews = self.data["reviews"].str.lower().str.split().replace("!", ".")

        self.reviews = self.reviews.apply(
            lambda review: [word for word in review if word not in self.stopwords_set])

    def stack(self):
        """
        :return: Creating a table of the 20 most common words, not including stop words
        """
        self.Processing()
        top20 = self.reviews.apply(pd.Series).stack().value_counts().head(20).index.tolist()
        top20_counts = self.reviews.apply(
            lambda review: pd.Series([review.count(words) for words in top20], index=top20))
        return top20_counts
