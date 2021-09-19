from io import TextIOWrapper
from app.src.Player import Player
from app.src.Stats import Stats
from app.src.StatSheet import StatSheet
from app.src.statcalc import avg_points

# This is the program's main function: the entry point.


def main():
    filepath = ''  # insert file path to your test file here.
    # the second argument is the mode that the interpreter will read the file in. r is for read-only
    f: TextIOWrapper = open(filepath, 'r')
    stats: list[str] = f.readlines()
    statsheets: list[StatSheet] = []
    for i in range(1, len(stats)):
        stat: str = stats[i]
        stat_details: list[str] = stat.split(',')
        id, name, number, sport = stat_details[:4]
        player: Player = Player(id, name, number, sport)
        points, assists, fouls = stat_details[4:]
        player_stats: Stats = Stats(points, assists, fouls)
        statsheet: StatSheet = StatSheet(player, player_stats)
        statsheets.append(statsheet)
    print(avg_points(statsheets))


# it is important to know what this syntax means as you are likely to see it a lot.
# when you run a command like this in your command prompt:
#
#   > python -m apps.src.main
#
# the python interpreter will start executing from the apps.src.main module. It is important to know that when the interpreter
# starts executing code in a module it assigns a special variable to the module called __name__. For all modules this will
# be given a value equal to the module name, except for when the module is the first executing module, in this case the
# __name__ variable will be assigned the special value: __main__
#
# so code like the below is regularly used to check whether this module is being executed directly (i.e., from the command
# promt) or as part of another module (i.e., through import)
if __name__ == '__main__':
    main()
