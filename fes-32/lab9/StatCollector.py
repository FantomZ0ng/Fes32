class StatCollector:
    def __init__(self):
        self.fields = {
            "Player": lambda soup: soup.find('h1', class_='summaryNickname text-ellipsis').get_text(strip=True),

            "Firepower": lambda soup: soup.find('div', class_="row-stats-section-score").contents[0].get_text(strip=True),

            "KPR": lambda soup: soup.find(
                'div', class_='role-stats-row stats-side-combined',
                attrs={'data-per-round-title': 'Kills per round'}
            ).get('data-original-value'),

            "Damage per round": lambda soup: soup.find(
                'div', class_='role-stats-row stats-side-combined',
                attrs={'data-per-round-title': 'Damage per round'}
            ).get('data-original-value'),

            "DPR/win": lambda soup: soup.find(
                'div', class_='role-stats-row stats-side-combined',
                attrs={'data-per-round-title': 'Damage per round win'}
            ).get('data-original-value'),

            "Rounds with kill": lambda soup: soup.find(
                'div', class_='role-stats-row stats-side-combined',
                attrs={'data-per-round-title': 'Rounds with a kill'}
            ).get('data-original-value'),

            "Rating 1.0": lambda soup: soup.find(
                'div', class_='role-stats-row stats-side-combined',
                title="HLTV's in-house formula for performance, taking into account Kills, Damage, Survival, Impact, and round-to-round consistency."
            ).find('div', class_='role-stats-data').get_text(strip=True),

            "Rounds with multi kill": lambda soup: soup.find(
                'div', class_='role-stats-row stats-side-combined',
                attrs={'data-per-round-title': 'Rounds with a multi-kill'}
            ).get('data-original-value'),

            "Pistol round rating": lambda soup: soup.find(
                'div', class_='role-stats-row stats-side-combined',
                title="Rating 1.0 in the first round of each half."
            ).find('div', class_='role-stats-data').get_text(strip=True)
        }

    def extract(self, soup):
        result = {}
        for key, extractor in self.fields.items():
            try:
                result[key] = extractor(soup)
            except AttributeError as e:
                print(f"Warning: Failed to extract '{key}': {e}")
        return result
