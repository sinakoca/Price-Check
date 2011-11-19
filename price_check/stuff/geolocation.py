import json, urllib, urllib2, socket

class IPInfo() :
    def __init__(self, apikey) :
        self.apikey = apikey
    def GetIPInfo(self, baseurl, ip=None, timezone=False) :
        """Same as GetCity and GetCountry, but a baseurl is required.  This is for if you want to use a different server that uses the the php scripts on ipinfodb.com."""
        passdict = {"output":"json", "key":self.apikey}
        if ip :
            try :
                passdict["ip"] = socket.gethostbyaddr(ip)[2][0]
            except : passdict["ip"] = ip
        if timezone :
            passdict["timezone"] = "true"
        else :
            passdict["timezone"] = "false"
        urldata = urllib.urlencode(passdict)
        url = baseurl + "?" + urldata
        urlobj = urllib2.urlopen(url)
        data = urlobj.read()
        urlobj.close()
        datadict = json.loads(data)
        return datadict

    def GetCity(self, ip=None, timezone=False) :
        """Gets the location with the context of the city of the given IP.  If no IP is given, then the location of the client is given.  The timezone option defaults to False, to spare the server some queries."""
        baseurl = "http://api.ipinfodb.com/v2/ip_query.php"
        return self.GetIPInfo(baseurl, ip, timezone)

    def GetCountry(self, ip=None, timezone=False) :
        """Gets the location with the context of the country of the given IP.  If no IP is given, then the location of the client is given.  The timezone option defaults to False, to spare the server some queries."""
        baseurl = "http://api.ipinfodb.com/v2/ip_query_country.php"
        return self.GetIPInfo(baseurl, ip, timezone)

KEY = '9a492351d85daba42ec4a458aee0491fffa01a9d157efc89e1a6ecc28e238593'
ip_info = IPInfo(KEY)

def get_city(ip):
    result = ip_info.GetCity(ip)
    return result.get(u'City')
