from user_interface import temperature_view
from user_interface import wind_speed_view
from user_interface import pressure_view

path2 = '/Users/seva/Desktop/Учеба/Python/Lections/Lection4/join_jon/index.html'
def create(device = 1):
    style = 'style="font-size:30px;"'
    html = '<html>\n <head></head>\n <body>\n'
    html += '      <p {}>Temperature: {} c</p>\n'\
        .format(style, temperature_view(device))
    html += '      <p {}>Wind_speed: {} c</p>\n'\
        .format(style, wind_speed_view(device))
    html += '      <p {}>Pressure: {} c</p>\n'\
        .format(style, pressure_view(device))
    html += '</body>\n</html>'

    with open(path2, 'w') as page:
        page.write(html)

    return html

path3 = '/Users/seva/Desktop/Учеба/Python/Lections/Lection4/join_jon/new_index.html'
def new_create(data, device = 1):
    t, p, w = data
    style = 'style="font-size:30px;"'
    html = '<html>\n <head></head>\n <body>\n'
    html += '      <p {}>Temperature: {} c</p>\n'\
        .format(style, t)
    html += '      <p {}>Wind_speed: {} c</p>\n'\
        .format(style, w)
    html += '      <p {}>Pressure: {} c</p>\n'\
        .format(style, p)
    html += '</body>\n</html>'

    with open(path3, 'w') as page:
        page.write(html)

    return data