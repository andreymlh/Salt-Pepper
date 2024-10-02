'''
Разработать методы для программы Камень-Ножницы-Бумага.
Метод rps_game_winner должен принимать на вход массив следующей структуры
[ ["player1", "P"], ["player2", "S"] ], где P - бумага, S - ножницы, R - камень, и
функционировать следующим образом:
• если количество игроков больше 2 необходимо вызывать исключение
WrongNumberOfPlayersError
• если ход игроков отличается от ‘R’, ‘P’ или ‘S’ необходимо вызывать
исключение NoSuchStrategyError
• в иных случаях необходимо вернуть имя и ход победителя, если оба
игрока походили одинаково - выигрывает первый игрок.

Тесты для примеров и проверки:
rps_game_winner([['player1', 'P'], ['player2', 'S'], ['player3', 'S']]) #
=> WrongNumberOfPlayersError
rps_game_winner([['player1', 'P'], ['player2', 'A']]) #
=> NoSuchStrategyError
rps_game_winner([['player1', 'P'], ['player2', 'S']]) #
=> 'player2 S'
rps_game_winner([['player1', 'P'], ['player2', 'P']]) #
=> 'player1 P'
'''
class WrongNumberOfPlayersError(Exception):
    pass

class NoSuchStrategyError(Exception):
    pass

def rps_game_winner(players):
    # Проверяем количество игроков
    if len(players) != 2:
        raise WrongNumberOfPlayersError("Количество игроков должно быть ровно 2.")
    
    player1, player2 = players[0], players[1]
    name1, strategy1 = player1[0], player1[1]
    name2, strategy2 = player2[0], player2[1]
    
    # Проверяем, корректны ли стратегии
    valid_strategies = {'R', 'P', 'S'}
    if strategy1 not in valid_strategies or strategy2 not in valid_strategies:
        raise NoSuchStrategyError("Неверная стратегия.")
    
    # Определяем победителя
    if strategy1 == strategy2:
        return f'{name1} {strategy1}'
    
    if (strategy1 == 'R' and strategy2 == 'S') or \
       (strategy1 == 'P' and strategy2 == 'R') or \
       (strategy1 == 'S' and strategy2 == 'P'):
        return f'{name1} {strategy1}'
    else:
        return f'{name2} {strategy2}'

# Тесты
try:
    print(rps_game_winner([['player1', 'P'], ['player2', 'S'], ['player3', 'S']]))  
except WrongNumberOfPlayersError as e:
    print(e)

try:
    print(rps_game_winner([['player1', 'P'], ['player2', 'A']]))  
except NoSuchStrategyError as e:
    print(e)

print(rps_game_winner([['player1', 'P'], ['player2', 'S']]))  
print(rps_game_winner([['player1', 'P'], ['player2', 'P']]))  
