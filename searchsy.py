import requests
import json

r = requests.get('https://openapi.etsy.com/v2/listings/trending?api_key=uyvwtl04yi98duy546afittr&page=1')
print "Response Code:", r.status_code

decoded = json.loads(r.text)

for item in decoded['results']:
    print "Title of listing", item['title']
    for mytags in item['tags']:
        print json.dumps(mytags, sort_keys=True, indent=4, separators=(',', ': '))

#print json.dumps(decoded['results'], sort_keys=True, indent=4, separators=(',', ': '))
