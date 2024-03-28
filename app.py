from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

class Creature:
    def Twirl(self):
        return 'Twirl'

    def Leap(self):
        return 'Leap'

    def Spin(self):
        return 'Spin'


class Lox(Creature):
    pass


class Drako(Creature):
    pass


def perform_dance(creature1, move1, creature2, move2):
    if move1 == move2 == 'Twirl':
        return 'Fireflies light up the forest.'
    elif (move1, move2) in [('Leap', 'Spin'), ('Spin', 'Leap')]:
        return 'Gentle rain starts falling.'
    elif move1 == 'Spin' and move2 == 'Leap':
        return 'A rainbow appears in the sky.'
    else:
        return 'Other combinations create different effects that you can dream up.'


lox = Lox()
drako = Drako()

print(perform_dance(lox, lox.Twirl(), drako, drako.Spin()))    