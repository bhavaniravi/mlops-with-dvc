class Config:
    ORIGINAL_DATASET_PATH = "assets/original_data"
    TRAIN_DATASET = f"{ORIGINAL_DATASET_PATH}/train.csv"
    TEST_DATASET = f"{ORIGINAL_DATASET_PATH}/test.csv"
    PREPROCESS_PATH = "assets/preprocessed"
    FEATURES_PATH = "assets/featurized"
    MODELS_PATH = "assets/models"

    PREPROCESSED_TRAIN = f"{PREPROCESS_PATH}/train.csv"
    PREPROCESSED_TEST = f"{PREPROCESS_PATH}/test.csv"