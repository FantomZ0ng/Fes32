from StatCollector import StatCollector
from CsvWritter import CsvWriter
from PageFetcher import PageFetcher


class PlayerStatsParser:
    def __init__(self, output_file=None, headers=None, fields=None):
        self.output_file = output_file

        self.headers = headers or {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
            "Referer": "https://www.hltv.org/",
            "DNT": "1",
        }

        self.collector = StatCollector()
        if fields:
            self.collector.fields.update(fields)

        self.writer = CsvWriter()

    def parse(self, url):

        print(f"Fetching: {url}")

        fetcher = PageFetcher(url, headers=self.headers)
        soup = fetcher.fetch()

        if not soup:
            return

        data = self.collector.extract(soup)

        if not data:
            print('No data extracted.')
            return
        
        return data

    def save_csv(self, data):
        if data:

            self.writer.write_csv(self.output_file, data)
        else:
            print('Not parsed yet')
