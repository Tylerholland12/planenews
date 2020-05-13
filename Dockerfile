# FROM python

# RUN apk update


RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

# add a requirements.txt file before cashing to the rest of the repo
RUN pip install -r requirements.txt

# install dependencies
RUN npm install

# copy the code into the directory
# COPY . /usr/src/app

# CMD 