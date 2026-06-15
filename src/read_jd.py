from docx import Document

doc = Document("data/job_description.docx")

for paragraph in doc.paragraphs:
    print(paragraph.text)