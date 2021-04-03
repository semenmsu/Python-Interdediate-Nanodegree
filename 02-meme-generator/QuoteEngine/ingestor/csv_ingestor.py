from typing import List
import pandas as pd
from ..interface import IngestorInterface
from ..quote_model import QuoteModel


class CSVIngestor(IngestorInterface):
    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[IngestorInterface]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quotes = []
        df = pd.read_csv(path, header=0)

        for index, row in df.iterrows():
            body, author = row['body'], row['author']
            quotes.append(QuoteModel(body, author))

        return quotes
