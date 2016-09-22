import requests
import json

def gettrendingresponse():
    r = requests.get('https://openapi.etsy.com/v2/listings/trending?api_key=uyvwtl04yi98duy546afittr&limit=50')
    #print "Response Code:", r.status_code
    iterkeywords = []
    keywords = json.loads(r.text)
    for item in keywords['results']:
        #print "Title of listing", item['title']
        for mytags in item['tags']:
            #make lowercase and add to keywords list
            iterkeywords.append(mytags.lower())
    killunicode(iterkeywords)

def killunicode(iw):

    #change unicode to ASCII. also .encode("ascii", "ignore") is to force removal of
    #of the BOM unicode stuff.
    wordlist = []
    wordlist = [str(unicodes.encode("ascii", "ignore")) for unicodes in iw]
    printdict(wordlist)

    #print json.dumps(decoded['results'], sort_keys=True, indent=4, separators=(',', ': '))

def printdict(wl):
    #count phrase freq
    wordfreq = [wl.count(p) for p in wl]
    #make the finished dict to print from
    mydict = dict(zip(wl,wordfreq))

    for key, value in sorted(mydict.iteritems(), key=lambda (k,v): (v,k), reverse=True):
        if value == 1:
            pass
        else:
            print key, "Freq", value

def main():
    gettrendingresponse()

main()
