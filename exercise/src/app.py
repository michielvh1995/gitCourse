from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


# this is an endpoint that yields the message "goodbye world" 
@app.get("/goodbye")
async def goodbye():
    return { "message": "Goodbye World" }


@app.post("/echo")
async def echo(message: str):
    return {"message": message}