from typing import List
from ..interface import IngestorInterface
from ..quote_model import QuoteModel
from .docx_ingestor import DocxIngestor
from .csv_ingestor import CSVIngestor
from .txt_ingestor import TXTIngestor
from .pdf_ingestor import PDFIngestor


class Ingestor(IngestorInterface):
    ingestors = [DocxIngestor, CSVIngestor, TXTIngestor, PDFIngestor]

    @classmethod
    def parse(cls, path: str) -> List[IngestorInterface]:
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
