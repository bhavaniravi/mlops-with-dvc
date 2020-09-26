from sklearn.naive_bayes import MultinomialNB
import pickle
import featurize
import pandas as pd
import json
from config import Config
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
import os

def train(model, X_train, y_train):
    fitted_model = model.fit(X_train,y_train)


def test(model, X_test, y_test):
    prediction = model.predict(X_test)
    cm = confusion_matrix(y_test, prediction)
    score = accuracy_score(y_test, prediction)
    with open(f"{Config.EVAL_PATH}/scores.json", "w") as f:
        f.write(json.dumps({"acc": score}))
    print ("Accuracy ::", score)
    print ("CM :: \n", cm)

def infer(model):
    infer_df = pd.read_csv(Config.TEST_DATASET)
    vectorizer_analyzer = pickle.load(open(f"{Config.FEATURES_PATH}/vectorizer.pickle", "rb")) 
    X_infer = featurize.featurize("test", vectorizer_analyzer)

    result_df = pd.DataFrame()
    result_df["id"] = infer_df["id"]
    result_df["infer"] = model.predict(X_infer)

    result_df.to_csv(f"{Config.MODELS_PATH}/result.csv", index=False)


def run(model):  
    train_df = pd.read_csv(Config.TRAIN_DATASET)
    
        
    vectorizer_analyzer = pickle.load(open(f"{Config.FEATURES_PATH}/vectorizer.pickle", "rb")) 
    X_features = featurize.featurize("train", vectorizer_analyzer)
    X_train, X_test, y_train, y_test = train_test_split(X_features, train_df["label"], test_size = 0.2, random_state = 1)
    # print ("Train, test :: ", X_train.shape, X_test.shape)
    del X_features
    
    train(model, X_train, y_train)
    test(model, X_test, y_test)
    result = infer(model)

import os
if not os.path.isdir(Config.MODELS_PATH):
    os.mkdir(Config.MODELS_PATH)

if not os.path.isdir(Config.EVAL_PATH):
    os.mkdir(Config.EVAL_PATH)


model = MultinomialNB()
run(model)
pickle.dump(model, open(f"{Config.MODELS_PATH}/model.pickle", "wb"))