from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"Welcome to my API!"}

def foo():
    return "bar"

@app.get("/test")
def test_endpoint():
    my_name = {"name": "Richard"}
    my_role = {"position": "MLE"}
    return my_name | my_role
    