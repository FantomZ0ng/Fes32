from string import ascii_uppercase
from PlayerStatsParser import PlayerStatsParser


class PlayersParser(PlayerStatsParser):
    def __init__(self, output_file, headers=None, fields=None):
        super().__init__(output_file, headers, fields)

        self.collector.fields = fields or {
            'link': lambda soup: [
                a.get('href') for a in soup
                .find('div', class_='players-archive-grid')
                .find_all('a', href=lambda u: u and u.startswith('/player/'))
        ]
    }

    def parse(self):

        urls = [f'https://www.hltv.org/players/{i}' for i in ascii_uppercase[:1]]

        return {'link': [link for url in urls for link in super().parse(url).get('link', [])]}
