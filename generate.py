import json
import urllib2
import os

def cls():
    os.system(['clear','cls'][os.name == 'nt'])

github_login = raw_input('Please enter your GitHub login: ')

cls()

github_data = urllib2.urlopen('https://api.github.com/users/'+github_login+'/repos')
decoded_json = json.load(github_data)

print "Name: "+decoded_json[0]["name"]
print "Description: "+decoded_json[0]["description"]
print "Language: "+decoded_json[0]["language"] 
