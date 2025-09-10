from fastapi import FastAPI, Request, Response, Form
from starlette.middleware.sessions import SessionMiddleware

app = FastAPI()

# Add session middleware (handles cookie creation + signing)
app.add_middleware(SessionMiddleware, secret_key="super-secret-key")

@app.post("/login")
async def login(request: Request, username: str = Form(...)):
    # Set session data
    request.session["username"] = username
    return {"message": f"Logged in as {username}"}

@app.get("/profile")
async def profile(request: Request):
    # Retrieve session data
    username = request.session.get("username")
    if not username:
        return {"error": "Not logged in"}
    return {"username": username}

@app.post("/logout")
async def logout(request: Request):
    # Clear session
    request.session.clear()
    return {"message": "Logged out"}
