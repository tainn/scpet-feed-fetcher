# scpet-rss
![Version](https://img.shields.io/badge/version-v1.0-blue)
![License](https://img.shields.io/badge/license-GPLv3-orange)

Automated discord webhook posting of entries published to the two primary scpet news and updates rss feeds.

## Requirements
scpet-rss requires the [feedparser](https://github.com/kurtmckee/feedparser) and [ookami](https://github.com/tainn1/ookami) packages in order to parse and manipulate discord webhook data respectively.

## Usage
- Webhook url should be specified separately in a local `hook.txt` file
- Saving of exhausted links should be made to a local `rss.txt` file
- `hook.txt` and `rss.txt` should be located in the same directory as the executable

## Run
```sh
cd /path/to/dir

chmod +x ./rss.py

./rss.py
```
