
import requests
import re
import json

def get_queue(imageData):
    print("checking queue...")
    jsonRes = json.loads(ocr_space_file(imageData))
    parsedText = jsonRes['ParsedResults'][0]['ParsedText']
    queue = re.search("\d+", parsedText).group(0)
    print("queue is:")
    print(queue)
    return queue

image = "hej";

def ocr_space_file(overlay=True, api_key='9c1888603288957', language='eng'):
    payload = {'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               'base64Image': 'data:image/png;base64,' + image,
               }

    r = requests.post('https://api.ocr.space/parse/image', data=payload)
    return r.content.decode()

get_queue('/Users/gabrielvilen/Downloads/queue.jpg')