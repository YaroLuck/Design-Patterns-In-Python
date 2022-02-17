"A Leaderboard Singleton Class"


class Leaderboard():
    "The Leaderboard as a Singleton"
    _table = {}

    def __new__(cls):
        return cls

    @classmethod
    def _print(cls):
        "A class level method"
        print("-----------Leaderboard-----------")
        for key, value in sorted(cls._table.items()):
            print('fdfd')
            # print(f'|\t{key}\t|\t{value}\t|')
            # print(f'|{key}|{value}|')
        print()

    @classmethod
    def add_winner(cls, position, name):
        "A class level method"
        cls._table[position] = name
