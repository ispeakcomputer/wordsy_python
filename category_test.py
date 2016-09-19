import requests
import json

r = requests.get('https://www.openapi.etsy.com/v2/taxonomy/categories?api_key=uyvwtl04yi98duy546afittr')
print "Response Code:", r.status_code
decoded = json.loads(r.text)
print decoded
print json.dumps(decoded, sort_keys=True, indent=4, separators=(',', ': '))
