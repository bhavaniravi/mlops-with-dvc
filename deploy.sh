set -x
export PYTHONPATH=.
python python-setup.py
dvc pull -r gcs
dvc repro
gunicorn app:app -w 6 --threads 10 -b 0.0.0.0:80