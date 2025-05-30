from PlayersParser import PlayersParser
from PlayerStatsParser import PlayerStatsParser


# Даний код парсить сторінку https://www.hltv.org/stats/players/922/snappi та записує атрибути в csv файл
# Його буде розширено для різних гравців та збільшено кількість атрибутів. Можливо потрібно використати інший підхід до парсингу сторінок


def main():
    output_file = './lab9/result.csv'

    users_parser = PlayersParser(output_file)
    data = users_parser.parse()
    users_parser.save_csv(data)

    output_file = './lab9/uresult.csv'
    user_parser = PlayerStatsParser(output_file)
    
    for i in data['link']:
        stats = user_parser.parse(
            f"https://www.hltv.org/stats{i.replace('player', 'players')}"
        )
        user_parser.save_csv(stats)

    


if __name__ == '__main__':
    main()
