from fastapi import FastAPI

app = FastAPI(title="DevOps Practice API")




@app.get("/")
def home():
    return {"message": "Hello! My DevOps journey starts here."}


@app.get("/health")
def health():
    return {"status": "healthy"}