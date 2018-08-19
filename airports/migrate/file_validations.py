# from airports.models import Airport
from airport.models import Airport

def airport_file_validations(text:str):
    '''
    {
        'airport_id':0, 'name':1, 'city': 2, 'country': 3, 'iata':4,
        'icao':5, 'latitude':6, 'longitude':7, 'altitude':8, 'timezone':9,
        'dst':10, 'tz':11, 'type':12, 'source:':13
    }

    airport_id  integer
    name        string
    city        string
    country     string
    iata        string
    icao        string
    latitude    float
    longitude   float
    altitude    float
    timezone    integer
    dst         string
    tz          string
    type        string
    source      string

    result = 0 if wrong format
    result = 1 if already exists
    result = 2 if created
    '''

    result = 0
    airport = None

    line = text.decode('utf-8')
    # print (line)
    info = line.split(',')
    info = [li.replace('"', '') for li in info]

    if len(info) != 14:
        # print ("ERROR1")
        return airport, result
    else:
        try:
            airport_id = int(info[0])
            name = str(info[1])
            city = str(info[2])
            country = str(info[3])
            iata = str(info[4])
            icao = str(info[5])
            latitude = float(info[6])
            longitude = float(info[7])
            altitude = float(info[8])
            timezone = int(info[9])
            dst = str(info[10])
            tz = str(info[11])
            type = str(info[12])
            source = str(info[13])
        except:
            # print ("ERROR2")
            return airport, result

        if Airport.objects.filter(pk=airport_id).count() > 0:
            # print ("EXISTS")
            result = 1
            airport = Airport.objects.filter(pk=airport_id).first()
            airport.update(name=name, city=city, country=country, iata=iata, icao=icao, latitude=latitude, longitude=longitude, altitude=altitude, timezone=timezone, dst=dst, tz=tz, type=type, source=source)
            return airport, result
        else:
            # print ("SUCCESS")
            result = 2
            airport = Airport.objects.create(airport_id=airport_id, name=name, city=city, country=country, iata=iata, icao=icao, latitude=latitude, longitude=longitude, altitude=altitude, timezone=timezone, dst=dst, tz=tz, type=type, source=source)
            return airport, result
