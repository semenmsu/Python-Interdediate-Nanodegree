from typing import List
from ..interface import IngestorInterface
from ..quote_model import QuoteModel


class TXTIngestor(IngestorInterface):
    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quotes = []
        with open(path, "r") as f:
            for line in f:
                if line:
                    parse = line.split('-')
                    body, author = parse[0], parse[1]
                    quotes.append(QuoteModel(body, author))
        return quotes
