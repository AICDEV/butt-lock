# pulling alpine linux
FROM alpine:3.10

# prepare
RUN apk update && \
    apk add g++ && \
    apk add git python3 py-pip && \
    pip3 install --upgrade pip && \ 
    git clone https://github.com/AICDEV/butt-lock.git && \
    pip3 install -r butt-lock/requirements.txt && \
    mkdir butt-lock/temp && \
    echo "Hello" > butt-lock/temp/hello.txt && \
    echo "World" > butt-lock/temp/world && \
    echo "run the following command 'python3 main.py --mode=encrypt --dir ./temp --replace copy' inside butt-lock folder" > HOW_TO_ENCRYPT && \
    echo "run the following command 'python3 main.py --mode=decrypt --dir ./temp/ --recovery ./buttlock/buttlock_recovery'  inside butt-lock folder" > HOW_TO_DECRYPT

# JUST FOR THE DEMO - DON'T USE IT IN PRODUCTION
ENTRYPOINT ["tail", "-f", "/dev/null"]
