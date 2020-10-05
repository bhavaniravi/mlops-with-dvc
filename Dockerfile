FROM python:3.8

# set working directory
WORKDIR /project

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# add requirements
COPY ./requirements.txt /project/requirements.txt

# updating pip
ADD https://bootstrap.pypa.io/get-pip.py /get-pip.py
RUN python /get-pip.py

# install requirements
RUN pip install -r requirements.txt

# add source code
COPY . /project

WORKDIR /project/

# run server
#CMD python manage.py runserver
CMD bash ./deploy.sh

# expose
EXPOSE 5000
