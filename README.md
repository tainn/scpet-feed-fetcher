# scpet-rss
![Version](https://img.shields.io/badge/version-v1.0-blue)
![License](https://img.shields.io/badge/license-GPLv3-orange)

Automated discord webhook posting of entries published to the two primary scpet [news](https://vss.scpet.si/vss/rss.php?sec=news) and [updates](https://vss.scpet.si/vss/rss.php?sec=obvestila) rss feeds.

## Requirements
`scpet-rss` requires the [feedparser](https://github.com/kurtmckee/feedparser) and [ookami](https://github.com/tainn/ookami) packages in order to parse and manipulate discord webhook data respectively.

## Usage
- Webhook url should be specified separately in a local `hook.txt` file
- Saving of exhausted links should be made to a local `rss.txt` file
- `hook.txt` and `rss.txt` should be located in the same directory as the executable

## Direct run
```sh
cd /path/to/rss

chmod +x ./rss.py

./rss.py
```

## Docker

### Build and run
```sh
cd /path/to/rss

docker build --tag scpet-rss .

docker container run -d --rm scpet-rss
```

### Stop
```sh
docker container stop <NAME>
```

The daemon can be stopped (and removed due to the `--rm` option at run) by referencing either the `CONTAINER ID` or `NAME`, both of which can be accessed under the running containers list:
```sh
docker ps | grep -E "NAMES|scpet-rss"
```
