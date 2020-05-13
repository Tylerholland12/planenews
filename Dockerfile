FROM python:3.7

# RUN apk -- no-cache --quiet add gcc make g++ bash bit openssh \
#     postgresql-dev curl build-base libffi-dev python-dev py-pip \
#     jpeg-dev zlib-dev libsass-dev
# 
RUN apt-get update && apt-get upgrade -y && apt-get autoremove && apt-get autoclean


# add a requirements.txt file before cashing to the rest of the repo
COPY requirements.txt /requirements.txt

# === [STAGE 2] ===
FROM python:3.7

RUN apk --no cache 

# create a directory onto the image
RUN mkdir -p $PROJECT_PATH

# creat new directory
RUN mkdir -p $PROJECT_PATH/media

# create new directory
RUN mkdir -p $PROJECT_PATH/static/assets

# copy the code into the directory
COPY . /usr/src/app

CMD sh /usr/src/app/run.sh