from fastapi import FastAPI

app = FastAPI(title="Student API")

# TODO: add your data model and API routes here


@app.get("/")
def read_root():
    return {"message": "Welcome to the API"}
