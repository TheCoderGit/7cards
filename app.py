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
                new_stack = engine.collect_cards(game_cards,'top')
                redist = engine.redistripute(new_stack)
                game_cards = redist
                engine.print_card_list(game_cards)
                values = engine.face_values(redist)
                return render_template('index.html', **values)
            elif engine.trials == 2:
                new_stack = engine.collect_cards(game_cards,'top')
                game_cards = new_stack
                engine.trials = 0
                return render_template('win.html',win=f"{engine.selected_card(game_cards)}")
        elif request.form.get('middle'):
            if engine.trials != 2:
                new_stack = engine.collect_cards(game_cards,'middle')
                redist = engine.redistripute(new_stack)
                game_cards = redist
                engine.print_card_list(game_cards)
                values = engine.face_values(redist)
                return render_template('index.html', **values)
            elif engine.trials == 2:
                new_stack = engine.collect_cards(game_cards,'middle')
                game_cards = new_stack
                
                engine.trials = 0
                return render_template('win.html',win=f"{engine.selected_card(game_cards)}")
        elif request.form.get('bottom'):
            if engine.trials != 2:
                new_stack = engine.collect_cards(game_cards,'bottom')
                redist = engine.redistripute(new_stack)
                game_cards = redist
                engine.print_card_list(game_cards)
                values = engine.face_values(redist)
                return render_template('index.html', **values)
            elif engine.trials == 2:
                new_stack = engine.collect_cards(game_cards,'bottom')
                game_cards = new_stack
                engine.trials = 0
                return render_template('win.html',win=f"{engine.selected_card(game_cards)}")


    game_cards = engine.start_new_game()
    values = engine.face_values(game_cards)
    return render_template('index.html', **values)

@app.route('/start/', methods=['POST'])
def start_button():
    global engine
    global game_cards
    game_cards = engine.start_new_game()
    values = engine.face_values(game_cards)
    return render_template('index.html', **values)

