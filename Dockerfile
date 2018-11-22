FROM ubuntu:xenial

USER root

RUN apt-get update && \
    apt-get install -y software-properties-common && \
    apt-add-repository ppa:deadsnakes/ppa && \
    apt-get -y update && \
    apt-get -y install python3 && \
    apt-get -y install python3-bs4

# make some useful symlinks
RUN ln -f -s /usr/bin/pydoc3 /usr/local/bin/pydoc && \
    ln -f -s /usr/bin/python3 /usr/local/bin/python && \
    ln -f -s /usr/bin/python3-config /usr/local/bin/python-config

ADD ./code /code
WORKDIR /code

EXPOSE 8080

CMD ["sh", "-c", "python -u ./main.py"]