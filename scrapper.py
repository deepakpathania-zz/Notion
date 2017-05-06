########### Python 2.7 #############
import httplib, urllib, base64,json,time

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': '44d7169c2f9546ea89f4d74a320d4fbc',
}

offset = 0
for i in range(1,21):
    params = urllib.urlencode({
        # Request parameters
        'q': 'aadhar',
        'count': '100',
        'offset': offset,
        'mkt': 'en-In',
        'safeSearch': 'Moderate',
    })
    try:
        conn = httplib.HTTPSConnection('api.cognitive.microsoft.com')
        time.sleep(3)
        conn.request("GET", "/bing/v5.0/news/search?%s" % params, "{body}", headers)
        offset += 100
        response = conn.getresponse()
        data = response.read()
        with open("json/"+str(i)+"data.json",'w') as f: 
            json.dump(data, f, ensure_ascii=False)
        print i
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################
