# scpet-feed-fetcher
`fetcher` is a script that enables automated fetching, parsing and channel forwarding of entries published to the two primary scpet rss feeds: [news](https://vss.scpet.si/vss/rss.php?sec=news) and [updates](https://vss.scpet.si/vss/rss.php?sec=obvestila).

## Requirements
- [feedparser](https://github.com/kurtmckee/feedparser) package
- [ookami](https://github.com/tainn/ookami) package

## Usage
Saving of exhausted links should be made to a local `links.log` file, located in the `data` directory.

### Opt `1.0` : Direct run
Webhook url should be specified separately in a local `hook.txt` file, located in the `data` directory.

```sh
./fetcher.py
```

### Opt `2.0` : Docker
Webhook should be passed as an environment variable `HOOK` by specifying it in a separate `.env` file. This is done in order to separate sensitive information from the rest. `.env` should be located in the same directory as `docker-compose.yml`.

```sh
HOOK=<webhook>
```

Build and run a container as a daemon, as well as stop and remove it
```sh
docker-compose up -d

docker-compose down
```
