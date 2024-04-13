from fastapi import FastAPI
app = FastAPI(title = "MLOPS")

@app.get("/")
async def home():
    return "<h2> this is simple app </h2>"

@app.get("/predict")
async def get_prediction(text: str):
    return 10
