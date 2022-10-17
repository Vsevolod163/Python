from user_interface import temperature_view
from user_interface import wind_speed_view
from user_interface import pressure_view

path2 = '/Users/seva/Desktop/Учеба/Python/Lections/Lection4/join_jon/index.html'
def create(device = 1):
    xml = '<xml>\n"'
    html += '      <temperature units = "c">{}</temperature>\n'\
        .format(style, temperature_view(device))
    html += '      <p {}>Wind_speed: {} c</p>\n'\
        .format(style, wind_speed_view(device))
    html += '      <p {}>Pressure: {} c</p>\n'\
        .format(style, pressure_view(device))
    html += '</body>\n</html>'

    with open(path2, 'w') as page:
        page.write(html)

    return html