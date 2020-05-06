import requests

request = requests.get('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
with open('C:/Users/User/PycharmProjects/jpwp2/plik.csv', 'w') as csv:
    csv.write(request.text)
