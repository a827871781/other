#!/usr/bin/python3
# encoding: utf-8
import json
import sys
import pyperclip
def main():
    str = sys.argv[1]
    str1 = str.replace('[','{')
    str1 = str1.replace(']','}')
    result = {"items": [{"title": str1},{"title":str}]}
    print(json.dumps(result))
    pyperclip.copy(str1)


if __name__ == '__main__':
    main()