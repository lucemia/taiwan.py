import urllib2
import ast
import datetime

resp = urllib2.urlopen('https://api.meetup.com/Taipei-py/boards/8146082/discussions?&sign=true&key=67696b60237605c323f6649447f73').read()

resp_json = ast.literal_eval(resp)

get_dict = lambda dct, *keys: {key: dct[key] for key in keys}

def dicttomd(**post):
    content =  """---
layout:post.html
title:{}
tags:[sprint]
author:{}
type:event
---
{}
""".format(post["subject"],
           post["name"],
           post["body"])
    return content


for p in resp_json:
    post = get_dict(p, 'subject', 'body', 'created', 'updated')
    post['name'] = p['started_by']['name']

    t = datetime.datetime.fromtimestamp(int(post["created"])/1000).strftime('%Y-%m-%d_%H-%M-%S')

    filename = t+'.md'

    f = file(filename, "w")
    f.write(dicttomd(**post))
    f.close()
