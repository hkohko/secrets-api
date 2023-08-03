from uvicorn import run
from fastapi import FastAPI
from routers import send_password

app = FastAPI()
app.include_router(send_password.router)

@app.get("/")
async def welcome():
    return "Hello."

if __name__ == "__main__":
    run("main:app", port=1000, reload=True)