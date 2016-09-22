import requests
import json

r = requests.get('https://openapi.etsy.com/v2/listings/trending?api_key=uyvwtl04yi98duy546afittr&offset=400&limit=50')
#print "Response Code:", r.status_code
#decoded = json.loads(r.text)
decoded = json.loads(r.text)
keywords = []
wordlist = []
wordfreq = []

for item in decoded['results']:
    #print "Title of listing", item['title']
    for mytags in item['tags']:
        #make lowercase and add to keywords list
        keywords.append(mytags.lower())
#change unicode to ASCII. also .encode("ascii", "ignore") is to force removal of
#of the BOM unicode stuff.
wordlist = [str(unicodes.encode("ascii", "ignore")) for unicodes in keywords]

print keywords
#print json.dumps(decoded['results'], sort_keys=True, indent=4, separators=(',', ': '))

def makeDict (wordlist):
    wordfreq = [wordlist.count(p) for p in wordlist]
    mydict = dict(zip(wordlist,wordfreq))
    #sorteddict = sorted(mydict.keys())

    for key, value in sorted(mydict.iteritems(), key=lambda (k,v): (v,k), reverse=True):
        if value == 1:
            pass
        else:
            print "Keyword", key, "Freq", value

        #list.append("Count:", value, "Keyword:", key)
    #return list

makeDict(wordlist)
