from basketball_reference_scraper.teams import get_roster, get_team_stats, get_opp_stats, get_roster_stats, \
    get_team_misc
from basketball_reference_scraper.players import get_stats, get_game_logs, get_player_headshot


scrap_failures = []


def get_config():
    import yaml

    with open('config.yml') as config_file:
        config_data = yaml.load(config_file, Loader=yaml.FullLoader)

    return config_data


def clean_player_name(name):
    return name.replace(" (TW)", "")


def scrap_roster(roster=None, suffixes=None):
    if roster is not None:
        for raw_player_name in roster["PLAYER"]:
            try:
                player_name = clean_player_name(raw_player_name)
                player_data = get_stats(player_name, suffixes=suffixes)
                print(player_data)
            except:
                scrap_failures.append(raw_player_name)


def run_scrapping(seasons=None, teams=None, suffixes=None):
    for season in seasons:
        for team in teams.values():
            roster = get_roster(team=team, season_end_year=season)
            scrap_roster(roster, suffixes=suffixes)


if __name__ == "__main__":
    config = get_config()
    seasons = config.get('seasons')
    teams = config.get('teams')
    suffixes = config.get('suffixes')

    run_scrapping(seasons=seasons, teams=teams, suffixes=suffixes)

    print(scrap_failures)
