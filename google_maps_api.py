# Import API Key from file
from google_maps_credentials import APIKey

# Import libraries
import googlemaps
import csv

gmaps = googlemaps.Client(key=APIKey)
gmaps.distance_matrix(origins, destinations)
