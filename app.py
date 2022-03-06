from flask import Flask, render_template
import json
import os

PORT = int(os.environ.get('PORT', 8080))

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/trade", methods=['GET', 'POST'])
def trade_page():

    with open('db/recent_trades.json', 'r') as in_trades:
        recent_trades = json.load(in_trades)

    with open('db/available_trades.json', 'r') as in_trades2:
        available_trades = json.load(in_trades2)

    return render_template(
            'trades.html', 
            recent_trades=recent_trades['trades'],
            available_trades=available_trades['availableTrades']
        )

if __name__ == '__main__':
    app.run(host='localhost', port=PORT, debug=True)