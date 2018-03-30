from geocode import getGeocodeLocation
import json
import httplib2
import config

import sys
import codecs
sys.stdout = codecs.getwriter('utf8')(sys.stdout)
sys.stderr = codecs.getwriter('utf8')(sys.stderr)

foursquare_client_id = config.foursquare_api_key
foursquare_client_secret = config.foursquare_secret


def findARestaurant(mealType,location):
	coordinates = getGeocodeLocation(location)
        url = ('https://api.foursquare.com/v2/venues/search?client_id=%s&client_secret=%s&v=20130815&ll=%s,%s&query=%s' % (foursquare_client_id, foursquare_client_secret, coordinates[0],coordinates[1], mealType))
        h = httplib2.Http()
        result = json.loads(h.request(url,'GET')[1])
        name = result['response']['venues'][0]['name']
        venue_id = result['response']['venues'][0]['id']
        street = result['response']['venues'][0]['location']['address']
        city = result['response']['venues'][0]['location']['city']
        country = result['response']['venues'][0]['location']['country']
        address =(street, city, country)
        url = ('https://api.foursquare.com/v2/venues/%s/photos?client_id=%s&client_secret=%s&v=20130815&limit=1' % (venue_id, foursquare_client_id, foursquare_client_secret))
        result = json.loads(h.request(url,'GET')[1])
        photo = result['response']['photos']['items'][0]['prefix']
        photo += '300x300'
        photo += result['response']['photos']['items'][0]['suffix']
        print (name,address,photo)
        return (name,address,photo)
if __name__ == '__main__':
	findARestaurant("Pizza", "Tokyo, Japan")
	findARestaurant("Tacos", "Jakarta, Indonesia")
	findARestaurant("Tapas", "Maputo, Mozambique")
	findARestaurant("Falafel", "Cairo, Egypt")
	findARestaurant("Spaghetti", "New Delhi, India")
	findARestaurant("Cappuccino", "Geneva, Switzerland")
	findARestaurant("Sushi", "Los Angeles, California")
	findARestaurant("Steak", "La Paz, Bolivia")
	findARestaurant("Gyros", "Sydney Australia")
