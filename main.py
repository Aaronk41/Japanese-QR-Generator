from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
import qrcode
import os

app = FastAPI()

@app.get("/generate-qr/")
async def generate_qr(text: str, size: int = 10):
    try:
        # Generate QR with Japanese text support
        qr = qrcode.QRCode(version=1, box_size=size, border=5)
        qr.add_data(text)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        
        # Save temporarily
        img_path = "temp_qr.png"
        img.save(img_path)
        return FileResponse(img_path, media_type="image/png")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))