import pandas as pd
from config import Config
from src import utils
from sklearn.feature_extraction.text import CountVectorizer
from numpy import savetxt
import pickle, os

def featurize(dataset, vectorizer_analyzer):
    fit_and_transform = dataset == "train"
    preped_df = pd.read_csv(f"{Config.PREPROCESS_PATH}/{dataset}.csv")
    preped_df["tweet"] = preped_df["tweet"].fillna("")
    if fit_and_transform:
        countvectorizer_tweets = vectorizer_analyzer.fit_transform(preped_df['tweet'])
        pickle.dump(vectorizer_analyzer, open(f"{Config.FEATURES_PATH}/vectorizer.pickle", "wb"))
    else:
        countvectorizer_tweets =  vectorizer_analyzer.transform(preped_df['tweet'])
    return countvectorizer_tweets


def create_featurizer(dataset, force=False):
    if not os.path.isdir(Config.FEATURES_PATH):  
        os.mkdir(Config.FEATURES_PATH)
    try:
        if force:
            raise FileNotFoundError("Forcing creation")
        vectorizer_analyzer = pickle.load(open(f"{Config.FEATURES_PATH}/vectorizer.pickle", "rb"))  
    except FileNotFoundError as e:
        vectorizer_analyzer = CountVectorizer()
        fit_and_transform=True
        if dataset == "test":
            raise Exception("Cannot transform without fitting")
    featurize(dataset, vectorizer_analyzer)


if __name__ == '__main__':
    create_featurizer("train")
    create_featurizer("test")