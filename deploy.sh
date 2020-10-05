set -x
export PYTHONPATH=.
python python-setup.py
dvc pull
dvc repro
dvc push
gunicorn app:app -w 6 --threads 10 -b 0.0.0.0:5000