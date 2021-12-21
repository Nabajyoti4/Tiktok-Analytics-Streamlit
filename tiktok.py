# importing tiktok python sdk
from TikTokApi import TikTokApi as tiktok
import json
from helpers import process_results
import pandas as pd
import sys

def get_data(hashtag = 'ai'):
    # get cokkie data
    verifyFp = ""
    api = tiktok.get_instance(custom_verifyFp=verifyFp, use_test_endpoints=True)

    # get data by hastatg
    # ai, python etc
    trending = api.by_hashtag(hashtag)

    # process data
    flattened_data = process_results(trending)

    # convert to preprocesses data to df
    df = pd.DataFrame.from_dict(flattened_data)
    df.to_csv('tiktokdata.csv')

if __name__ == '__main__':
    get_data(sys.argv[1])