import os, sys
sys.path.insert(0,f'{os.getcwd()}/src')

from preprocess import preprocess_df
from featurize import featurize_df
from model import infer_df
from config import Config
import pandas as pd
import pickle


def predict(text):
    df = pd.DataFrame([{"id": 1, "tweet":text}])
    df = preprocess_df(df)
    features = featurize_df(df)
    model = pickle.load(open(f"{Config.MODELS_PATH}/model.pickle", "rb"))
    result_df = infer_df(model, features)
    return result_df
    