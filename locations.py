import yaml
import googlemaps
import ConfigParser, os

# get configuration file and settings.
config = ConfigParser.ConfigParser()
config.readfp(open('configuration.ini'))
API_KEY = config.get('settings', 'api_key')
DATA_FILE = config.get('settings', 'data_file')

# read data file
data = yaml.load(open(DATA_FILE))

#  load google maps api and query
gmaps = googlemaps.Client(key=API_KEY)

for row in data:
    name = row[0]
    address = row[1]
    
    # get geolocation with gmaps api.
    try:
        query = gmaps.geocode(address)
        result = query[0]
        lat = result['geometry']['location']['lat']
        lng = result['geometry']['location']['lng']
        print("{0},{1},{2}".format(name.strip(),lat,lng))
    
    # error handling.
    except googlemaps.exceptions.HTTPError as error:
        print error
