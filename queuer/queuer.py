
import requests
import re
import json
from screenshoter import take_screenshot
from screenshoter import delete_screenshot

def get_queue():
    print("checking queue...")
    name = take_screenshot()
    delete_screenshot(name)
    try:
        jsonRes = json.loads(ocr_space_file(name))
        parsedText = jsonRes['ParsedResults'][0]['ParsedText']
        queue = re.search("\d+", parsedText).group(0)
        print("queue is:")
        print(queue)
        return queue
    except:
        print("Error: could not parse screenshot")

def ocr_space_file(filename, overlay=True, api_key='9c1888603288957', language='eng'):
    payload = {'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               }
    with open(filename, 'rb') as f:
        r = requests.post('https://api.ocr.space/parse/image',
                          files={filename: f},
                          data=payload,
                          )
    return r.content.decode()


def ocr_space_url(url, overlay=True, api_key='9c1888603288957', language='eng'):
    payload = {'url': url,
               'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               }
    r = requests.post('https://api.ocr.space/parse/image',
                      data=payload,
                      )
    return r.content.decode()