# Engineer Project

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
```
Define your settings:

```
$ cd gifter
$ touch local_settings.py
# open settings.py and change it
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
