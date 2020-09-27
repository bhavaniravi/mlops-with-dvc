# MLOps - Devfest

The project is designed to for a talk at #devfestindia-2020

## Topics to be convered

1. Data versioning
2. Building training pipelines
3. Versioning models
4. Deploying using docker and kubernetes

## Slides

WIP

## Setup and Run project

The project still doesn't have a remote dvc so it's a WIP

## DVC Notes

> To be updated

```
dvc run -n preprocess -d src/preprocess.py -d assets/original_data/train.csv  -o assets/preprocessed/  python src/preprocess.python
dvc run -n featurize -d src/preprocess.py -d assets/preprocessed/train.csv -d assets/preprocessed/train.csv   -o assets/featurized/  python src/featurize.py 
dvc run -fn train_test_eval  -d src/model.py -d assets/featurized -p model.random,model.split  -o assets/models  -M assets/eval/scores.json  python src/model.py 
dvc run -fn train_test_eval  -d src/model.py -d assets/featurized -p model.random,model.split  -o assets/models  -M assets/eval/scores.json  python src/model.py 
```

