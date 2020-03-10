FROM fedora:31

COPY rss/ /rss/

RUN dnf install -y git python3-pip && pip3 install --user feedparser git+git://github.com/tainn/ookami.git

WORKDIR /rss

CMD ["/rss/rss.py"]
