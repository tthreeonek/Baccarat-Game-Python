import sys
import os
from flask import Flask, render_template, request, redirect, url_for

# Добавляем путь к основной директории проекта в sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Импортируем функции и переменные из baccarat.py
from baccarat import deal_cards, calculate_score, determine_winner, M, F1, F, G, B, C, V, Q

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        num_players = request.form.get("players")
        if num_players:
            num_players = int(num_players)
            return redirect(url_for("players", num_players=num_players))
    return render_template("index.html")

@app.route("/players/<int:num_players>", methods=["GET", "POST"])
def players(num_players):
    if request.method == "POST":
        player_names = []
        for i in range(num_players):
            name = request.form.get(f"player{i+1}")
            if name:
                player_names.append(name)
        return redirect(url_for("game", player_names=",".join(player_names)))
    return render_template("players.html", num_players=num_players)

@app.route("/game/<player_names>", methods=["GET", "POST"])
def game(player_names):
    global M, F1, F, G, C, B

    player_names = player_names.split(",")
    num_players = len(player_names)
    for i in range(num_players):
        G[i] = player_names[i]
        M[i] = 10000

    if request.method == "POST":
        for i in range(num_players):
            F[i] = int(request.form.get(f"bet{i+1}", 0))
            F1[i] = int(request.form.get(f"choice{i+1}", 1))

        cards = deal_cards()
        for i in range(6):
            C[i] = cards[i][1]
            B[i] = cards[i][0]

        T1 = B[1] + B[2]
        T2 = B[3] + B[4]
        if T1 >= 10:
            T1 -= 10
        if T2 >= 10:
            T2 -= 10

        winner = "BANKER" if T2 > T1 else "PLAYER"

        for i in range(num_players):
            if F1[i] == (1 if winner == "BANKER" else 2):
                M[i] += F[i]
            else:
                M[i] -= F[i]

        return redirect(url_for("results", player_names=",".join(player_names)))

    return render_template("game.html", player_names=player_names)

@app.route("/results/<player_names>")
def results(player_names):
    player_names = player_names.split(",")
    num_players = len(player_names)
    results = []

    T1 = B[1] + B[2]
    T2 = B[3] + B[4]
    if T1 >= 10:
        T1 -= 10
    if T2 >= 10:
        T2 -= 10

    winner = "BANKER" if T2 > T1 else "PLAYER"

    for i in range(num_players):
        player_result = f"{G[i]} bet ${F[i]} on "
        player_result += "BANKER" if F1[i] == 1 else "PLAYER"
        if F1[i] == (1 if winner == "BANKER" else 2):
            player_result += f" and WON! Now has ${M[i]}."
        else:
            player_result += f" and LOST! Now has ${M[i]}."
        results.append(player_result)

    return render_template("results.html", results=results, winner=winner)

if __name__ == "__main__":
    app.run(debug=True)