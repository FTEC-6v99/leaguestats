from app.src.StatSheet import StatSheet
from app.src.utils import calc_avg
from app.src.validator import is_sport_unique


def avg_points(statsheets: list[StatSheet]) -> dict[int, float]:
    if len(statsheets) == 0:
        return {}
    if not is_sport_unique(statsheets):
        raise Exception('No more than one sport is allowed!')
    # group the stat sheet list by player_id
    player_to_stats: dict[int, list[StatSheet]] = {}
    for statsheet in statsheets:
        player_id: int = statsheet.player.id
        if player_id in player_to_stats.keys():
            player_to_stats.get(player_id).append(statsheet)
        else:
            player_to_stats[player_id] = [statsheet]
    player_to_avgpts: dict[int, float] = {}
    for player_id, stats in player_to_stats.items():
        points = [x.stats.points for x in stats]
        avg_pts = calc_avg(points)
        player_to_avgpts[player_id] = avg_pts
    return player_to_avgpts
