#!/usr/bin/python3

import requests

URL= "http://api.open-notify.org/astros.json"
def main():
    # requests.get() sends GET request to the URL
    # .json() strips JSON off the response and translates into Python!
    resp= requests.get(URL).json()

print("The List Of Aastronauts")

resp= requests.get(URL).json()
# the API gives us a headcount of people in space
print(resp["number"])

# the value of the key "people" is a list of dictionaries, one dictionary per astronaut
listofdicts= resp["people"]

# loop over each dictionary, and print out the values of "name" and "craft" from each one
for astrodict in listofdicts:
    print(astrodict["name"])
    print(astrodict["craft"])
main()


