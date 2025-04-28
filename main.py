from fastapi import FastAPI, Query
import requests

app = FastAPI()

NAVER_CLIENT_ID = "_MUs39d7RiLsvPw6kEAK"
NAVER_CLIENT_SECRET = "TO1beTvQkM"

@app.get("/blog-search")
def blog_search(query: str = Query(...), display: int = 5, start: int = 1):
    url = "https://openapi.naver.com/v1/search/blog.json"
    headers = {
        "X-Naver-Client-Id": NAVER_CLIENT_ID,
        "X-Naver-Client-Secret": NAVER_CLIENT_SECRET
    }
    params = {
        "query": query,
        "display": display,
        "start": start
    }
    response = requests.get(url, headers=headers, params=params)
    return response.json()
