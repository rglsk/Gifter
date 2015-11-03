from core.config import LLDA_RESULTS_DIRECTORY

from gifter.api.ebay_api import EbayApi


def convert_hashtag_response(hashtags):
    new = [{'name': key, 'count': str(value)}
           for key, value in hashtags.iteritems()]
    return {'hashtags': new}


def generate_ebay_category():
    ebay_api = EbayApi()
    ebay_api.generate_category_hierarchy()


def get_category_from_filepath(file_path):
    return file_path.split('/')[-2]


def get_data_file_path(filename):
    return '/'.join([LLDA_RESULTS_DIRECTORY, filename])
