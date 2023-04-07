from typing import Optional

import uvicorn
from fastapi import FastAPI
from NoobStuffs.libandroid import get_all_magisks, get_magisk

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "API is running."}


@app.get("/magisk/{type}")
async def magisk(type: Optional[str] = None):
    error = {"Error": "Version not found."}
    if not type:
        return error
    if type == "all":
        return get_all_magisks()
    try:
        return get_magisk(type)
    except Exception:
        return error


if __name__ == '__main__':
    uvicorn.run(app)
