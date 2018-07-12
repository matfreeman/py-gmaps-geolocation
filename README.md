# py-gmaps-geolocation
A script to use the google maps api to get the geolocation coordinates from a set of postal addresses.

Requires a google maps api key at https://developers.google.com/console with the following google maps services:
- Directions API
- Distance Matrix API
- Elevation API
- Geocoding API
- Geolocation API
- Places API
- Roads API
- Time Zone API

## Data
Defined in locations.yml, with the format: [["name", "postal address"], ....]

## Configuration
Requires an api key specificed in configuration.ini