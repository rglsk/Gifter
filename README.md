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
```
