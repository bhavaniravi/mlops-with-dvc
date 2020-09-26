import pandas as pd
from config import Config
import utils


def preprocess(force=False):
    try:
        if force:
            raise FileNotFoundError
        train_df = pd.read_csv(Config.PREPROCESSED_TRAIN)
        test_df = pd.read_csv(Config.PREPROCESSED_TEST)

        hashtags_train = pd.read_csv(f"{Config.PREPROCESS_PATH}/hashtags_train.csv")
        hashtags_test = pd.read_csv(f"{Config.PREPROCESS_PATH}/hashtags_test.csv")
    except FileNotFoundError:
        train_df = pd.read_csv(Config.TRAIN_DATASET)
        test_df = pd.read_csv(Config.TEST_DATASET)
        # Get length
        train_df['lengths'] = train_df['tweet'].apply(len)
        test_df['lengths'] = test_df['tweet'].apply(len)

        # encode ascii
        train_df['tweet'] = train_df['tweet'].apply(utils.encode)
        test_df['tweet'] = test_df['tweet'].apply(utils.encode)
        

        hashtags_train = train_df['tweet'].apply(utils.get_hashtags).explode()
        hashtags_test = test_df['tweet'].apply(utils.get_hashtags).explode()

        # remove puntuation
        train_df['tweet'] = train_df['tweet'].apply(utils.remove_puncuation)
        test_df['tweet'] = test_df['tweet'].apply(utils.remove_puncuation)

        # remove  stop words
        train_df['tweet'] = train_df['tweet'].apply(utils.remove_stop_words)
        test_df['tweet'] = test_df['tweet'].apply(utils.remove_stop_words)

        import os
        os.mkdir(Config.PREPROCESS_PATH)

        train_df.to_csv(Config.PREPROCESSED_TRAIN)
        test_df.to_csv(Config.PREPROCESSED_TEST)

        hashtags_train.to_csv(f"{Config.PREPROCESS_PATH}/hastags_train.csv")
        hashtags_test.to_csv(f"{Config.PREPROCESS_PATH}/hashtags_test.csv")

if __name__ == '__main__':
    preprocess(force=False)

