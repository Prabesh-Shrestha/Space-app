from tkinter import *
from PIL import ImageTk, Image
import requests
import math
root = Tk()
root.title("Orbital Satellite Data Collector (OSDC)")



spacer1 = Label(root, text = "", padx = 300)
satallite = Label(root, text = "Satallite")

def abouts():
    abo = Toplevel()
    abo.title("About")
    a = Label(abo, text = "Team Alpha Centauri includes the members of young and energetic high scholars ").grid(row = 0, column = 0)
    b = Label(abo, text = "having enthusiasts in coding and having a very great interest in the exploration of ").grid(row = 1, column = 0)
    c = Label(abo, text = "space. The way we participants had worked together in a team to compete for global ").grid(row = 2, column = 0)
    d = Label(abo, text = "challenges bringing in perspectives and insides from various space data which was ").grid(row = 3, column = 0)
    e = Label(abo, text = "an experience NASA space app organizers can share proudly. We also took this ").grid(row = 4, column = 0)
    f = Label(abo, text = "event as an opportunity to link young students and professionals with electronics ").grid(row = 5, column = 0)
    g = Label(abo, text = "and computing background to establish linkages with technologists as well as ").grid(row = 6, column = 0)
    h = Label(abo, text = "environmentalists by using data that can be made available and come up with").grid(row = 7, column = 0)
    i = Label(abo, text = "prototypes of space applications that can even be scaled up. Actually, we were ").grid(row = 8, column = 0)
    j = Label(abo, text = "provided open opportunities to create space application with which we are benefited").grid(row = 9, column = 0)
    k = Label(abo, text = "a lot and our experiences in coding and making apps were upgraded too. We choose").grid(row = 10, column = 0)
    l = Label(abo, text = "the challenge Orbital Sky because as a task we were assigned was wonderful that to ").grid(row = 11, column = 0)
    m = Label(abo, text = "develop a method to improve public knowledge of satellites of Earth’s orbit that ").grid(row = 12, column = 0)
    n = Label(abo, text = "supports day to day life of people on the ground with an eye towards driving user  ").grid(row = 13, column = 0)
    o = Label(abo, text = "engagement, enthusiasm and satellite exploration using an application.  ").grid(row = 14, column = 0)

    return

def ref():
    refe = Toplevel()
    refe.title("Refrence")
    ref1 = Label(refe, text ="https://api.nasa.gov/").grid(row = 0, column = 0, padx = 100)
    ref2 = Label(refe, text ="https://nssdc.gsfc.nasa.gov/").grid(row = 1, column = 0)




def GEOS6(IDs):
    GEOS6 = Toplevel()
    spacer2 = Label(GEOS6, text = "", pady = 100)
    GEOS6.title("GEOS6")
    a = Label(GEOS6, text = "hello this is the place where the data of GEOS6 is stored").grid(row = 0, column = 0)
    Location =requests.get('https://ipinfo.io')
    datauser = Location.json()
    gpsloc = datauser['loc']
    aa = Label(GEOS6, text = gpsloc).grid(row = 1, column = 0) # user location OUTPUT
    Xl,Yl = (gpsloc.split(','))
    xl = float(Xl)
    yl = float(Yl)
    xl=int(xl)
    yl=int(yl)

    url1 = ("https://uphere-space1.p.rapidapi.com/satellite/")
    url2 = IDs
    url3 =("/location")
    url= url1+url2+url3
    querystring = {"units":"imperial","lat":"47.6484346","lng":"122.374199"}
    headers = {
        'x-rapidapi-host': "uphere-space1.p.rapidapi.com",
        'x-rapidapi-key': "your api key"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    dataiss = response.json()
    position = dataiss["coordinates"]
    position= str(position)
    d = position.replace("[","")
    f = d.replace("]","")
    x,y = (f.split(','))
    x =float(x)
    y =float(y)
    x=int(x)
    y=int(y)
    #determining the distance and direction of ISS

    Dx = (x)-(xl)
    Dy = (y)-(yl)
    D2 =Dx**2 - Dy**2
    D2X = math.sqrt(D2**2)
    GPSDISTANCE = math.sqrt(D2X)
    DISTANCE = int(GPSDISTANCE*111)
    dis = str(DISTANCE)
    distance = Label(GEOS6, text = dis + "km").grid(row = 2, column = 0)
    print(DISTANCE,'km')#this is Distance from user of Satellite OUTPUT
    rate = ((Dy/Dx)/math.pi)
    xis = math.atan(rate)
    angle= math.degrees(xis)
    if xl >= x :
        long='W'
    elif xl << x :
        long= 'E'
    if yl >= y :
        lat= 'N'
    elif yl << y :
        lat= 'S'
    ang = str(angle)
    dir = Label(GEOS6, text = "direction  " + ang +lat + long).grid(row = 3, column = 0)
    print("Direction",angle,lat,long)# this is the direction OUTPUT

    # determining the visibility from the user location 
    Alt= dataiss["height"]
    Alt = int(Alt)
    alti = str(Alt)
    
    alt = Label(GEOS6, text = "alt:"+alti).grid(row = 4, column = 0)
    print(Alt)

    ELEVATION = math.atan(Alt/DISTANCE)
    Sight =math.degrees(ELEVATION)
    sli = str(Sight)
    slight = Label(GEOS6, text = "sight"+sli).grid(row = 4, column = 0)
    print(Sight) # this is the angle of elevation OUTPUT






def GOES12(IDs):

    GOES12 = Toplevel()
    spacer2 = Label(GOES12, text = "", pady = 100)
    GOES12.title("GOES12")
    a = Label(GOES12, text = "hello this is the place where the data of GOES12 is stored").grid(row = 0, column = 0)
    Location =requests.get('https://ipinfo.io')
    datauser = Location.json()
    gpsloc = datauser['loc']
    aa = Label(GOES12, text = gpsloc).grid(row = 1, column = 0) # user location OUTPUT
    Xl,Yl = (gpsloc.split(','))
    xl = float(Xl)
    yl = float(Yl)
    xl=int(xl)
    yl=int(yl)

    url1 = ("https://uphere-space1.p.rapidapi.com/satellite/")
    url2 = IDs
    url3 =("/location")
    url= url1+url2+url3
    querystring = {"units":"imperial","lat":"47.6484346","lng":"122.374199"}
    headers = {
        'x-rapidapi-host': "uphere-space1.p.rapidapi.com",
        'x-rapidapi-key': "your api key"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    dataiss = response.json()
    position = dataiss["coordinates"]
    position= str(position)
    d = position.replace("[","")
    f = d.replace("]","")
    x,y = (f.split(','))
    x =float(x)
    y =float(y)
    x=int(x)
    y=int(y)
    #determining the distance and direction of ISS

    Dx = (x)-(xl)
    Dy = (y)-(yl)
    D2 =Dx**2 - Dy**2
    D2X = math.sqrt(D2**2)
    GPSDISTANCE = math.sqrt(D2X)
    DISTANCE = int(GPSDISTANCE*111)
    dis = str(DISTANCE)
    distance = Label(GOES12, text = dis + "km").grid(row = 2, column = 0)
    print(DISTANCE,'km')#this is Distance from user of Satellite OUTPUT
    rate = ((Dy/Dx)/math.pi)
    xis = math.atan(rate)
    angle= math.degrees(xis)
    if xl >= x :
        long='W'
    elif xl << x :
        long= 'E'
    if yl >= y :
        lat= 'N'
    elif yl << y :
        lat= 'S'
    ang = str(angle)
    dir = Label(GOES12, text = "direction  " + ang +lat + long).grid(row = 3, column = 0)
    print("Direction",angle,lat,long)# this is the direction OUTPUT

    # determining the visibility from the user location 
    Alt= dataiss["height"]
    Alt = int(Alt)
    alti = str(Alt)
    
    alt = Label(GOES12, text = "alt:"+alti).grid(row = 4, column = 0)
    print(Alt)

    ELEVATION = math.atan(Alt/DISTANCE)
    Sight =math.degrees(ELEVATION)
    sli = str(Sight)
    slight = Label(GOES12, text = "sight"+sli).grid(row = 4, column = 0)
    print(Sight) # this is the angle of elevation OUTPUT





def GOES2(IDs):

    GOES2 = Toplevel()
    spacer2 = Label(GOES2, text = "", pady = 100)
    GOES2.title("GOES2")
    a = Label(GOES2, text = "hello this is the place where the data of GOES2 is stored").grid(row = 0, column = 0)
    Location =requests.get('https://ipinfo.io')
    datauser = Location.json()
    gpsloc = datauser['loc']
    aa = Label(GOES2, text = gpsloc).grid(row = 1, column = 0) # user location OUTPUT
    Xl,Yl = (gpsloc.split(','))
    xl = float(Xl)
    yl = float(Yl)
    xl=int(xl)
    yl=int(yl)

    url1 = ("https://uphere-space1.p.rapidapi.com/satellite/")
    url2 = IDs
    url3 =("/location")
    url= url1+url2+url3
    querystring = {"units":"imperial","lat":"47.6484346","lng":"122.374199"}
    headers = {
        'x-rapidapi-host': "uphere-space1.p.rapidapi.com",
        'x-rapidapi-key': "your api key"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    dataiss = response.json()
    position = dataiss["coordinates"]
    position= str(position)
    d = position.replace("[","")
    f = d.replace("]","")
    x,y = (f.split(','))
    x =float(x)
    y =float(y)
    x=int(x)
    y=int(y)
    #determining the distance and direction of ISS

    Dx = (x)-(xl)
    Dy = (y)-(yl)
    D2 =Dx**2 - Dy**2
    D2X = math.sqrt(D2**2)
    GPSDISTANCE = math.sqrt(D2X)
    DISTANCE = int(GPSDISTANCE*111)
    dis = str(DISTANCE)
    distance = Label(GOES2, text = dis + "km").grid(row = 2, column = 0)
    print(DISTANCE,'km')#this is Distance from user of Satellite OUTPUT
    rate = ((Dy/Dx)/math.pi)
    xis = math.atan(rate)
    angle= math.degrees(xis)
    if xl >= x :
        long='W'
    elif xl << x :
        long= 'E'
    if yl >= y :
        lat= 'N'
    elif yl << y :
        lat= 'S'
    ang = str(angle)
    dir = Label(GOES2, text = "direction  " + ang +lat + long).grid(row = 3, column = 0)
    print("Direction",angle,lat,long)# this is the direction OUTPUT

    # determining the visibility from the user location 
    Alt= dataiss["height"]
    Alt = int(Alt)
    alti = str(Alt)
    
    alt = Label(GOES2, text = "alt:"+alti).grid(row = 4, column = 0)
    print(Alt)

    ELEVATION = math.atan(Alt/DISTANCE)
    Sight =math.degrees(ELEVATION)
    sli = str(Sight)
    slight = Label(GOES2, text = "sight"+sli).grid(row = 4, column = 0)
    print(Sight) # this is the angle of elevation OUTPUT




def GOES5(IDs):

    GOES5 = Toplevel()
    spacer2 = Label(GOES5, text = "", pady = 100)
    GOES5.title("GOES5")
    a = Label(GOES5, text = "hello this is the place where the data of GOES5 is stored").grid(row = 0, column = 0)
    Location =requests.get('https://ipinfo.io')
    datauser = Location.json()
    gpsloc = datauser['loc']
    aa = Label(GOES5, text = gpsloc).grid(row = 1, column = 0) # user location OUTPUT
    Xl,Yl = (gpsloc.split(','))
    xl = float(Xl)
    yl = float(Yl)
    xl=int(xl)
    yl=int(yl)

    url1 = ("https://uphere-space1.p.rapidapi.com/satellite/")
    url2 = IDs
    url3 =("/location")
    url= url1+url2+url3
    querystring = {"units":"imperial","lat":"47.6484346","lng":"122.374199"}
    headers = {
        'x-rapidapi-host': "uphere-space1.p.rapidapi.com",
        'x-rapidapi-key': "your api key"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    dataiss = response.json()
    position = dataiss["coordinates"]
    position= str(position)
    d = position.replace("[","")
    f = d.replace("]","")
    x,y = (f.split(','))
    x =float(x)
    y =float(y)
    x=int(x)
    y=int(y)
    #determining the distance and direction of ISS

    Dx = (x)-(xl)
    Dy = (y)-(yl)
    D2 =Dx**2 - Dy**2
    D2X = math.sqrt(D2**2)
    GPSDISTANCE = math.sqrt(D2X)
    DISTANCE = int(GPSDISTANCE*111)
    dis = str(DISTANCE)
    distance = Label(GOES5, text = dis + "km").grid(row = 2, column = 0)
    print(DISTANCE,'km')#this is Distance from user of Satellite OUTPUT
    rate = ((Dy/Dx)/math.pi)
    xis = math.atan(rate)
    angle= math.degrees(xis)
    if xl >= x :
        long='W'
    elif xl << x :
        long= 'E'
    if yl >= y :
        lat= 'N'
    elif yl << y :
        lat= 'S'
    ang = str(angle)
    dir = Label(GOES5, text = "direction  " + ang +lat + long).grid(row = 3, column = 0)
    print("Direction",angle,lat,long)# this is the direction OUTPUT

    # determining the visibility from the user location 
    Alt= dataiss["height"]
    Alt = int(Alt)
    alti = str(Alt)
    
    alt = Label(GOES5, text = "alt:"+alti).grid(row = 4, column = 0)
    print(Alt)

    ELEVATION = math.atan(Alt/DISTANCE)
    Sight =math.degrees(ELEVATION)
    sli = str(Sight)
    slight = Label(GOES5, text = "sight"+sli).grid(row = 4, column = 0)
    print(Sight) # this is the angle of elevation OUTPUT




def GOES17(IDs):

    GOES17 = Toplevel()
    spacer2 = Label(GOES17, text = "", pady = 100)
    GOES17.title("GOES17")
    a = Label(GOES17, text = "hello this is the place where the data of GOES17 is stored").grid(row = 0, column = 0)
    Location =requests.get('https://ipinfo.io')
    datauser = Location.json()
    gpsloc = datauser['loc']
    aa = Label(GOES17, text = gpsloc).grid(row = 1, column = 0) # user location OUTPUT
    Xl,Yl = (gpsloc.split(','))
    xl = float(Xl)
    yl = float(Yl)
    xl=int(xl)
    yl=int(yl)

    url1 = ("https://uphere-space1.p.rapidapi.com/satellite/")
    url2 = IDs
    url3 =("/location")
    url= url1+url2+url3
    querystring = {"units":"imperial","lat":"47.6484346","lng":"122.374199"}
    headers = {
        'x-rapidapi-host': "uphere-space1.p.rapidapi.com",
        'x-rapidapi-key': "your api key"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    dataiss = response.json()
    position = dataiss["coordinates"]
    position= str(position)
    d = position.replace("[","")
    f = d.replace("]","")
    x,y = (f.split(','))
    x =float(x)
    y =float(y)
    x=int(x)
    y=int(y)
    #determining the distance and direction of ISS

    Dx = (x)-(xl)
    Dy = (y)-(yl)
    D2 =Dx**2 - Dy**2
    D2X = math.sqrt(D2**2)
    GPSDISTANCE = math.sqrt(D2X)
    DISTANCE = int(GPSDISTANCE*111)
    dis = str(DISTANCE)
    distance = Label(GOES17, text = dis + "km").grid(row = 2, column = 0)
    print(DISTANCE,'km')#this is Distance from user of Satellite OUTPUT
    rate = ((Dy/Dx)/math.pi)
    xis = math.atan(rate)
    angle= math.degrees(xis)
    if xl >= x :
        long='W'
    elif xl << x :
        long= 'E'
    if yl >= y :
        lat= 'N'
    elif yl << y :
        lat= 'S'
    ang = str(angle)
    dir = Label(GOES17, text = "direction  " + ang +lat + long).grid(row = 3, column = 0)
    print("Direction",angle,lat,long)# this is the direction OUTPUT

    # determining the visibility from the user location 
    Alt= dataiss["height"]
    Alt = int(Alt)
    alti = str(Alt)
    
    alt = Label(GOES17, text = "alt:"+alti).grid(row = 4, column = 0)
    print(Alt)

    ELEVATION = math.atan(Alt/DISTANCE)
    Sight =math.degrees(ELEVATION)
    sli = str(Sight)
    slight = Label(GOES17, text = "sight"+sli).grid(row = 4, column = 0)
    print(Sight) # this is the angle of elevation OUTPUT




def GOES14(IDs):

    GOES14 = Toplevel()
    spacer2 = Label(GOES14, text = "", pady = 100)
    GOES14.title("GOES14")
    a = Label(GOES14, text = "hello this is the place where the data of GOES14 is stored").grid(row = 0, column = 0)
    Location =requests.get('https://ipinfo.io')
    datauser = Location.json()
    gpsloc = datauser['loc']
    aa = Label(GOES14, text = gpsloc).grid(row = 1, column = 0) # user location OUTPUT
    Xl,Yl = (gpsloc.split(','))
    xl = float(Xl)
    yl = float(Yl)
    xl=int(xl)
    yl=int(yl)

    url1 = ("https://uphere-space1.p.rapidapi.com/satellite/")
    url2 = IDs
    url3 =("/location")
    url= url1+url2+url3
    querystring = {"units":"imperial","lat":"47.6484346","lng":"122.374199"}
    headers = {
        'x-rapidapi-host': "uphere-space1.p.rapidapi.com",
        'x-rapidapi-key': "your api key"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    dataiss = response.json()
    position = dataiss["coordinates"]
    position= str(position)
    d = position.replace("[","")
    f = d.replace("]","")
    x,y = (f.split(','))
    x =float(x)
    y =float(y)
    x=int(x)
    y=int(y)
    #determining the distance and direction of ISS

    Dx = (x)-(xl)
    Dy = (y)-(yl)
    D2 =Dx**2 - Dy**2
    D2X = math.sqrt(D2**2)
    GPSDISTANCE = math.sqrt(D2X)
    DISTANCE = int(GPSDISTANCE*111)
    dis = str(DISTANCE)
    distance = Label(GOES14, text = dis + "km").grid(row = 2, column = 0)
    print(DISTANCE,'km')#this is Distance from user of Satellite OUTPUT
    rate = ((Dy/Dx)/math.pi)
    xis = math.atan(rate)
    angle= math.degrees(xis)
    if xl >= x :
        long='W'
    elif xl << x :
        long= 'E'
    if yl >= y :
        lat= 'N'
    elif yl << y :
        lat= 'S'
    ang = str(angle)
    dir = Label(GOES14, text = "direction  " + ang +lat + long).grid(row = 3, column = 0)
    print("Direction",angle,lat,long)# this is the direction OUTPUT

    # determining the visibility from the user location 
    Alt= dataiss["height"]
    Alt = int(Alt)
    alti = str(Alt)
    
    alt = Label(GOES14, text = "alt:"+alti).grid(row = 4, column = 0)
    print(Alt)

    ELEVATION = math.atan(Alt/DISTANCE)
    Sight =math.degrees(ELEVATION)
    sli = str(Sight)
    slight = Label(GOES14, text = "sight"+sli).grid(row = 4, column = 0)
    print(Sight) # this is the angle of elevation OUTPUT



def GOES16(IDs):

    GOES16 = Toplevel()
    spacer2 = Label(GOES16, text = "", pady = 100)
    GOES16.title("GOES16")
    a = Label(GOES16, text = "hello this is the place where the data of GOES16 is stored").grid(row = 0, column = 0)
    Location =requests.get('https://ipinfo.io')
    datauser = Location.json()
    gpsloc = datauser['loc']
    aa = Label(GOES16, text = gpsloc).grid(row = 1, column = 0) # user location OUTPUT
    Xl,Yl = (gpsloc.split(','))
    xl = float(Xl)
    yl = float(Yl)
    xl=int(xl)
    yl=int(yl)

    url1 = ("https://uphere-space1.p.rapidapi.com/satellite/")
    url2 = IDs
    url3 =("/location")
    url= url1+url2+url3
    querystring = {"units":"imperial","lat":"47.6484346","lng":"122.374199"}
    headers = {
        'x-rapidapi-host': "uphere-space1.p.rapidapi.com",
        'x-rapidapi-key': "your api key"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    dataiss = response.json()
    position = dataiss["coordinates"]
    position= str(position)
    d = position.replace("[","")
    f = d.replace("]","")
    x,y = (f.split(','))
    x =float(x)
    y =float(y)
    x=int(x)
    y=int(y)
    #determining the distance and direction of ISS

    Dx = (x)-(xl)
    Dy = (y)-(yl)
    D2 =Dx**2 - Dy**2
    D2X = math.sqrt(D2**2)
    GPSDISTANCE = math.sqrt(D2X)
    DISTANCE = int(GPSDISTANCE*111)
    dis = str(DISTANCE)
    distance = Label(GOES16, text = dis + "km").grid(row = 2, column = 0)
    print(DISTANCE,'km')#this is Distance from user of Satellite OUTPUT
    rate = ((Dy/Dx)/math.pi)
    xis = math.atan(rate)
    angle= math.degrees(xis)
    if xl >= x :
        long='W'
    elif xl << x :
        long= 'E'
    if yl >= y :
        lat= 'N'
    elif yl << y :
        lat= 'S'
    ang = str(angle)
    dir = Label(GOES16, text = "direction  " + ang +lat + long).grid(row = 3, column = 0)
    print("Direction",angle,lat,long)# this is the direction OUTPUT

    # determining the visibility from the user location 
    Alt= dataiss["height"]
    Alt = int(Alt)
    alti = str(Alt)
    
    alt = Label(GOES16, text = "alt:"+alti).grid(row = 4, column = 0)
    print(Alt)

    ELEVATION = math.atan(Alt/DISTANCE)
    Sight =math.degrees(ELEVATION)
    sli = str(Sight)
    slight = Label(GOES16, text = "sight"+sli).grid(row = 4, column = 0)
    print(Sight) # this is the angle of elevation OUTPUT




def GOES8(IDs):

    GOES8 = Toplevel()
    spacer2 = Label(GOES8, text = "", pady = 100)
    GOES8.title("GOES8")
    a = Label(GOES8, text = "hello this is the place where the data of GOES8 is stored").grid(row = 0, column = 0)
    Location =requests.get('https://ipinfo.io')
    datauser = Location.json()
    gpsloc = datauser['loc']
    aa = Label(GOES8, text = gpsloc).grid(row = 1, column = 0) # user location OUTPUT
    Xl,Yl = (gpsloc.split(','))
    xl = float(Xl)
    yl = float(Yl)
    xl=int(xl)
    yl=int(yl)

    url1 = ("https://uphere-space1.p.rapidapi.com/satellite/")
    url2 = IDs
    url3 =("/location")
    url= url1+url2+url3
    querystring = {"units":"imperial","lat":"47.6484346","lng":"122.374199"}
    headers = {
        'x-rapidapi-host': "uphere-space1.p.rapidapi.com",
        'x-rapidapi-key': "your api key"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    dataiss = response.json()
    position = dataiss["coordinates"]
    position= str(position)
    d = position.replace("[","")
    f = d.replace("]","")
    x,y = (f.split(','))
    x =float(x)
    y =float(y)
    x=int(x)
    y=int(y)
    #determining the distance and direction of ISS

    Dx = (x)-(xl)
    Dy = (y)-(yl)
    D2 =Dx**2 - Dy**2
    D2X = math.sqrt(D2**2)
    GPSDISTANCE = math.sqrt(D2X)
    DISTANCE = int(GPSDISTANCE*111)
    dis = str(DISTANCE)
    distance = Label(GOES8, text = dis + "km").grid(row = 2, column = 0)
    print(DISTANCE,'km')#this is Distance from user of Satellite OUTPUT
    rate = ((Dy/Dx)/math.pi)
    xis = math.atan(rate)
    angle= math.degrees(xis)
    if xl >= x :
        long='W'
    elif xl << x :
        long= 'E'
    if yl >= y :
        lat= 'N'
    elif yl << y :
        lat= 'S'
    ang = str(angle)
    dir = Label(GOES8, text = "direction  " + ang +lat + long).grid(row = 3, column = 0)
    print("Direction",angle,lat,long)# this is the direction OUTPUT

    # determining the visibility from the user location 
    Alt= dataiss["height"]
    Alt = int(Alt)
    alti = str(Alt)
    
    alt = Label(GOES8, text = "alt:"+alti).grid(row = 4, column = 0)
    print(Alt)

    ELEVATION = math.atan(Alt/DISTANCE)
    Sight =math.degrees(ELEVATION)
    sli = str(Sight)
    slight = Label(GOES8, text = "sight"+sli).grid(row = 4, column = 0)
    print(Sight) # this is the angle of elevation OUTPUT




def GOES3(IDs):

    GOES3 = Toplevel()
    spacer2 = Label(GOES3, text = "", pady = 100)
    GOES3.title("GOES3")
    a = Label(GOES3, text = "hello this is the place where the data of GOES3 is stored").grid(row = 0, column = 0)
    Location =requests.get('https://ipinfo.io')
    datauser = Location.json()
    gpsloc = datauser['loc']
    aa = Label(GOES3, text = gpsloc).grid(row = 1, column = 0) # user location OUTPUT
    Xl,Yl = (gpsloc.split(','))
    xl = float(Xl)
    yl = float(Yl)
    xl=int(xl)
    yl=int(yl)

    url1 = ("https://uphere-space1.p.rapidapi.com/satellite/")
    url2 = IDs
    url3 =("/location")
    url= url1+url2+url3
    querystring = {"units":"imperial","lat":"47.6484346","lng":"122.374199"}
    headers = {
        'x-rapidapi-host': "uphere-space1.p.rapidapi.com",
        'x-rapidapi-key': "your api key"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    dataiss = response.json()
    position = dataiss["coordinates"]
    position= str(position)
    d = position.replace("[","")
    f = d.replace("]","")
    x,y = (f.split(','))
    x =float(x)
    y =float(y)
    x=int(x)
    y=int(y)
    #determining the distance and direction of ISS

    Dx = (x)-(xl)
    Dy = (y)-(yl)
    D2 =Dx**2 - Dy**2
    D2X = math.sqrt(D2**2)
    GPSDISTANCE = math.sqrt(D2X)
    DISTANCE = int(GPSDISTANCE*111)
    dis = str(DISTANCE)
    distance = Label(GOES3, text = dis + "km").grid(row = 2, column = 0)
    print(DISTANCE,'km')#this is Distance from user of Satellite OUTPUT
    rate = ((Dy/Dx)/math.pi)
    xis = math.atan(rate)
    angle= math.degrees(xis)
    if xl >= x :
        long='W'
    elif xl << x :
        long= 'E'
    if yl >= y :
        lat= 'N'
    elif yl << y :
        lat= 'S'
    ang = str(angle)
    dir = Label(GOES3, text = "direction  " + ang +lat + long).grid(row = 3, column = 0)
    print("Direction",angle,lat,long)# this is the direction OUTPUT

    # determining the visibility from the user location 
    Alt= dataiss["height"]
    Alt = int(Alt)
    alti = str(Alt)
    
    alt = Label(GOES3, text = "alt:"+alti).grid(row = 4, column = 0)
    print(Alt)

    ELEVATION = math.atan(Alt/DISTANCE)
    Sight =math.degrees(ELEVATION)
    sli = str(Sight)
    slight = Label(GOES3, text = "sight"+sli).grid(row = 4, column = 0)
    print(Sight) # this is the angle of elevation OUTPUT



def GOES4(IDs):

    GOES4 = Toplevel()
    spacer2 = Label(GOES4, text = "", pady = 100)
    GOES4.title("GOES4")
    a = Label(GOES4, text = "hello this is the place where the data of GOES4 is stored").grid(row = 0, column = 0)
    Location =requests.get('https://ipinfo.io')
    datauser = Location.json()
    gpsloc = datauser['loc']
    aa = Label(GOES4, text = gpsloc).grid(row = 1, column = 0) # user location OUTPUT
    Xl,Yl = (gpsloc.split(','))
    xl = float(Xl)
    yl = float(Yl)
    xl=int(xl)
    yl=int(yl)

    url1 = ("https://uphere-space1.p.rapidapi.com/satellite/")
    url2 = IDs
    url3 =("/location")
    url= url1+url2+url3
    querystring = {"units":"imperial","lat":"47.6484346","lng":"122.374199"}
    headers = {
        'x-rapidapi-host': "uphere-space1.p.rapidapi.com",
        'x-rapidapi-key': "your api key"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    dataiss = response.json()
    position = dataiss["coordinates"]
    position= str(position)
    d = position.replace("[","")
    f = d.replace("]","")
    x,y = (f.split(','))
    x =float(x)
    y =float(y)
    x=int(x)
    y=int(y)
    #determining the distance and direction of ISS

    Dx = (x)-(xl)
    Dy = (y)-(yl)
    D2 =Dx**2 - Dy**2
    D2X = math.sqrt(D2**2)
    GPSDISTANCE = math.sqrt(D2X)
    DISTANCE = int(GPSDISTANCE*111)
    dis = str(DISTANCE)
    distance = Label(GOES4, text = dis + "km").grid(row = 2, column = 0)
    print(DISTANCE,'km')#this is Distance from user of Satellite OUTPUT
    rate = ((Dy/Dx)/math.pi)
    xis = math.atan(rate)
    angle= math.degrees(xis)
    if xl >= x :
        long='W'
    elif xl << x :
        long= 'E'
    if yl >= y :
        lat= 'N'
    elif yl << y :
        lat= 'S'
    ang = str(angle)
    dir = Label(GOES4, text = "direction  " + ang +lat + long).grid(row = 3, column = 0)
    print("Direction",angle,lat,long)# this is the direction OUTPUT

    # determining the visibility from the user location 
    Alt= dataiss["height"]
    Alt = int(Alt)
    alti = str(Alt)
    
    alt = Label(GOES4, text = "alt:"+alti).grid(row = 4, column = 0)
    print(Alt)

    ELEVATION = math.atan(Alt/DISTANCE)
    Sight =math.degrees(ELEVATION)
    sli = str(Sight)
    slight = Label(GOES4, text = "sight"+sli).grid(row = 4, column = 0)
    print(Sight) # this is the angle of elevation OUTPUT



def GOES9(IDs):

    GOES9 = Toplevel()
    spacer2 = Label(GOES9, text = "", pady = 100)
    GOES9.title("GOES9")
    a = Label(GOES9, text = "hello this is the place where the data of GOES9 is stored").grid(row = 0, column = 0)
    Location =requests.get('https://ipinfo.io')
    datauser = Location.json()
    gpsloc = datauser['loc']
    aa = Label(GOES9, text = gpsloc).grid(row = 1, column = 0) # user location OUTPUT
    Xl,Yl = (gpsloc.split(','))
    xl = float(Xl)
    yl = float(Yl)
    xl=int(xl)
    yl=int(yl)

    url1 = ("https://uphere-space1.p.rapidapi.com/satellite/")
    url2 = IDs
    url3 =("/location")
    url= url1+url2+url3
    querystring = {"units":"imperial","lat":"47.6484346","lng":"122.374199"}
    headers = {
        'x-rapidapi-host': "uphere-space1.p.rapidapi.com",
        'x-rapidapi-key': "your api key"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    dataiss = response.json()
    position = dataiss["coordinates"]
    position= str(position)
    d = position.replace("[","")
    f = d.replace("]","")
    x,y = (f.split(','))
    x =float(x)
    y =float(y)
    x=int(x)
    y=int(y)
    #determining the distance and direction of ISS

    Dx = (x)-(xl)
    Dy = (y)-(yl)
    D2 =Dx**2 - Dy**2
    D2X = math.sqrt(D2**2)
    GPSDISTANCE = math.sqrt(D2X)
    DISTANCE = int(GPSDISTANCE*111)
    dis = str(DISTANCE)
    distance = Label(GOES9, text = dis + "km").grid(row = 2, column = 0)
    print(DISTANCE,'km')#this is Distance from user of Satellite OUTPUT
    rate = ((Dy/Dx)/math.pi)
    xis = math.atan(rate)
    angle= math.degrees(xis)
    if xl >= x :
        long='W'
    elif xl << x :
        long= 'E'
    if yl >= y :
        lat= 'N'
    elif yl << y :
        lat= 'S'
    ang = str(angle)
    dir = Label(GOES9, text = "direction  " + ang +lat + long).grid(row = 3, column = 0)
    print("Direction",angle,lat,long)# this is the direction OUTPUT

    # determining the visibility from the user location 
    Alt= dataiss["height"]
    Alt = int(Alt)
    alti = str(Alt)
    
    alt = Label(GOES9, text = "alt:"+alti).grid(row = 4, column = 0)
    print(Alt)

    ELEVATION = math.atan(Alt/DISTANCE)
    Sight =math.degrees(ELEVATION)
    sli = str(Sight)
    slight = Label(GOES9, text = "sight"+sli).grid(row = 4, column = 0)
    print(Sight) # this is the angle of elevation OUTPUT



def GOES11(IDs):

    GOES11 = Toplevel()
    spacer2 = Label(GOES11, text = "", pady = 100)
    GOES11.title("GOES11")
    a = Label(GOES11, text = "hello this is the place where the data of GOES11 is stored").grid(row = 0, column = 0)
    Location =requests.get('https://ipinfo.io')
    datauser = Location.json()
    gpsloc = datauser['loc']
    aa = Label(GOES11, text = gpsloc).grid(row = 1, column = 0) # user location OUTPUT
    Xl,Yl = (gpsloc.split(','))
    xl = float(Xl)
    yl = float(Yl)
    xl=int(xl)
    yl=int(yl)

    url1 = ("https://uphere-space1.p.rapidapi.com/satellite/")
    url2 = IDs
    url3 =("/location")
    url= url1+url2+url3
    querystring = {"units":"imperial","lat":"47.6484346","lng":"122.374199"}
    headers = {
        'x-rapidapi-host': "uphere-space1.p.rapidapi.com",
        'x-rapidapi-key': "your api key"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    dataiss = response.json()
    position = dataiss["coordinates"]
    position= str(position)
    d = position.replace("[","")
    f = d.replace("]","")
    x,y = (f.split(','))
    x =float(x)
    y =float(y)
    x=int(x)
    y=int(y)
    #determining the distance and direction of ISS

    Dx = (x)-(xl)
    Dy = (y)-(yl)
    D2 =Dx**2 - Dy**2
    D2X = math.sqrt(D2**2)
    GPSDISTANCE = math.sqrt(D2X)
    DISTANCE = int(GPSDISTANCE*111)
    dis = str(DISTANCE)
    distance = Label(GOES11, text = dis + "km").grid(row = 2, column = 0)
    print(DISTANCE,'km')#this is Distance from user of Satellite OUTPUT
    rate = ((Dy/Dx)/math.pi)
    xis = math.atan(rate)
    angle= math.degrees(xis)
    if xl >= x :
        long='W'
    elif xl << x :
        long= 'E'
    if yl >= y :
        lat= 'N'
    elif yl << y :
        lat= 'S'
    ang = str(angle)
    dir = Label(GOES11, text = "direction  " + ang +lat + long).grid(row = 3, column = 0)
    print("Direction",angle,lat,long)# this is the direction OUTPUT

    # determining the visibility from the user location 
    Alt= dataiss["height"]
    Alt = int(Alt)
    alti = str(Alt)
    
    alt = Label(GOES11, text = "alt:"+alti).grid(row = 4, column = 0)
    print(Alt)

    ELEVATION = math.atan(Alt/DISTANCE)
    Sight =math.degrees(ELEVATION)
    sli = str(Sight)
    slight = Label(GOES11, text = "sight"+sli).grid(row = 4, column = 0)
    print(Sight) # this is the angle of elevation OUTPUT



def GOES15(IDs):

    GOES15 = Toplevel()
    spacer2 = Label(GOES15, text = "", pady = 100)
    GOES15.title("GOES15")
    a = Label(GOES15, text = "hello this is the place where the data of GOES15 is stored").grid(row = 0, column = 0)
    Location =requests.get('https://ipinfo.io')
    datauser = Location.json()
    gpsloc = datauser['loc']
    aa = Label(GOES15, text = gpsloc).grid(row = 1, column = 0) # user location OUTPUT
    Xl,Yl = (gpsloc.split(','))
    xl = float(Xl)
    yl = float(Yl)
    xl=int(xl)
    yl=int(yl)

    url1 = ("https://uphere-space1.p.rapidapi.com/satellite/")
    url2 = IDs
    url3 =("/location")
    url= url1+url2+url3
    querystring = {"units":"imperial","lat":"47.6484346","lng":"122.374199"}
    headers = {
        'x-rapidapi-host': "uphere-space1.p.rapidapi.com",
        'x-rapidapi-key': "your api key"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    dataiss = response.json()
    position = dataiss["coordinates"]
    position= str(position)
    d = position.replace("[","")
    f = d.replace("]","")
    x,y = (f.split(','))
    x =float(x)
    y =float(y)
    x=int(x)
    y=int(y)
    #determining the distance and direction of ISS

    Dx = (x)-(xl)
    Dy = (y)-(yl)
    D2 =Dx**2 - Dy**2
    D2X = math.sqrt(D2**2)
    GPSDISTANCE = math.sqrt(D2X)
    DISTANCE = int(GPSDISTANCE*111)
    dis = str(DISTANCE)
    distance = Label(GOES15, text = dis + "km").grid(row = 2, column = 0)
    print(DISTANCE,'km')#this is Distance from user of Satellite OUTPUT
    rate = ((Dy/Dx)/math.pi)
    xis = math.atan(rate)
    angle= math.degrees(xis)
    if xl >= x :
        long='W'
    elif xl << x :
        long= 'E'
    if yl >= y :
        lat= 'N'
    elif yl << y :
        lat= 'S'
    ang = str(angle)
    dir = Label(GOES15, text = "direction  " + ang +lat + long).grid(row = 3, column = 0)
    print("Direction",angle,lat,long)# this is the direction OUTPUT

    # determining the visibility from the user location 
    Alt= dataiss["height"]
    Alt = int(Alt)
    alti = str(Alt)
    
    alt = Label(GOES15, text = "alt:"+alti).grid(row = 4, column = 0)
    print(Alt)

    ELEVATION = math.atan(Alt/DISTANCE)
    Sight =math.degrees(ELEVATION)
    sli = str(Sight)
    slight = Label(GOES15, text = "sight"+sli).grid(row = 4, column = 0)
    print(Sight) # this is the angle of elevation OUTPUT



def GOES13(IDs):

    GOES13 = Toplevel()
    spacer2 = Label(GOES13, text = "", pady = 100)
    GOES13.title("GOES13")
    a = Label(GOES13, text = "hello this is the place where the data of GOES13 is stored").grid(row = 0, column = 0)
    Location =requests.get('https://ipinfo.io')
    datauser = Location.json()
    gpsloc = datauser['loc']
    aa = Label(GOES13, text = gpsloc).grid(row = 1, column = 0) # user location OUTPUT
    Xl,Yl = (gpsloc.split(','))
    xl = float(Xl)
    yl = float(Yl)
    xl=int(xl)
    yl=int(yl)

    url1 = ("https://uphere-space1.p.rapidapi.com/satellite/")
    url2 = IDs
    url3 =("/location")
    url= url1+url2+url3
    querystring = {"units":"imperial","lat":"47.6484346","lng":"122.374199"}
    headers = {
        'x-rapidapi-host': "uphere-space1.p.rapidapi.com",
        'x-rapidapi-key': "your api key"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    dataiss = response.json()
    position = dataiss["coordinates"]
    position= str(position)
    d = position.replace("[","")
    f = d.replace("]","")
    x,y = (f.split(','))
    x =float(x)
    y =float(y)
    x=int(x)
    y=int(y)
    #determining the distance and direction of ISS

    Dx = (x)-(xl)
    Dy = (y)-(yl)
    D2 =Dx**2 - Dy**2
    D2X = math.sqrt(D2**2)
    GPSDISTANCE = math.sqrt(D2X)
    DISTANCE = int(GPSDISTANCE*111)
    dis = str(DISTANCE)
    distance = Label(GOES13, text = dis + "km").grid(row = 2, column = 0)
    print(DISTANCE,'km')#this is Distance from user of Satellite OUTPUT
    rate = ((Dy/Dx)/math.pi)
    xis = math.atan(rate)
    angle= math.degrees(xis)
    if xl >= x :
        long='W'
    elif xl << x :
        long= 'E'
    if yl >= y :
        lat= 'N'
    elif yl << y :
        lat= 'S'
    ang = str(angle)
    dir = Label(GOES13, text = "direction  " + ang +lat + long).grid(row = 3, column = 0)
    print("Direction",angle,lat,long)# this is the direction OUTPUT

    # determining the visibility from the user location 
    Alt= dataiss["height"]
    Alt = int(Alt)
    alti = str(Alt)
    
    alt = Label(GOES13, text = "alt:"+alti).grid(row = 4, column = 0)
    print(Alt)

    ELEVATION = math.atan(Alt/DISTANCE)
    Sight =math.degrees(ELEVATION)
    sli = str(Sight)
    slight = Label(GOES13, text = "sight"+sli).grid(row = 4, column = 0)
    print(Sight) # this is the angle of elevation OUTPUT




def GOES7(IDs):

    GOES7 = Toplevel()
    spacer2 = Label(GOES7, text = "", pady = 100)
    GOES7.title("GOES7")
    a = Label(GOES7, text = "hello this is the place where the data of GOES7 is stored").grid(row = 0, column = 0)
    Location =requests.get('https://ipinfo.io')
    datauser = Location.json()
    gpsloc = datauser['loc']
    aa = Label(GOES7, text = gpsloc).grid(row = 1, column = 0) # user location OUTPUT
    Xl,Yl = (gpsloc.split(','))
    xl = float(Xl)
    yl = float(Yl)
    xl=int(xl)
    yl=int(yl)

    url1 = ("https://uphere-space1.p.rapidapi.com/satellite/")
    url2 = IDs
    url3 =("/location")
    url= url1+url2+url3
    querystring = {"units":"imperial","lat":"47.6484346","lng":"122.374199"}
    headers = {
        'x-rapidapi-host': "uphere-space1.p.rapidapi.com",
        'x-rapidapi-key': "your api key"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    dataiss = response.json()
    position = dataiss["coordinates"]
    position= str(position)
    d = position.replace("[","")
    f = d.replace("]","")
    x,y = (f.split(','))
    x =float(x)
    y =float(y)
    x=int(x)
    y=int(y)
    #determining the distance and direction of ISS

    Dx = (x)-(xl)
    Dy = (y)-(yl)
    D2 =Dx**2 - Dy**2
    D2X = math.sqrt(D2**2)
    GPSDISTANCE = math.sqrt(D2X)
    DISTANCE = int(GPSDISTANCE*111)
    dis = str(DISTANCE)
    distance = Label(GOES7, text = dis + "km").grid(row = 2, column = 0)
    print(DISTANCE,'km')#this is Distance from user of Satellite OUTPUT
    rate = ((Dy/Dx)/math.pi)
    xis = math.atan(rate)
    angle= math.degrees(xis)
    if xl >= x :
        long='W'
    elif xl << x :
        long= 'E'
    if yl >= y :
        lat= 'N'
    elif yl << y :
        lat= 'S'
    ang = str(angle)
    dir = Label(GOES7, text = "direction  " + ang +lat + long).grid(row = 3, column = 0)
    print("Direction",angle,lat,long)# this is the direction OUTPUT

    # determining the visibility from the user location 
    Alt= dataiss["height"]
    Alt = int(Alt)
    alti = str(Alt)
    
    alt = Label(GOES7, text = "alt:"+alti).grid(row = 4, column = 0)
    print(Alt)

    ELEVATION = math.atan(Alt/DISTANCE)
    Sight =math.degrees(ELEVATION)
    sli = str(Sight)
    slight = Label(GOES7, text = "sight"+sli).grid(row = 4, column = 0)
    print(Sight) # this is the angle of elevation OUTPUT




def GOES10(IDs):

    GOES10 = Toplevel()
    spacer2 = Label(GOES10, text = "", pady = 100)
    GOES10.title("GOES10")
    a = Label(GOES10, text = "hello this is the place where the data of GOES10 is stored").grid(row = 0, column = 0)
    Location =requests.get('https://ipinfo.io')
    datauser = Location.json()
    gpsloc = datauser['loc']
    aa = Label(GOES10, text = gpsloc).grid(row = 1, column = 0) # user location OUTPUT
    Xl,Yl = (gpsloc.split(','))
    xl = float(Xl)
    yl = float(Yl)
    xl=int(xl)
    yl=int(yl)

    url1 = ("https://uphere-space1.p.rapidapi.com/satellite/")
    url2 = IDs
    url3 =("/location")
    url= url1+url2+url3
    querystring = {"units":"imperial","lat":"47.6484346","lng":"122.374199"}
    headers = {
        'x-rapidapi-host': "uphere-space1.p.rapidapi.com",
        'x-rapidapi-key': "your api key"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    dataiss = response.json()
    position = dataiss["coordinates"]
    position= str(position)
    d = position.replace("[","")
    f = d.replace("]","")
    x,y = (f.split(','))
    x =float(x)
    y =float(y)
    x=int(x)
    y=int(y)
    #determining the distance and direction of ISS

    Dx = (x)-(xl)
    Dy = (y)-(yl)
    D2 =Dx**2 - Dy**2
    D2X = math.sqrt(D2**2)
    GPSDISTANCE = math.sqrt(D2X)
    DISTANCE = int(GPSDISTANCE*111)
    dis = str(DISTANCE)
    distance = Label(GOES10, text = dis + "km").grid(row = 2, column = 0)
    print(DISTANCE,'km')#this is Distance from user of Satellite OUTPUT
    rate = ((Dy/Dx)/math.pi)
    xis = math.atan(rate)
    angle= math.degrees(xis)
    if xl >= x :
        long='W'
    elif xl << x :
        long= 'E'
    if yl >= y :
        lat= 'N'
    elif yl << y :
        lat= 'S'
    ang = str(angle)
    dir = Label(GOES10, text = "direction  " + ang +lat + long).grid(row = 3, column = 0)
    print("Direction",angle,lat,long)# this is the direction OUTPUT

    # determining the visibility from the user location 
    Alt= dataiss["height"]
    Alt = int(Alt)
    alti = str(Alt)
    
    alt = Label(GOES10, text = "alt:"+alti).grid(row = 4, column = 0)
    print(Alt)

    ELEVATION = math.atan(Alt/DISTANCE)
    Sight =math.degrees(ELEVATION)
    sli = str(Sight)
    slight = Label(GOES10, text = "sight"+sli).grid(row = 4, column = 0)
    print(Sight) # this is the angle of elevation OUTPUT


about = Button(root, text = "About", padx = 60, command = abouts)
ref = Button(root, text = "reference", padx = 15, command = ref)
Exit = Button(root, text = "Exit", padx = 15, command = root.destroy)

#sats

abc1= Button(root, text = "GEOS6", padx = 50, command =lambda: GEOS6("14050"))
abc2= Button(root, text = "GOES12", padx = 47, command =lambda: GOES12("26871"))
abc3= Button(root, text = "GOES2", padx = 50, command =lambda: GOES2("10061"))
abc4= Button(root, text = "GOES5", padx = 50, command =lambda: GOES5("12472"))
abc5= Button(root, text = "GOES17", padx = 47, command =lambda: GOES17("43226"))
abc6= Button(root, text = "GOES14", padx = 47, command =lambda: GOES14("35491"))
abc7= Button(root, text = "GOES16", padx = 47, command =lambda: GOES16("41866"))
abc8= Button(root, text = "GOES8", padx = 50, command =lambda: GOES8("23051"))
abc9= Button(root, text = "GOES3", padx = 50, command =lambda: GOES3("10953"))
abc10= Button(root, text = "GOES4", padx = 50, command =lambda: GOES4("11964"))
abc11= Button(root, text = "GOES9", padx = 50, command =lambda: GOES9("23581"))
abc12= Button(root, text = "GOES11", padx = 50, command =lambda: GOES11("26352"))
abc13= Button(root, text = "GOES15", padx = 50, command =lambda: GOES15("36411"))
abc14= Button(root, text = "GOES13", padx = 50, command =lambda: GOES13("29155"))
abc15= Button(root, text = "GOES7", padx = 50, command =lambda: GOES7("17561"))
abc16= Button(root, text = "GOES10", padx = 50, command =lambda: GOES10("24786"))

back = ImageTk.PhotoImage(Image.open("back.jpg"))
bg = Label(image=back)
#nasa logo
first_img = ImageTk.PhotoImage(Image.open("nasa.png"))
image1 = Label(image=first_img)

about.grid(row = 0, column = 0)
ref.grid(row = 0, column = 1)
Exit.grid(row = 0, column = 2)
spacer1.grid(row = 0, column = 3)
image1.grid(row = 1, column = 0, columnspan = 2)
satallite.grid(row = 2, column = 0)
abc1.grid(row = 3, column = 0)
abc2.grid(row = 4, column = 0)
abc3.grid(row = 5, column = 0)
abc4.grid(row = 6, column = 0)
abc5.grid(row = 7, column = 0)
abc6.grid(row = 8, column = 0)
abc7.grid(row = 9, column = 0)
abc8.grid(row = 10, column = 0)
bg.grid(row =0 , column =3, rowspan = 13)

root.mainloop()
