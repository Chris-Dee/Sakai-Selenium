# Sakai-Selenium

To run server, go to Sakai-Selenium/myproject and run
```python
sudo python manage.py runserver 0.0.0.0:80
```
required dependencies are Python 2.7, Django 1.8, Selenium and firefox


To generate a script, download the firefox extension selenium-IDE, and record your clicks and actions

Your script must be uploaded from the Selenium IDE (or using the same import structure, as listed below), to help ensure that harmful code snippets are not accidentally run.
```python
from selenium import ....
from selenium import ....
import unittest, time, re...
```

If you want the URL your script is tested on to be variable (i.e. they can be changed on the frontend), follow the steps below. 
Otherwise, please put the URL your script is running on in the title of the script!

inside your script, before uploading, add the lines:
```python
url = sys.argv[1]
del sys.argv[1]
```
and replace the line:
```python
self.base_url = "http://xxx.xxx/"
```
with 
```python
self.base_url = url
```


Your script should then be good to upload. 

