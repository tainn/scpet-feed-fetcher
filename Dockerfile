FROM fedora:31

COPY fetcher /fetcher
COPY data /data
WORKDIR /fetcher

RUN dnf install -y git python3-pip && pip3 install --user feedparser git+git://github.com/tainn/ookami.git

ENV PYTHONPATH="$PYTHONPATH:/fetcher"
