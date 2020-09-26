from preprocess import preprocess

def predict(text):
    df = pd.Dataframe([{"id": 1, "tweet":text}])
    preprocess(df)