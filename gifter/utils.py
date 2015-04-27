from gifter.api.ebay_api import EbayApi


def convert_hashtag_response(hashtags):
    new = [{'name': key, 'count': str(value)}
           for key, value in hashtags.iteritems()]
    return {'hashtags': new}


def generate_ebay_category():
    ebay_api = EbayApi()
    ebay_api.generate_category_hierarchy()
