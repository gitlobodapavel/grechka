from flask import Flask, render_template, request, redirect
import web_parser


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/prices')
def prices():
    parsed_data = web_parser.parse()
    return render_template('prices.html', parsed_data = parsed_data)


if __name__ == '__main__':
    app.run(debug=True)