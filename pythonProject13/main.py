from flask import Flask, render_template
import json

app = Flask(__name__)


def load_serials():
    with open('serials.json', 'r', encoding='utf-8') as file:
        serials_data = json.load(file)
    return serials_data


def load_films():
    with open('films.json', 'r', encoding='utf-8') as file:
        films_data = json.load(file)
    return films_data


@app.route('/')
def menu():
    return render_template('menu.html', title="Главная страница")


@app.route('/films')
def films():
    films_data = load_films()
    return render_template('films.html', films=films_data, title="Фильмы")


@app.route('/serials')
def serials_page():
    serials_data = load_serials()
    return render_template('serials.html', serials=serials_data, title="Сериалы")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5200)