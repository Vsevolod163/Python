from user_interface import temperature_view
from user_interface import wind_speed_view
from user_interface import pressure_view

path2 = '/Users/seva/Desktop/Учеба/Python/Lections/Lection4/join_jon/data.xml'
def create(device = 1):
    xml = '<xml>\n'
    xml += '      <temperature units = "c">{}</temperature>\n'\
        .format(temperature_view(device))
    xml += '      <wind_speed_view units = "m/s">{}</wind_speed_view>\n'\
        .format(wind_speed_view(device))
    xml += '      <pressure units = "mmHg">{}</pressure>\n'\
        .format(pressure_view(device))
    xml += '</xml>'

    with open(path2, 'w') as page:
        page.write(xml)

    return xml

path3 = '/Users/seva/Desktop/Учеба/Python/Lections/Lection4/join_jon/new_data.xml'
def new_create(data, device = 1):
    t, p, w = data
    t = t * 1.8 + 32
    xml = '<xml>\n'
    xml += '      <temperature units = "f">{}</temperature>\n'\
        .format(t)
    xml += '      <wind_speed_view units = "m/s">{}</wind_speed_view>\n'\
        .format(w)
    xml += '      <pressure units = "mmHg">{}</pressure>\n'\
        .format(p)
    xml += '</xml>'

    with open(path3, 'w') as page:
        page.write(xml)

    return data