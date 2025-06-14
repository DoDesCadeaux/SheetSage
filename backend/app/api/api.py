from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Welcome to the API from ROOT !"}


@app.get("/health")
def health():
    """Health check endpoint."""
    return {"status": "OK"}


@app.get("/ask")
def ask():
    """Endpoint to handle questions or requests."""
    return {"response": "This is a placeholder response for the ask endpoint."}
