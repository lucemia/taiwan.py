Introduction
---

[台灣的Python社群, 網站source](http://taiwan-py.appspot.com/)

Requirement
---

1. [python 2.7](http://www.python.org/download/releases/2.7/)
1. [mynt==2.3](http://mynt.mirroredwhite.com/)
2. [jinja2](http://jinja.pocoo.org/docs/)
3. [google appengine sdk](https://developers.google.com/appengine/downloads) (option) 

Build
---

1. `pip install mynt==2.3`
2. `git clone http://github.com/lucemia/taiwan.py.git`
3. `cd taiwan.py`
4. `mynt gen -f src/ build/`   

Run
---

run by mynt

`mynt serve build`


upload to appengine

1. `edit app.yaml with your appspot`
2. `appcfg.py update .`


![alt tag](https://tw.pycon.org/2015apac/images/Logo_red_1280.svg)
####Tutorials May 30-31, Conference June 5-7, Sprints June 8, Taipei, Taiwan
Mark your calendar now and stay up to date on the must-attend event in 2015. Join the biggest Python conference in ASIA. 
To find more -> 'https://tw.pycon.org/2015apac/'
