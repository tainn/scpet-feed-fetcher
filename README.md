# scpet-rss
![Version](https://img.shields.io/badge/version-v1.2-blue)
![License](https://img.shields.io/badge/license-GPLv3-orange)

Automated discord webhook posting of entries published to the two primary scpet [news](https://vss.scpet.si/vss/rss.php?sec=news) and [updates](https://vss.scpet.si/vss/rss.php?sec=obvestila) rss feeds.

## Requirements
`scpet-rss` requires the [feedparser](https://github.com/kurtmckee/feedparser) and [ookami](https://github.com/tainn/ookami) packages in order to parse and manipulate discord webhook data respectively.

## Usage
- Saving of exhausted links should be made to a local `rss.txt` file
- `rss.txt` should be located in the same directory as the executable

## Direct run
Webhook url should be specified separately in a local `hook.txt` file. `hook.txt` should be located in the same directory as the executable.

```sh
cd /path/to/rss

chmod +x ./rss.py

./rss.py
```

## Docker
Webhook should be passed as an environment variable `HOOK` by specifying it in a separate `.env` file. This is done in order to separate sensitive information from the rest. `.env` should be located in the same directory as `docker-compose.yml`.

```sh
HOOK=<webhook>
```

### Build and run
```sh
cd path/to/repository

docker-compose up -d
```

### Stop and remove
```sh
cd path/to/repository

docker-compose down
```
