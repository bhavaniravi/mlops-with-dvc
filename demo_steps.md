# MLOps

## Data and model versioning

### Define a project structure

```
├── app
│   └── app.py
├── assets
│   ├── eval
│   ├── featurized
│   ├── models
│   ├── original_data
│   │   ├── test.csv
│   │   └── train.csv
│   └── preprocessed
└── src
    ├── config.py
    ├── preprocess.py
    ├── featurize.py
    └── utils.py
```

### Initializing the project

```
git init
dvc init
```

### Add original Data

```
dvc add assets/original_data
```

### Create pipeline scripts

> Edit preprocessing.py

### Create pipeline stage

```
dvc run -n preprocess -d assets/original_data -o assets/preprocessed python src/preprocess.py
```

### Set remote

```
dvc remote add -d local ./dvc-remote
```

### Push changes

```
dvc push -r local
```

## Change data and reproduce steps

```
dvc repro
```



## CI/CD Pipeline

1. Setup GCS remote folder

```
dvc remote add gcs gs://mlops-dvc-storage
dvc push -r gcs
```

2. Setup DockerFile

3. Setup kubernetes yaml

4. Setup CI/CD script

> Commit and push code