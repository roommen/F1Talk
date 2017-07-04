from amazon.api import AmazonAPI
# import bottlenose.api
# import os

AMAZON_ACCESS_KEY = ""
AMAZON_SECRET_KEY = ""
# AMAZON_ASSOC_TAG = ""
AMAZON_ASSOC_TAG = ""

amazon = AmazonAPI(AMAZON_ACCESS_KEY, AMAZON_SECRET_KEY, AMAZON_ASSOC_TAG, region="IN")
# product = amazon.lookup(ItemId='B00UVIU1PA')
# print(product.title)
products = amazon.search(Keywords='kindle', SearchIndex='All')
for i, product in enumerate(products):
    print("{0}. '{1}'".format(i, product.title))
    print("{0}. {1}.format(i, product.large_image_url")
