from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/api/covid-data', methods=['POST'])
def covid_data():
    data = request.json
    country = data.get('country')

    # Example API call to COVID-19 data
    response = requests.get(f'https://api.covid19api.com/summary')
    if response.status_code == 200:
        summary = response.json()
        countries = summary['Countries']
        country_data = next((c for c in countries if c['Country'].lower() == country.lower()), None)
        if country_data:
            return jsonify({
                'total_cases': country_data['TotalConfirmed'],
                'total_deaths': country_data['TotalDeaths'],
                'total_recovered': country_data['TotalRecovered']
            })
    return jsonify({'error': 'Country not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
