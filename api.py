import json

import urllib2

def get_info(query):

    """create variable to store api key"""
    api_key = 'a9703581911908ceefc3f30cf655e06b'
    """url to look for movie info"""
    url = 'http://api.themoviedb.org/3/search/movie?api_key=' + api_key
    movie_title = query.replace(' ', '%20')
    final_url = url + "&query=" + movie_title.lower()
    """open url and create json file"""
    json_obj = urllib2.urlopen(final_url)
    data = json.load(json_obj)
    """return information about the movie"""
    return data

def get_title(query):

"""call function get_info with provided movie title and store data in variable"""  # NOQA
data = get_info(query)
"""loop through items in results dic"""
for key in data['results']:
        """look for a match with provided movie title"""
        if key['title'] == query:
            """return movie title if match found"""
            return key['title']

def get_poster(query):

"""call function get_info with provided movie title and store data in variable"""  # NOQA
data = get_info(query)
"""loop through items in results dic"""
for title in data['results']:
    """look for a match with provided movie title"""
    if title['title'] == query:
        """return poster image path if match found"""

            return "https://image.tmdb.org/t/p/w500/" + title['poster_path']