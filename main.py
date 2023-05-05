from typing import Union

import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/walking_skeleton")
async def read_root():
    return {"Walking": "Skeleton"}


if __name__ == "__main__":
    uvicorn.run("main:app", port=5000, log_level="info")
