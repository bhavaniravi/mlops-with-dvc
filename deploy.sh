set -x

dvc pull
export PYTHONPATH=.
gunicorn app:app -w 6 --threads 10 -b 0.0.0.0:5000