from app.src.StatSheet import StatSheet


def is_sport_unique(statsheets: list[StatSheet]) -> bool:
    unique_sport: set[str] = set()
    for statsheet in statsheets:
        sport = statsheet.player.sport
        unique_sport.add(sport)
    return len(unique_sport) == 1
