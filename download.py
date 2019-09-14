from flickrapi import FlickrAPI
from urllib.request import urlretrieve
from pprint import pprint
from dotenv import load_dotenv
import os
import time
import sys

load_dotenv()
FLICKR_API_KEY = os.environ['FLICKR_API_KEY']
FLICKR_API_SECRET_KEY = os.environ['FLICKR_API_SECRET_KEY']

key = FLICKR_API_KEY
secret = FLICKR_API_SECRET_KEY
wait_time = 1

animal_name = sys.argv[1]
save_dir = './' + animal_name

flickr = FlickrAPI(key, secret, format='parsed-json')
result = flickr.photos.search(
    text=animal_name,
    per_page=400,
    media='photos',
    sort='relevance',
    safe_search=1,
    extras='url_q, licence'
)

photos = result['photos']

for i, photo in enumerate(photos['photo']):
    url_q = photo['url_q']
    file_path = save_dir + '/' + photo['id'] + '.jpg'
    if os.path.exists(file_path):
        continue
    urlretrieve(url_q, file_path)
    time.sleep(wait_time)
