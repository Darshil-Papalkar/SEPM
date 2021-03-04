from flask import Flask, render_template, request, abort
import json
import urllib.request 

app = Flask(__name__)
app.secret_key = b'\x1a\x1b$$+p\xd7\xd9YX\x87\x0e\xfeQb\xebl\xba\x84H]^d!'

countryCode = {'India': "IN"}

stateCode = {
                "Andhra pradesh": "AD",
                "Arunachal pradesh":"AR",
                "Assam":"AS",
                "Bihar":"BR",
                "Chattisgarh":'CG',
                "Delhi":"DL",
                "Goa":"GA",
                "Gujarat":"GJ",
                "Haryana":"HR",
                "Himachal pradesh":"HP",
                "Jammu and kashmir":"JK",
                "Jharkhand":"JH",
                "Karnataka":"KA",
                "Kerala":"KL",
                "Lakshadweep islands":"LD",
                "Madhya pradesh":"MP",
                "Maharashtra":"MH",
                "Manipur":"MN",
                "Meghalaya":'ML',
                "Mizoram":"MZ",
                "Nagaland":'NL',
                'Odisha':'OD',
                "Pondicherry":"PY",
                'Punjab':'PB',
                'Rajasthan':"RJ",
                "Sikkim":"SK",
                "Tamil nadu":"TN",
                'Telangana':'TS',
                'Tripura':"TR",
                "Uttar pradesh":"UP",
                "Uttarakhand":"UK",
                "West bengal":"WB"
}

def tocelcius(temp):
    return str(round(float(temp) - 273.16,2))

@app.route('/')
@app.route("/home/")
def home():
    return render_template('index.html')

@app.route('/weather/', methods=['POST','GET'])
def weather():
    if request.method == 'POST': 
        city = request.form['city']
        state = request.form['state']
        # country = request.form['country']
    else: 
        city = "Vadodara"
        state = "gujarat"
    
    country = "India"
  
    api = 'api_key' 
  
    try:
        source = urllib.request.urlopen("https://api.openweathermap.org/data/2.5/weather?q=" + city + "," + stateCode[state.capitalize()].upper() + "," + countryCode[country.capitalize()].upper() + "&appid=" + api).read()
    except Exception as e:
        print(e)
        return abort(404)

    list_of_data = json.loads(source) 
  
    data = { 
        "country_code": str(list_of_data['sys']['country']),
        "coordinate": str(list_of_data['coord']['lon']) + ' ' + str(list_of_data['coord']['lat']),
        "temp": str(list_of_data['main']['temp']) + 'k',
        "temp_cel": tocelcius(list_of_data['main']['temp']) + 'C',
        "pressure": str(list_of_data['main']['pressure']),
        "humidity": str(list_of_data['main']['humidity']),
        "cityname":str(city.capitalize()),
        "statename" : str(state.capitalize()),
        "countryname" : str(country.capitalize()),
    } 
#     print(data) 
    return render_template('weather.html', data = data)


if __name__ == "__main__":
    app.run(debug=True)
