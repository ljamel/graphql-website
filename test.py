import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key='AIzaSyBQgvWjC1PYovGZ_cf3L3NRksw2Xp8mN9Y')

# Request directions via public transit
now = datetime.now()

directions_results = gmaps.directions("paris",
                                      "lyon",
                                      mode="driving",
                                      departure_time=now)


print(directions_results)