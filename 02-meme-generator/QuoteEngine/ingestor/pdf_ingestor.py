import subprocess
from io import StringIO
from typing import List
import docx
from ..interface import IngestorInterface
from ..quote_model import QuoteModel


class PDFIngestor(IngestorInterface):
    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')
        quotes = []
        p = subprocess.Popen(["pdftotext", "-raw", path, "-"],
                             stdout=subprocess.PIPE)
        output, err = p.communicate()
        p_status = p.wait()
        for line in StringIO(output.decode('utf-8')):
            values = line.split("-")
            if len(values) >= 2:
                body, author = values[0], values[1]
                quotes.append(QuoteModel(body, author))
        return quotes
