# pulling alpine linux
FROM alpine:3.10

# update package list
RUN apk update

# install base deps
RUN apk add g++

# install git
RUN apk add git

# install python and pip
RUN apk add python3 py-pip && pip3 install --upgrade pip

# checkout butt-lock
RUN git clone https://github.com/AICDEV/butt-lock.git

# install butt-lock deps
RUN pip3 install -r butt-lock/requirements.txt

# prepare test szenario
RUN mkdir butt-lock/temp

# building test file
RUN echo "Hello" > butt-lock/temp/hello.txt
RUN echo "World" > butt-lock/temp/world

# building instruction

RUN echo "run the following command 'python3 main.py --mode=encrypt --dir ./temp --replace copy' inside butt-lock folder" > HOW_TO_ENCRYPT

RUN echo "run the following command 'python3 main.py --mode=decrypt --dir ./temp/ --recovery ./buttlock/buttlock_recovery'  inside butt-lock folder" > HOW_TO_DECRYPT

# JUST FOR THE DEMO - DON'T USE IT IN PRODUCTION
ENTRYPOINT ["tail", "-f", "/dev/null"]
