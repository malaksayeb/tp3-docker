import os, socket, time
from fastapi import FastAPI

app = FastAPI(title="TP3 API")
START = time.time()

@app.get("/")
def root():
    return {"message": "Bonjour depuis Docker", "host": socket.gethostname(),
            "env": os.getenv("APP_ENV", "dev")}

@app.get("/health")
def health():
    return {"status": "ok", "uptime_s": round(time.time() - START, 1)}
# test
# change
# change
# change
