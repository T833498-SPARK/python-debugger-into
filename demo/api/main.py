from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

def foo():
    return "bar"

@app.get("/test/")
def test_endpoint():
    value = foo()
    return "foo" + value
    