import random

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

def calculate_score(hand):
    """Подсчет очков для руки."""
    total = sum(card[0] for card in hand)
    return total % 10

def determine_winner(player_score, banker_score):
    """Определение победителя."""
    if player_score > banker_score:
        return "PLAYER"
    elif banker_score > player_score:
        return "BANKER"
    else:
        return "TIE"