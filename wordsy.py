import requests
import json

r = requests.get('https://openapi.etsy.com/v2/listings/trending?api_key=uyvwtl04yi98duy546afittr&category_id=68887482&page=1')
#print "Response Code:", r.status_code
#decoded = json.loads(r.text)
decoded = json.loads(r.text)
keywords = []

for item in decoded['results']:
    #print "Title of listing", item['title']
    for mytags in item['tags']:
        #print mytags
        keywords.append(mytags.lower())

#Make all lowercase
#lowerwords = [words.lower() for words in keywords]

        #print json.dumps(mytags, sort_keys=True, indent=4, separators=(',', ': '))

#print json.dumps(decoded['results'], sort_keys=True, indent=4, separators=(',', ': '))

#change unicode to ASCII. also .encode("ascii", "ignore") is to force removal of
#of the BOM unicode stuff.
keywords = [str(unicodes.encode("ascii", "ignore")) for unicodes in keywords]
print keywords

for word in keywords:
    print word
