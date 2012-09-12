import sys
from django.http import HttpResponse
from django.conf import settings
from django.db import connection, transaction
from datetime import timedelta, datetime
from django.template import Context, loader

#from collections import Counter

def alert():
    try:

        cursor = connection.cursor()
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        #cursor.execute("SELECT * FROM `event`")
        #cursor.execute("SELECT signature, ip_src,ip_dst,sig_name from event,iphdr,signature where iphdr.cid = event.cid and event.signature= signature.sig_id")
        cursor.execute("SELECT signature, ip_src,ip_dst from event,iphdr,signature where iphdr.cid = event.cid and event.signature= signature.sig_id")

        #cursor.execute("SELECT signature,ip_src,ip_dst,sig_name from event,iphdr,signature where event.timestamp < '2010-12-08 19:40:31' and iphdr.cid = event.cid and event.signature= signature.sig_id")
        rows = cursor.fetchall()
        return rows
    except Exception, e:
        print str(e)

#def ip2num(ip):
  
def num2ip(num):
    D = num % 256
    C = (num / 256) % 256
    B = (num / 256**2) % 256
    A = (num / 256**3) % 256
    ip = str(A)+ "." + str(B)+ "." + str(C)+ "."+ str(D)
    return ip

def ip2num(ip):
    ipl = ip.split('.')
    num = 256**3 * int(ipl[0]) + 256**2 * int(ipl[1]) + 256 * int(ipl[2]) + int(ipl[3]) 
    return num

def home(request):
    try:
        test = ((1,2),(1,3),(1,2),(1,4))
        #print set(test)
        #print Counter(test)


        alerts = alert()
        sd = []
        
        count = {}
        for k in alerts:
            if k in count.keys():
                sd.append((num2ip(k[1]), num2ip(k[2])))
                count[k] = count[k] + 1
            else:
                sd.append((num2ip(k[1]), num2ip(k[2])))
                count[k] = 1

        count2 = {}
        for k,v in count.iteritems():
            kk = (num2ip(k[1]),num2ip(k[2]))
            if kk in count2.keys():
                count2[kk][k[0]] = v
                count2[kk]['t'] = count2[kk]['t'] + v
            else:
                count2[kk] = {}
                count2[kk]['t'] = 0
                count2[kk][k[0]] = v
                count2[kk]['t'] = count2[kk]['t'] + v

        for k,v in count2.iteritems():
            print k,v

        
        #print sd
        setsd = set(sd)
        #print setsd
        t = loader.get_template('index.html')
        c = Context({
            'results': count2,
        })
        return HttpResponse(t.render(c))
    
    
        #return HttpResponse("<pre> this is  page</pre>" )
    except Exception, e:
        print str(e)
        return HttpResponse("<pre> home page load fail</pre>")