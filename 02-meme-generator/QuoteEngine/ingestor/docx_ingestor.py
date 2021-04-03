from typing import List
import docx
from ..interface import IngestorInterface
from ..quote_model import QuoteModel


class DocxIngestor(IngestorInterface):
    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quotes = []
        doc = docx.Document(path)

        for para in doc.paragraphs:
            if para.text != "":
                parse = para.text.split('-')
                body, author = parse[0], parse[1]
                quotes.append(QuoteModel(body, author))

        return quotes
