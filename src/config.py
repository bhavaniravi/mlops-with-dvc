class Config:
    BASE = "assets"
    ORIGINAL_DATASET_PATH = f"{BASE}/original_data"
    TRAIN_DATASET = f"{ORIGINAL_DATASET_PATH}/train.csv"
    TEST_DATASET = f"{ORIGINAL_DATASET_PATH}/test.csv"
    PREPROCESS_PATH = f"{BASE}/preprocessed"
    FEATURES_PATH = f"{BASE}/featurized"
    MODELS_PATH = f"{BASE}/models"
    EVAL_PATH = f"{BASE}/eval"

    PREPROCESSED_TRAIN = f"{PREPROCESS_PATH}/train.csv"
    PREPROCESSED_TEST = f"{PREPROCESS_PATH}/test.csv"