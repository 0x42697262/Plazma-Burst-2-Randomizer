from flask import Flask, redirect, request
import random

app = Flask(__name__)


@app.route('/')
def index():
  return redirect("https://github.com/KrulYuno/Plazma-Burst-2-Randomizer", code=200)

@app.route('/player', methods = ['POST'])
def player():
    if "players" in request.args:
        return random.choice(list(filter(None, request.args.get('players').split(','))))

if __name__ == '__main__':
  app.run(debug=False)
