# Gifter

## Requirements:
 * [Python 2.7](https://www.python.org/download/releases/2.7/)
 * [virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/)
 * [Flask](http://flask.pocoo.org/)
 * [Postgresql](http://www.postgresql.org.pl/)
 * [Amazon Web Service](http://aws.amazon.com/)
 * [eBay developers](go.developer.ebay.com)

## Installation

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

## Setting up developer enviroment

Note: Remember to set up passwords.

### Setting up enviroment variables:
```
$ source ./scripts/setup_environ.sh
```

### Setting up local database:
```
$ ./gifter/db/init_db.sh
```

## Scripts:

* crawl_tweets
* crawl_suggested_tweets
* preprocess_suggested
* remove_preprocessed
* generate_ebay_category
* report
* stats

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
$ npm install -g grunt-cli

```

## To run app in browser (default google-chrome):
```
$ cd /path/to/static
$ grunt serve

If there will be an error "/usr/bin/env: node: No such file or directory " then:
$ ln -s /usr/bin/nodejs /usr/bin/node
```

## Example API usage:
```
curl -X POST http://127.0.0.1:5000/api/items/PiotrRogulski/
```