from app.src.Player import Player
from app.src.Stats import Stats
from app.src.StatSheet import StatSheet
from app.src.statcalc import avg_points


def main():
    filepath = 'D:\\Users\\mab105120\\Desktop\\leaguestats\\resources\\player_stats.txt'
    f = open(filepath, 'r')
    stats = f.readlines()
    statsheets: list[StatSheet] = []
    for i in range(1, len(stats)):
        stat = stats[i]
        stat_details = stat.split(',')
        id, name, number, sport = stat_details[:4]
        player = Player(id, name, number, sport)
        points, assists, fouls = stat_details[4:]
        player_stats = Stats(points, assists, fouls)
        statsheet = StatSheet(player, player_stats)
        statsheets.append(statsheet)
    print(avg_points(statsheets))


if __name__ == '__main__':
    main()
