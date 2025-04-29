from fastapi import FastAPI, Query
import requests
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# 네이버 API 인증 정보
NAVER_CLIENT_ID = "_MUs39d7RiLsvPw6kEAK"
NAVER_CLIENT_SECRET = "TO1beTvQkM"

# CORS 허용 (브라우저 호출용)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 모든 오리진 허용
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/search-blog")
def search_blog(query: str = Query(..., description="검색할 블로그 키워드")):
    """
    네이버 블로그 검색 프록시 API
    """
    url = "https://openapi.naver.com/v1/search/blog.json"
    headers = {
        "X-Naver-Client-Id": NAVER_CLIENT_ID,
        "X-Naver-Client-Secret": NAVER_CLIENT_SECRET
    }
    params = {
        "query": query,
        "display": 5  # 검색 결과 5개 가져오기
    }
    response = requests.get(url, headers=headers, params=params)
    return response.json()
