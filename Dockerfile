FROM fedora:31

COPY fetcher/ /fetcher/

RUN dnf install -y git python3-pip && pip3 install --user feedparser git+git://github.com/tainn/ookami.git

WORKDIR /fetcher

CMD ["/fetcher/fetcher.py"]
