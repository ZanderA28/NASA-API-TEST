from io import BytesIO
import json
import requests
from PIL import Image
from datetime import date

api_key = "UHw0k91LsqKb3YnDxbRpmexNgcAHcfy4q6I3Pv6I"

URL_APOD = "https://api.nasa.gov/planetary/apod"
today = date.today()
params = {
    'api_key':api_key,
    'date':today,
    'hd':'True'
}
response = requests.get(URL_APOD,params=params).json()
imageURL = response['url']
imageResponse = requests.get(imageURL)
img = Image.open(BytesIO(imageResponse.content))
img.show()
