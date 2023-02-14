import base64
from random import randint, choice

from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"

@app.route('/')
def main():
    return "Миссия Колонизация Марса"

@app.route('/promotion')
def promotion():
    promotions = ['Человечество вырастает из детства.', 'Человечеству мала одна планета.',
           'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!', 'Присоединяйся!']
    return '</br>'.join(promotions)


@app.route('/astronaut_selection', methods=['GET', 'POST'])
def astronaut_selection():
    if request.method == 'GET':
        with open('templates/astronaut_selection.html', 'r', encoding='utf-8') as astronaut_selection:
            return astronaut_selection.read()
    elif request.method == 'POST':
        pass


@app.route('/promotion_image')
def promotion_image():
    with open('templates/promotion_image.html', 'r', encoding='utf-8') as promotion_image:
        return promotion_image.read()

@app.route('/choice/<planet_name>')
def choice(planet_name):
    planets = {'Марс': ['Эта планета близка к Земле;', 'На ней много необходимых ресурсов;',
                        'На ней есть небольшое магнитное поле;', 'Наконец, она просто красива!'],
               'Земля': ['Эта планета заселена людьми;', 'На ней много необходимых ресурсов;',
                        'На ней есть вода и атмосфера;', 'Наконец, она просто красива!'],
               'Венера': ['Эта планета близка к Земле;', 'На ней много необходимых ресурсов;',
                        'На ней есть небольшое магнитное поле;', 'Наконец, она просто красива!'],
               'Юпитер': ['Эта планета далека от Земли;', 'На ней много необходимых ресурсов;',
                          'Наконец, она просто красива!'],
               'Сатурн': ['Эта планета далека от Земли;', 'На ней много необходимых ресурсов;',
                        'На ней есть небольшое магнитное поле;', 'Наконец, она просто красива!'],
               'Меркурий': ['Эта планета близка к Земле;', 'На ней много необходимых ресурсов;',
                        'Планета очень мала;', 'Наконец, она просто красива!']
               }
    return render_template('choice.html', planet_name=planet_name, planet=planets[planet_name],
                           size=randint(1, 6))


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    return render_template('results.html', nickname=nickname, level=level, rating=rating)


@app.route('/load_photo', methods=['GET', 'POST'])
def load_photo():
    if request.method == 'GET':
        return render_template('load_photo.html', photo='')
    elif request.method == 'POST':
        f = request.files['file']
        return render_template('load_photo.html', photo=base64.b64encode(f.read()))


@app.route('/carousel')
def carousel():
    return render_template('carousel.html')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')