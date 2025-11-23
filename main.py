from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import feedparser
import requests
import subprocess
import os

app = FastAPI()

templates = Jinja2Templates(directory="templates")

RSS_FEED_URL = "https://static.cricinfo.com/rss/livescores.xml"

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    # Get directory listing
    try:
        # For Windows, use 'dir'. For Linux/macOS, use 'ls -l'.
        command = "dir" if os.name == "nt" else "ls -l"
        process = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            check=True
        )
        dir_output = process.stdout
    except subprocess.CalledProcessError as e:
        dir_output = f"Error executing command: {e}"
    except FileNotFoundError:
        dir_output = "Command not found."

    return templates.TemplateResponse("index.html", {"request": request, "dir_listing": dir_output})

@app.get("/api/scores")
async def get_scores():
    response = requests.get(RSS_FEED_URL)
    feed = feedparser.parse(response.content)
    return {"scores": feed.entries}
