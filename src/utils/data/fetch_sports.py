import requests

    # https://gist.github.com/akeaswaran/b48b02f1c94f873c6655e7129910fc3b
    # https://github.com/pseudo-r/Public-ESPN-API

    # NFL (9/5 - 2/14)
        # https://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard

    # college football (8/24 - 1/21)
        # https://site.api.espn.com/apis/site/v2/sports/football/college-football/scoreboard

    # NBA (10/4 - 6/23)
        # https://site.api.espn.com/apis/site/v2/sports/basketball/nba/scoreboard
    
    # MLB (3/20 - 11/2)
        # https://site.api.espn.com/apis/site/v2/sports/baseball/mlb/scoreboard
    
    # Golf (on thursday-sunday)
        # https://site.api.espn.com/apis/site/v2/sports/golf/pga/scoreboard
    
    # UFC (only on fight week)
        # https://site.api.espn.com/apis/site/v2/sports/mma/ufc/scoreboard
    
    # college basketball (11/4 - 4/5)
        # https://site.api.espn.com/apis/site/v2/sports/basketball/mens-college-basketball/scoreboard
    
    # favorites
        # http://site.api.espn.com/apis/site/v2/sports/football/college-football/teams/2132
        # http://site.api.espn.com/apis/site/v2/sports/basketball/mens-college-basketball/teams/2132
        # http://site.api.espn.com/apis/site/v2/sports/football/nfl/teams/9
        # http://site.api.espn.com/apis/site/v2/sports/basketball/nba/teams/14
        # http://site.api.espn.com/apis/site/v2/sports/baseball/mlb/teams/19

def get_period_suffix(period):
    if 10 <= period % 100 <= 20:
        suffix = 'th'
    else:
        suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(period % 10, 'th')
    return suffix

def fetch_cincinnati_football():
    url = "http://site.api.espn.com/apis/site/v2/sports/football/college-football/teams/2132"
    response = requests.get(url)
    data = response.json()

    game = data['team']['nextEvent'][0]['competitions'][0]
    home_team = game['competitors'][0]['team']['displayName']
    home_team_logo = game['competitors'][0]['team'].get('logos', [{}])[0].get('href', '')
    away_team = game['competitors'][1]['team']['displayName']
    away_team_logo = game['competitors'][1]['team'].get('logos', [{}])[0].get('href', '')
    game_status = game['status']['type']['state']

    if game_status in ['in', 'post']:
        score = f"{game['competitors'][0]['score']['displayValue']} - {game['competitors'][1]['score']['displayValue']}"
        clock = game['status']['displayClock']
        period = game['status']['period']
        period = f"{period}{get_period_suffix(period)} Quarter"
        return {
            "home_team": home_team,
            "home_team_logo": home_team_logo,
            "away_team": away_team,
            "away_team_logo": away_team_logo,
            "is_game_playing_or_completed": True,
            "is_game_still_playing": game_status == 'in',
            "score": score,
            "clock": clock,
            "period": period
        }
    else:
        game_time = game['date']
        return {
            "home_team": home_team,
            "home_team_logo": home_team_logo,
            "away_team": away_team,
            "away_team_logo": away_team_logo,
            "is_game_playing_or_completed": False,
            "is_game_still_playing": False,
            "game_time": game_time,
            "game_date": game_time.split("T")[0]
        }

def fetch_cincinnati_basketball():
    url = "http://site.api.espn.com/apis/site/v2/sports/basketball/mens-college-basketball/teams/2132"
    response = requests.get(url)
    data = response.json()

    game = data['team']['nextEvent'][0]['competitions'][0]
    home_team = game['competitors'][0]['team']['displayName']
    home_team_logo = game['competitors'][0]['team'].get('logos', [{}])[0].get('href', '')
    away_team = game['competitors'][1]['team']['displayName']
    away_team_logo = game['competitors'][1]['team'].get('logos', [{}])[0].get('href', '')
    game_status = game['status']['type']['state']

    if game_status in ['in', 'post']:
        score = f"{game['competitors'][0]['score']['displayValue']} - {game['competitors'][1]['score']['displayValue']}"
        clock = game['status']['displayClock']
        period = game['status']['period']
        period = f"{period}{get_period_suffix(period)} Half"
        return {
            "home_team": home_team,
            "home_team_logo": home_team_logo,
            "away_team": away_team,
            "away_team_logo": away_team_logo,
            "is_game_playing_or_completed": True,
            "is_game_still_playing": game_status == 'in',
            "score": score,
            "clock": clock,
            "period": period
        }
    else:
        game_time = game['date']
        return {
            "home_team": home_team,
            "home_team_logo": home_team_logo,
            "away_team": away_team,
            "away_team_logo": away_team_logo,
            "is_game_playing_or_completed": False,
            "is_game_still_playing": False,
            "game_time": game_time,
            "game_date": game_time.split("T")[0]
        }

def fetch_packers():
    url = "http://site.api.espn.com/apis/site/v2/sports/football/nfl/teams/9"
    response = requests.get(url)
    data = response.json()

    game = data['team']['nextEvent'][0]['competitions'][0]
    home_team = game['competitors'][0]['team']['displayName']
    home_team_logo = game['competitors'][0]['team'].get('logos', [{}])[0].get('href', '')
    away_team = game['competitors'][1]['team']['displayName']
    away_team_logo = game['competitors'][1]['team'].get('logos', [{}])[0].get('href', '')
    game_status = game['status']['type']['state']

    if game_status in ['in', 'post']:
        score = f"{game['competitors'][0]['score']['displayValue']} - {game['competitors'][1]['score']['displayValue']}"
        clock = game['status']['displayClock']
        period = game['status']['period']
        period = f"{period}{get_period_suffix(period)} Quarter"
        return {
            "home_team": home_team,
            "home_team_logo": home_team_logo,
            "away_team": away_team,
            "away_team_logo": away_team_logo,
            "is_game_playing_or_completed": True,
            "is_game_still_playing": game_status == 'in',
            "score": score,
            "clock": clock,
            "period": period
        }
    else:
        game_time = game['date']
        return {
            "home_team": home_team,
            "home_team_logo": home_team_logo,
            "away_team": away_team,
            "away_team_logo": away_team_logo,
            "is_game_playing_or_completed": False,
            "is_game_still_playing": False,
            "game_time": game_time,
            "game_date": game_time.split("T")[0]
        }

def fetch_dodgers():
    url = "http://site.api.espn.com/apis/site/v2/sports/baseball/mlb/teams/19"
    response = requests.get(url)
    data = response.json()

    game = data['team']['nextEvent'][0]['competitions'][0]
    home_team = game['competitors'][0]['team']['displayName']
    home_team_logo = game['competitors'][0]['team'].get('logos', [{}])[0].get('href', '')
    away_team = game['competitors'][1]['team']['displayName']
    away_team_logo = game['competitors'][1]['team'].get('logos', [{}])[0].get('href', '')
    game_status = game['status']['type']['state']

    if game_status in ['in', 'post']:
        score = f"{game['competitors'][0]['score']['displayValue']} - {game['competitors'][1]['score']['displayValue']}"
        clock = game['status']['displayClock']
        period = game['status']['period']
        period = f"{period}{get_period_suffix(period)} Inning"
        return {
            "home_team": home_team,
            "home_team_logo": home_team_logo,
            "away_team": away_team,
            "away_team_logo": away_team_logo,
            "is_game_playing_or_completed": True,
            "is_game_still_playing": game_status == 'in',
            "score": score,
            "clock": clock,
            "period": period
        }
    else:
        game_time = game['date']
        return {
            "home_team": home_team,
            "home_team_logo": home_team_logo,
            "away_team": away_team,
            "away_team_logo": away_team_logo,
            "is_game_playing_or_completed": False,
            "is_game_still_playing": False,
            "game_time": game_time,
            "game_date": game_time.split("T")[0]
        }

def fetch_heat():
    url = "http://site.api.espn.com/apis/site/v2/sports/basketball/nba/teams/14"
    response = requests.get(url)
    data = response.json()

    game = data['team']['nextEvent'][0]['competitions'][0]
    home_team = game['competitors'][0]['team']['displayName']
    home_team_logo = game['competitors'][0]['team'].get('logos', [{}])[0].get('href', '')
    away_team = game['competitors'][1]['team']['displayName']
    away_team_logo = game['competitors'][1]['team'].get('logos', [{}])[0].get('href', '')
    game_status = game['status']['type']['state']

    if game_status in ['in', 'post']:
        score = f"{game['competitors'][0]['score']['displayValue']} - {game['competitors'][1]['score']['displayValue']}"
        clock = game['status']['displayClock']
        period = game['status']['period']
        period = f"{period}{get_period_suffix(period)} Quarter"
        return {
            "home_team": home_team,
            "home_team_logo": home_team_logo,
            "away_team": away_team,
            "away_team_logo": away_team_logo,
            "is_game_playing_or_completed": True,
            "is_game_still_playing": game_status == 'in',
            "score": score,
            "clock": clock,
            "period": period
        }
    else:
        game_time = game['date']
        return {
            "home_team": home_team,
            "home_team_logo": home_team_logo,
            "away_team": away_team,
            "away_team_logo": away_team_logo,
            "is_game_playing_or_completed": False,
            "is_game_still_playing": False,
            "game_time": game_time,
            "game_date": game_time.split("T")[0]
        }

def fetch_favorites():
    cincinnati_football_info = fetch_cincinnati_football()
    cincinnati_basketball_info = fetch_cincinnati_basketball()
    packers_info = fetch_packers()
    dodgers_info = fetch_dodgers()
    heat_info = fetch_heat()

    return [
        cincinnati_football_info,
        cincinnati_basketball_info,
        packers_info,
        dodgers_info,
        heat_info
    ]

def fetch_nfl_scores():
    url = "https://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard"
    response = requests.get(url)
    data = response.json()

    games_info = []

    for event in data['events']:
        game = event['competitions'][0]
        home_team = game['competitors'][0]['team']['displayName']
        home_team_logo = game['competitors'][0]['team']['logo']
        away_team = game['competitors'][1]['team']['displayName']
        away_team_logo = game['competitors'][1]['team']['logo']
        game_status = game['status']['type']['state']

        if game_status in ['in', 'post']:
            score = f"{game['competitors'][0]['score']} - {game['competitors'][1]['score']}"
            clock = game['status']['displayClock']
            period = game['status']['period']
            period = f"{period}{get_period_suffix(period)} Quarter"
            game_info = {
                "home_team": home_team,
                "home_team_logo": home_team_logo,
                "away_team": away_team,
                "away_team_logo": away_team_logo,
                "is_game_playing_or_completed": True,
                "is_game_still_playing": game_status == 'in',
                "score": score,
                "clock": clock,
                "period": period
            }
        else:
            game_time = game['date']
            game_info = {
                "home_team": home_team,
                "home_team_logo": home_team_logo,
                "away_team": away_team,
                "away_team_logo": away_team_logo,
                "is_game_playing_or_completed": False,
                "is_game_still_playing": False,
                "game_time": game_time,
                "game_date": game_time.split("T")[0]
            }

        games_info.append(game_info)

    return games_info

def fetch_ncaaf_scores():
    url = "https://site.api.espn.com/apis/site/v2/sports/football/college-football/scoreboard"
    response = requests.get(url)
    data = response.json()

    games_info = []

    for event in data['events']:
        game = event['competitions'][0]
        home_team = game['competitors'][0]['team']['displayName']
        home_team_logo = game['competitors'][0]['team']['logo']
        home_team_rank = game['competitors'][0].get('curatedRank', {}).get('current', None)
        away_team = game['competitors'][1]['team']['displayName']
        away_team_logo = game['competitors'][1]['team']['logo']
        away_team_rank = game['competitors'][1].get('curatedRank', {}).get('current', None)
        game_status = game['status']['type']['state']

        if game_status in ['in', 'post']:
            score = f"{game['competitors'][0]['score']} - {game['competitors'][1]['score']}"
            clock = game['status']['displayClock']
            period = game['status']['period']
            period = f"{period}{get_period_suffix(period)} Quarter"
            game_info = {
                "home_team": home_team,
                "home_team_logo": home_team_logo,
                "home_team_rank": home_team_rank,
                "away_team": away_team,
                "away_team_logo": away_team_logo,
                "away_team_rank": away_team_rank,
                "is_game_playing_or_completed": True,
                "is_game_still_playing": game_status == 'in',
                "score": score,
                "clock": clock,
                "period": period
            }
        else:
            game_time = game['date']
            game_info = {
                "home_team": home_team,
                "home_team_logo": home_team_logo,
                "home_team_rank": home_team_rank,
                "away_team": away_team,
                "away_team_logo": away_team_logo,
                "away_team_rank": away_team_rank,
                "is_game_playing_or_completed": False,
                "is_game_still_playing": False,
                "game_time": game_time,
                "game_date": game_time.split("T")[0]
            }

        games_info.append(game_info)

    return games_info

def fetch_ncaam_scores():
    url = "https://site.api.espn.com/apis/site/v2/sports/basketball/mens-college-basketball/scoreboard"
    response = requests.get(url)
    data = response.json()

    games_info = []

    for event in data['events']:
        game = event['competitions'][0]
        home_team = game['competitors'][0]['team']['displayName']
        home_team_logo = game['competitors'][0]['team'].get('logo', '')
        home_team_rank = game['competitors'][0].get('curatedRank', {}).get('current', None)
        away_team = game['competitors'][1]['team']['displayName']
        away_team_logo = game['competitors'][1]['team'].get('logo', '')
        away_team_rank = game['competitors'][1].get('curatedRank', {}).get('current', None)
        game_status = game['status']['type']['state']

        if (home_team_rank is not None and home_team_rank <= 98) or (away_team_rank is not None and away_team_rank <= 98):
            if game_status in ['in', 'post']:
                score = f"{game['competitors'][0]['score']} - {game['competitors'][1]['score']}"
                clock = game['status']['displayClock']
                period = game['status']['period']
                period = f"{period}{get_period_suffix(period)} Half"
                game_info = {
                    "home_team": home_team,
                    "home_team_logo": home_team_logo,
                    "home_team_rank": home_team_rank,
                    "away_team": away_team,
                    "away_team_logo": away_team_logo,
                    "away_team_rank": away_team_rank,
                    "is_game_playing_or_completed": True,
                    "is_game_still_playing": game_status == 'in',
                    "score": score,
                    "clock": clock,
                    "period": period
                }
            else:
                game_time = game['date']
                game_info = {
                    "home_team": home_team,
                    "home_team_logo": home_team_logo,
                    "home_team_rank": home_team_rank,
                    "away_team": away_team,
                    "away_team_logo": away_team_logo,
                    "away_team_rank": away_team_rank,
                    "is_game_playing_or_completed": False,
                    "is_game_still_playing": False,
                    "game_time": game_time,
                    "game_date": game_time.split("T")[0]
                }

            games_info.append(game_info)

    return games_info

def fetch_nba_scores():
    url = "https://site.api.espn.com/apis/site/v2/sports/basketball/nba/scoreboard"
    response = requests.get(url)
    data = response.json()

    games_info = []

    for event in data['events']:
        game = event['competitions'][0]
        home_team = game['competitors'][0]['team']['displayName']
        home_team_logo = game['competitors'][0]['team'].get('logo', '')
        away_team = game['competitors'][1]['team']['displayName']
        away_team_logo = game['competitors'][1]['team'].get('logo', '')
        game_status = game['status']['type']['state']

        if game_status in ['in', 'post']:
            score = f"{game['competitors'][0]['score']} - {game['competitors'][1]['score']}"
            clock = game['status']['displayClock']
            period = game['status']['period']
            period = f"{period}{get_period_suffix(period)} Quarter"
            game_info = {
                "home_team": home_team,
                "home_team_logo": home_team_logo,
                "away_team": away_team,
                "away_team_logo": away_team_logo,
                "is_game_playing_or_completed": True,
                "is_game_still_playing": game_status == 'in',
                "score": score,
                "clock": clock,
                "period": period
            }
        else:
            game_time = game['date']
            game_info = {
                "home_team": home_team,
                "home_team_logo": home_team_logo,
                "away_team": away_team,
                "away_team_logo": away_team_logo,
                "is_game_playing_or_completed": False,
                "is_game_still_playing": False,
                "game_time": game_time,
                "game_date": game_time.split("T")[0]
            }

        games_info.append(game_info)

    return games_info

def fetch_mlb_scores():
    url = "https://site.api.espn.com/apis/site/v2/sports/baseball/mlb/scoreboard"
    response = requests.get(url)
    data = response.json()

    games_info = []

    for event in data['events']:
        game = event['competitions'][0]
        home_team = game['competitors'][0]['team']['displayName']
        home_team_logo = game['competitors'][0]['team'].get('logo', '')
        away_team = game['competitors'][1]['team']['displayName']
        away_team_logo = game['competitors'][1]['team'].get('logo', '')
        game_status = game['status']['type']['state']

        if game_status in ['in', 'post']:
            score = f"{game['competitors'][0]['score']} - {game['competitors'][1]['score']}"
            clock = game['status']['displayClock']
            period = game['status']['period']
            period = f"{period}{get_period_suffix(period)} Inning"
            game_info = {
                "home_team": home_team,
                "home_team_logo": home_team_logo,
                "away_team": away_team,
                "away_team_logo": away_team_logo,
                "is_game_playing_or_completed": True,
                "is_game_still_playing": game_status == 'in',
                "score": score,
                "clock": clock,
                "period": period
            }
        else:
            game_time = game['date']
            game_info = {
                "home_team": home_team,
                "home_team_logo": home_team_logo,
                "away_team": away_team,
                "away_team_logo": away_team_logo,
                "is_game_playing_or_completed": False,
                "is_game_still_playing": False,
                "game_time": game_time,
                "game_date": game_time.split("T")[0]
            }

        games_info.append(game_info)

    return games_info

def fetch_ufc_scores():
    url = "https://site.api.espn.com/apis/site/v2/sports/mma/ufc/scoreboard"
    response = requests.get(url)
    data = response.json()

    fights_info = []

    for event in data['events']:
        for competition in event['competitions']:
            fight_info = {
                "fighters": [],
                "is_fight_completed": competition['status']['type']['state'] == 'post'
            }

            for competitor in competition['competitors']:
                full_name = competitor['athlete']['fullName']
                name_parts = full_name.split()
                first_name = name_parts[0]
                last_name = name_parts[-1]
                formatted_name = f"{first_name[0]}. {last_name}"
                fighter_info = {
                    "name": formatted_name,
                    "record": competitor['records'][0]['summary'],
                    "flag": competitor['athlete']['flag']['href']
                }
                if fight_info["is_fight_completed"]:
                    fighter_info["winner"] = competitor.get('winner', False)
                fight_info["fighters"].append(fighter_info)

            if not fight_info["is_fight_completed"]:
                fight_info["date_time"] = competition['date']

            fights_info.append(fight_info)

    return fights_info