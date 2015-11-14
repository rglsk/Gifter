from os import path

import pandas as pd

from core.config import DATA_DIRECTORY


def get_ebay_categories_mapping():
    df = pd.read_json(path.join(DATA_DIRECTORY, 'category_mapping.json'))

    ebay_categories = df[['CategoryName', 'CategoryName2']].values.tolist()
    return dict(
        zip(df['OurCategoryName'],
            map(lambda cats:
                [cat for cat in cats if not pd.isnull(cat)], ebay_categories))
    )
