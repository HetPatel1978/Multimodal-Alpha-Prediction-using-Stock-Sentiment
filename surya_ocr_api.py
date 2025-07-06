from fastapi import FastAPI, UploadFile, File
from surya_ocr import SuryaOCR

app = FastAPI()
ocr = SuryaOCR()

@app.post("/ocr")
async def extract_text(file: UploadFile = File(...)):
    content = await file.read()
    result = ocr.read_bytes(content)
    return {"text": result}
