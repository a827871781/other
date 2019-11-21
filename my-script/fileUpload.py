#!/usr/bin/python3
# encoding: utf-8
import requests
from PIL import ImageGrab
from PIL import Image
import uuid
import os
import json


def main():
    url = 'https://sm.ms/api/upload'

    img = ImageGrab.grabclipboard()
    uuid_str = str(uuid.uuid1())
    file_pash = '/Users/syz/Documents/java-notes/Python/' + uuid_str + '.png'


    if isinstance(img, Image.Image):
        img.save(file_pash, 'png')
    else:
        strA ="当前剪切板内的不是图片，请复制/截图后，再执行。"
        result = {"items": [{"title": strA}]}
        print(json.dumps(result))
        return

    file_obj = open(file_pash, 'rb')
    # file_obj = open('/Users/syz/Desktop/a1.png', 'rb')
    files = {'smfile': file_obj}
    r = requests.post(url, data=None, files=files)

    import pyperclip
    the_json = json.loads(r.text)
    msg = ''
    if the_json['success']:
        pyperclip.copy( the_json["data"]["url"])
        mk = '![%s](%s )' % (uuid_str, the_json["data"]["url"])
        pyperclip.copy(mk)
        msg = {"items": [{"title": mk}]}

    else:
        pyperclip.copy(the_json['message'])
        msg = the_json['message']
        msg = {"items": [{"title": msg}]}

    os.remove(file_pash)
    print(json.dumps(msg))



if __name__ == "__main__":
   main()
