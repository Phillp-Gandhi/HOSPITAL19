import json, httplib2

def getCoordinates(location):

    google_api_key = "AIzaSyAhGakWBJQX7z8zDF0RqLEbjUMCysxdwBo"
    locationString = location.replace(" ", "+")
    url = ('https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s'% (locationString, google_api_key))
    h = httplib2.Http()
    response, content = h.request(url, 'GET')
    result = json.loads(content)
	#return result
    latitude = result['results'][0]['geometry']['location']['lat']
    longitude = result['results'][0]['geometry']['location']['lng']
    return latitude,longitude