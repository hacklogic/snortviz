
Number = 168298629
def num2ip(num):
    D = Number % 256
    C = (Number / 256) % 256
    B = (Number / 256**2) % 256
    A = (Number / 256**3) % 256
    ip = str(A)+ "." + str(B)+ "." + str(C)+ "."+ str(D)
    return ip
def ip2num(ip):
    ipl = ip.split('.')
    num = 256**3 * int(ipl[0]) + 256**2 * int(ipl[1]) + 256 * int(ipl[2]) + int(ipl[3]) 
    return num
    
#print num2ip(168298629)
print ip2num('10.8.8.133')