from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

# Глобальные переменные
M = [0] * 20  # Деньги игроков
F1 = [0] * 20  # Выбор игрока (банкир или игрок)
F = [0] * 20  # Ставки игроков
G = [""] * 20  # Имена игроков
B = [""] * 13  # Названия карт
V = [0] * 13  # Значения карт
A = ["SPADES", "HEARTS", "DIAMONDS", "CLUBS"]  # Масти
Z = [[0 for _ in range(10)] for _ in range(9)]  # Таблица правил для банкира
W = [0] * 10  # Таблица правил для игрока
Q = [[0 for _ in range(13)] for _ in range(4)]  # Счетчик карт в колоде
C = [""] * 6  # Карты на столе

# Данные для карт
B = ["ACE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE", "TEN", "JACK", "QUEEN", "KING"]
V = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0]

# Таблица правил для банкира
Z = [
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

# Таблица правил для игрока
W = [0, 1, 1, 1, 1, 1, 1, 1, 0, 1]


def deal_cards():
    """Раздача карт."""
    global Q
    cards = []
    for _ in range(6):
        while True:
            suit = random.randint(0, 3)
            rank = random.randint(0, 12)
            if Q[suit][rank] < 32:
                Q[suit][rank] += 1
                cards.append((V[rank], f"{B[rank]} OF {A[suit]}"))
                break
    return cards


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Получаем количество игроков из формы
        num_players = request.form.get("players")
        if num_players:
            num_players = int(num_players)  # Преобразуем в число
            # Перенаправляем на страницу с игроками
            return redirect(url_for("players", num_players=num_players))
    return render_template("index.html")


@app.route("/players/<int:num_players>", methods=["GET", "POST"])
def players(num_players):
    if request.method == "POST":
        # Получаем имена игроков из формы
        player_names = []
        for i in range(num_players):
            name = request.form.get(f"player{i+1}")
            if name:
                player_names.append(name)
        # Перенаправляем на игру
        return redirect(url_for("game", player_names=",".join(player_names)))
    return render_template("players.html", num_players=num_players)


@app.route("/game/<player_names>", methods=["GET", "POST"])
def game(player_names):
    global M, F1, F, G, C, B

    # Инициализация игроков
    player_names = player_names.split(",")
    num_players = len(player_names)
    for i in range(num_players):
        G[i] = player_names[i]
        M[i] = 10000

    if request.method == "POST":
        # Обработка ставок и выбора игроков
        for i in range(num_players):
            F[i] = int(request.form.get(f"bet{i+1}", 0))
            F1[i] = int(request.form.get(f"choice{i+1}", 1))

        # Раздача карт
        cards = deal_cards()
        for i in range(6):
            C[i] = cards[i][1]
            B[i] = cards[i][0]

        # Подсчет очков
        T1 = B[1] + B[2]
        T2 = B[3] + B[4]
        if T1 >= 10:
            T1 -= 10
        if T2 >= 10:
            T2 -= 10

        # Определение победителя
        if T2 > T1:
            winner = "BANKER"
        else:
            winner = "PLAYER"

        # Обновление денег игроков
        for i in range(num_players):
            if F1[i] == (1 if winner == "BANKER" else 2):
                M[i] += F[i]
            else:
                M[i] -= F[i]

        # Перенаправление на результаты
        return redirect(url_for("results", player_names=",".join(player_names)))

    return render_template("game.html", player_names=player_names)


@app.route("/results/<player_names>")
def results(player_names):
    player_names = player_names.split(",")
    num_players = len(player_names)
    results = []

    # Определение победителя
    T1 = B[1] + B[2]
    T2 = B[3] + B[4]
    if T1 >= 10:
        T1 -= 10
    if T2 >= 10:
        T2 -= 10

    if T2 > T1:
        winner = "BANKER"
    else:
        winner = "PLAYER"

    # Формирование результатов
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