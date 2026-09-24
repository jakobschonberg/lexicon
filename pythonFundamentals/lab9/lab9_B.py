#B1
class Document:
    def __init__(self, title):
        self.title = title

    def describe(self):
        return "This is a document"

#B2, B3
class PDFDocument(Document):
    def __init__(self, title):
        super().__init__(title)

    def describe(self):
        return "This is a PDF document"

class TextDocument(Document):
    def __init__(self, title):
        super().__init__(title)

    def describe(self):
        return "This is a text document"

#B4
documents = [
    PDFDocument("CV"),
    PDFDocument("Cover Letter"),
    TextDocument("TODO List")
]

#B5
for document in documents:
    print(document.title, " - ", document.describe())