# MLOps - Devfest

The project is designed to for a talk at #devfestindia-2020

## Video 

[DevfestIndia Talk Video](https://youtu.be/chtdrBvJpZ4?t=1101)

## Topics to be convered

1. Data versioning
2. Building training pipelines
3. Versioning models
4. Deploying using docker and kubernetes

---

## Recreate Steps for new project

[Checkout demo steps here](demo_steps.md)



---

## Run this project

### Pre-Requisites

1. Python 3.7
2. Pip

### Setup the project

1. Clone the repo

```
git clone <repo_url>
cd <repo-name>
```

2. Pull the data from gdrive

```
dvc pull -r gdrive
```

> It will ask for authorization, please enter the auth key from the URL 

3. Install requirements

```
pip install -r requirements.txt
```

### Run project


1. Run the application

```
python app/app.py
```

2. Update model/any ML step and run

```
dvc repro
dvc push -r gdrive
```


---

## DVC Notes

> How is the pipeline created?

```
dvc run -n preprocess -d src/preprocess.py -d assets/original_data/train.csv  -o assets/preprocessed/  python src/preprocess.python
dvc run -n featurize -d src/preprocess.py -d assets/preprocessed/train.csv -d assets/preprocessed/train.csv   -o assets/featurized/  python src/featurize.py 
dvc run -fn train_test_eval  -d src/model.py -d assets/featurized -p model.random,model.split  -o assets/models  -M assets/eval/scores.json  python src/model.py 
dvc run -fn train_test_eval  -d src/model.py -d assets/featurized -p model.random,model.split  -o assets/models  -M assets/eval/scores.json  python src/model.py 
```
