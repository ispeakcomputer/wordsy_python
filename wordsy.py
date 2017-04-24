import requests
import json

class Etsy:
    def gettrendingresponse(self):
        r = requests.get('https://openapi.etsy.com/v2/listings/trending?api_key=uyvwtl04yi98duy546afittr&limit=250')
        #print "Response Code:", r.status_code
        iterkeywords = []
        keywords = json.loads(r.text)

        for item in keywords['results']:
            #print "Title of listing", item['title']
            if 'tags' in item:
                for mytags in item['tags']:
                    #make lowercase and add to keywords list
                    iterkeywords.append(mytags.lower())
        return iterkeywords

class Words:
    def killunicode(self, iw):

        #change unicode to ASCII. also .encode("ascii", "ignore") is to force removal of
        #of the BOM unicode stuff.
        wordlist = []
        wordlist = [str(unicodes.encode("ascii", "ignore")) for unicodes in iw]
        return wordlist

    def printdict(self, wl):
        #count phrase freq
        wordfreq = [wl.count(p) for p in wl]
        #make the finished dict to print from
        mydict = dict(zip(wl,wordfreq))
        #make our list
        for key, value in sorted(mydict.iteritems(), key=lambda (k,v): (v,k), reverse=True):
            if value <= 1:
                pass
            else:
                print key, "Freq", value

if __name__ == '__main__':
    keywords = Etsy()
    ourwords = Words()

    ourkeywords = keywords.gettrendingresponse()
    cleanwords = ourwords.killunicode(ourkeywords)
    ourwords.printdict(cleanwords)
