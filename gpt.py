import requests
out=requests.get('https://google.com') 
print(out.content)