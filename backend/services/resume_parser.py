import fitz  
import docx2txt
from fastapi import UploadFile

def parse_resume(file: UploadFile) -> str:
    filename = file.filename.lower()

    if filename.endswith(".pdf"):
        content = file.file.read()

        doc = fitz.open(stream=content, filetype="pdf")
        text = ""

        for page in doc:
            text += page.get_text()

   
        if not text.strip():
            raise RuntimeError(
                "No text could be extracted from this PDF. "
                "The resume may be scanned or image-based."
            )

        return text
    if filename.endswith(".docx"):
        file.file.seek(0)  
        text = docx2txt.process(file.file)

        if not text.strip():
            raise RuntimeError("No text found in DOCX file.")

        return text


    raise RuntimeError("Unsupported resume format")

