import pandas as pd
from config import Config
import utils

def preprocess_df(df):
    df['lengths'] = df['tweet'].apply(len)
    df['tweet'] = df['tweet'].apply(utils.encode)
    df["tweet"] = df["tweet"].apply(utils.remove_mention)
    df['tweet'] = df['tweet'].apply(utils.remove_puncuation)
    return df

def preprocess(force=False):
    try:
        if force:
            raise FileNotFoundError
        train_df = pd.read_csv(Config.PREPROCESSED_TRAIN)
        test_df = pd.read_csv(Config.PREPROCESSED_TEST)
    except FileNotFoundError:
        train_df = pd.read_csv(Config.TRAIN_DATASET)
        test_df = pd.read_csv(Config.TEST_DATASET)

        train_df = preprocess_df(train_df)
        test_df = preprocess_df(test_df)

        import os
        os.mkdir(Config.PREPROCESS_PATH)

        train_df.to_csv(Config.PREPROCESSED_TRAIN)
        test_df.to_csv(Config.PREPROCESSED_TEST)

if __name__ == '__main__':
    preprocess(force=False)

