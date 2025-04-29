from fastapi import FastAPI, Query
import requests
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS 허용
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

NAVER_CLIENT_ID = "여기 실제 ID"
NAVER_CLIENT_SECRET = "여기 실제 시크릿"

@app.get("/search-blog")
def search_blog(query: str):
    url = "https://openapi.naver.com/v1/search/blog.json"
    headers = {
        "X-Naver-Client-Id": NAVER_CLIENT_ID,
        "X-Naver-Client-Secret": NAVER_CLIENT_SECRET,
    }
    params = {
        "query": query,
        "display": 5,
        "start": 1
    }
    response = requests.get(url, headers=headers, params=params)
    return response.json()
