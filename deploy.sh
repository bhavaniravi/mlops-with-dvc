set -x
dvc pull
dvc repro
dvc push
export PYTHONPATH=.
gunicorn app:app -w 6 --threads 10 -b 0.0.0.0:5000