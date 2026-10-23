from pypdf import PdfReader

class PDFLoader:
    def load(self, file_path: str):
        reader = PdfReader(file_path)
        return reader
    