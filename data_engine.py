import requests
from datetime import datetime

'''def get_caf_dayparts():
    r = requests.get('http://legacy.cafebonappetit.com/api/2/menus?cafe=17?format=jsonp')
    raw_json = r.json()

    raw_dayparts = raw_json['days'][0]['cafes']['17?format=jsonp']['dayparts'][0]
    raw_items = raw_json['items']

    output = []

    for daypart in raw_dayparts:
        temp = {}
        temp['label'] = daypart['label'].title()

        # Time conversion
        starttime = datetime.strptime(daypart['starttime'], "%H:%M")
        endtime = datetime.strptime(daypart['endtime'], "%H:%M")

        temp['starttime'] = starttime.strftime("%I:%M %p").lstrip("0")
        temp['endtime'] = endtime.strftime("%I:%M %p").lstrip("0")


        # Items
        temp['items'] = []

        item_IDs = []

        for station in daypart['stations']:
            for ID in station['items']:
                item_IDs.append(ID)

        for ID in item_IDs:
            temp['items'].append(raw_items[ID]['label'].title())

        output.append(temp)

    return output'''


def get_dayparts(cafeID):
    r = requests.get('http://legacy.cafebonappetit.com/api/2/menus?cafe=' + str(cafeID) + '?format=jsonp')
    raw_json = r.json()

    raw_dayparts = raw_json['days'][0]['cafes'][str(cafeID) + '?format=jsonp']['dayparts'][0]
    raw_items = raw_json['items']

    output = []

    for daypart in raw_dayparts:
        temp = {}
        temp['label'] = daypart['label'].title()

        # Time conversion
        starttime = datetime.strptime(daypart['starttime'], "%H:%M")
        endtime = datetime.strptime(daypart['endtime'], "%H:%M")

        temp['starttime'] = starttime.strftime("%I:%M %p").lstrip("0")
        temp['endtime'] = endtime.strftime("%I:%M %p").lstrip("0")

        master_stations = {}

        for station in daypart['stations']:
            temp_stations = []
            for item in station['items']:
                temp_stations.append(raw_items[item]['label'].title())

                master_stations[station['label']] = temp_stations



        temp['stations'] = master_stations


        '''# Items
        temp['items'] = {}



        for ID in item_IDs:
            temp['items'][ID[0]] = (raw_items[ID[1]]['label'].title())'''

        output.append(temp)

    return output


if __name__ == "__main__":
    print get_dayparts(742)
