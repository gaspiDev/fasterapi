from fastapi import FastAPI

app = FastAPI()


@app.get(path="/greet/{name}")
def greet(name: str) -> dict:
    return {"status": 200, "message": f"Greetings {name}."}
