#!/usr/bin/python3
# encoding: utf-8
import json
import pyperclip
def main():
    str = pyperclip.paste()
    if not'[' in str and not']' in str:
        result = {"items": [{"title": "当前剪切板内字符串没有 [ / ] ,请重新复制." }]}
        print(json.dumps(result))
        return

    str1 = str.replace('[','{')
    str1 = str1.replace(']','}')
    result = {"items": [{"title": str1},{"title":str}]}
    print(json.dumps(result))
    pyperclip.copy(str1)

if __name__ == '__main__':
    main()