FROM python:3.7

RUN apt install python3.7-distutils

# set working directory
WORKDIR /project

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# add requirements
RUN git clone https://github.com/bhavaniravi/mlops-with-dvc.git .

# updating pip
# ADD https://bootstrap.pypa.io/get-pip.py /get-pip.py
# RUN python /get-pip.py

# install requirements
RUN pip install -r requirements.txt

# run server
#CMD python manage.py runserver
CMD bash ./deploy.sh

# expose
EXPOSE 5000
