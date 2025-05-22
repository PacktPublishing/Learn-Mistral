from flask import Flask, render_template
import requests
import json

app = Flask(__name__)  

@app.route('/joke', methods=['GET'])
def get_joke():
    with open('/Users/pavlocherkashyn/.continue/config.json') as config_file:
        config = json.load(config_file)

    response = requests.get(config['joke_api'])
    joke = response.json()['value']

    return render_template('joke.html', joke=joke)

if __name__ == '__main__':
    app.run(debug=True)
