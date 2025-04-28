from fastapi import FastAPI, Query
import requests

# 여기에서 FastAPI 앱을 생성할 때 제목과 설명을 추가합니다
app = FastAPI(
    title="네이버 블로그 검색 API 프록시",
    description="네이버 블로그 검색 API를 사용하여 블로그 정보를 검색하는 서비스"
)

# 네이버 API 키 (현재 코드에서 사용하는 그대로 유지)
NAVER_CLIENT_ID = "_MUs39d7RiLsvPw6kEAK"
NAVER_CLIENT_SECRET = "TO1beTvQkM"

@app.get("/")
def read_root():
    """루트 경로입니다."""  # 이 주석은 API 문서에 표시됩니다
    return {"Hello": "World"}

@app.get("/blog-search")
def blog_search(
    query: str = Query(..., description="검색할 키워드"), 
    display: int = Query(5, description="검색 결과 개수"), 
    start: int = Query(1, description="검색 시작 위치")
):
    """
    네이버 블로그 검색 API 입니다.
    
    query 파라미터에 검색어를 입력하세요.
    """
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
