from flask import Flask, redirect, request
import random

app = Flask(__name__)


@app.route('/')
def index():
  return redirect("https://github.com/KrulYuno/Plazma-Burst-2-Randomizer", code=200)

@app.route('/player')
def player():
    if "players" in request.args:
        return random.choice(request.args.get("players").split(','))

@app.route('/randomize')
def randomize():
    return str(random.randrange(int(request.args.get("start", default="0")), int(request.args.get("stop", default="256"))))
   

if __name__ == '__main__':
  app.run(debug=True)