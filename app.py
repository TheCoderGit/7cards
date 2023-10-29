from flask import Flask, render_template, request, session
from game_engine import Card, CardTypes, Engine

app = Flask(__name__)

engine = Engine()
game_cards = []

@app.route('/',methods=['POST','GET'])
def index():
    global engine
    global game_cards

    if request.method == 'POST':
        if request.form.get('top'):
            if engine.trials != 2:
                print('top pressed')
                print('create new stack')
                new_stack = engine.collect_cards(game_cards,'top')
                print('collect the cards')
                redist = engine.redistripute(new_stack)
                game_cards = redist
                print('redistribute')
                values = engine.face_values(redist)
                print('prepare the face values')
                return render_template('index.html', **values)
            elif engine.trials == 2:
                new_stack = engine.collect_cards(game_cards,'top')
                game_cards = new_stack
                selected_card = engine.selected_card(game_cards)
                engine.trials = 0
                return render_template('win.html',win=f"{selected_card.value}\n{selected_card.type.value}")
        elif request.form.get('middle'):
            if engine.trials != 2:
                print('middle pressed')
                print('create new stack')
                new_stack = engine.collect_cards(game_cards,'middle')
                print('collect the cards')
                redist = engine.redistripute(new_stack)
                game_cards = redist
                print('redistribute')
                values = engine.face_values(redist)
                print('prepare the face values')
                return render_template('index.html', **values)
            elif engine.trials == 2:
                new_stack = engine.collect_cards(game_cards,'middle')
                game_cards = new_stack
                selected_card = engine.selected_card(game_cards)
                engine.trials = 0
                return render_template('win.html',win=f"{selected_card.value}\n{selected_card.type.value}")
        elif request.form.get('bottom'):
            if engine.trials != 2:
                print('bottom pressed')
                print('create new stack')
                new_stack = engine.collect_cards(game_cards,'bottom')
                print('collect the cards')
                redist = engine.redistripute(new_stack)
                game_cards = redist
                print('redistribute')
                values = engine.face_values(redist)
                print('prepare the face values')
                return render_template('index.html', **values)
            elif engine.trials == 2:
                new_stack = engine.collect_cards(game_cards,'bottom')
                game_cards = new_stack
                selected_card = engine.selected_card(game_cards)
                engine.trials = 0
                return render_template('win.html',win=f"{selected_card.value}\n{selected_card.type.value}")


    game_cards = engine.start_new_game()
    print('start new cards for the game')
    values = engine.face_values(game_cards)
    print('prepare the face values')
    return render_template('index.html', **values)

@app.route('/start/', methods=['POST'])
def start_button():
    global engine
    global game_cards
    game_cards = engine.start_new_game()
    values = engine.face_values(game_cards)
    return render_template('index.html', **values)

