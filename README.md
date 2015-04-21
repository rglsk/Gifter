# Gifter

## Installation

Note: using `virtualenvwrapper`

```
$ mkvirtualenv gifter -a /path/to/gifter/
```
To use this virtualenv:
```
$ workon gifter
```

Install dependencies:
```
$ pip install -e .
$ python -m textblob.download_corpora lite
```

Define your settings:

```
$ cd gifter
$ touch local_settings.py
# open settings.py and change it
# open ebay.yaml and set tokens/ID's
```

## Crawling
```
$ crawl_tweets
```

## Running scripts:
```
$ python gifter/recipient.py
```

## Working with notebooks (only modeling!!)
```
$ ipython notebook .
```

## Setting up frontend stuff:
```
$ cd /path/to/static
$ sudo apt-get install npm

$ npm install
$ npm install -g bower
$ npm install -9 grunt-cli

```

## To run app in browser (default google-chrome):
```
$ cd /path/to/static
$ grunt serve

If there will be an error "/usr/bin/env: node: No such file or directory " then:
$ ln -s /usr/bin/nodejs /usr/bin/node
```
