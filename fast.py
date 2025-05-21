# This file is part of the FastAPI project.
from fastapi import FastAPI

app = FastAPI()
@app.get("/")
async def read_root():
    return {"Hello": "World"}
if __name__ == "__main__":
    app.run()