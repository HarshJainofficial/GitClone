# Loading the PDF document first
from src.loader import PDFLoader

loader = PDFLoader()
text = loader.load("data/Company_Policy.pdf")
print(text[:500])