from fastapi import FastAPI, Query
import requests

# FastAPI 앱 생성
app = FastAPI(
    title="네이버 블로그 검색 프록시",
    description="네이버 블로그 검색 API를 사용한 프록시 서비스",
    version="0.1.0"
)

# 네이버 API 키
NAVER_CLIENT_ID = "_MUs39d7RiLsvPw6kEAK"
NAVER_CLIENT_SECRET = "TO1beTvQkM"

# 테스트용 루트 엔드포인트
@app.get("/")
async def root():
    """
    테스트용 루트 엔드포인트
    """
    return {"message": "네이버 블로그 검색 API 프록시가 작동 중입니다."}

# 블로그 검색 엔드포인트
@app.get("/blog-search")
async def blog_search(
    query: str = Query(..., description="검색할 키워드"),
    display: int = Query(5, description="검색 결과 개수 (기본값: 5)"),
    start: int = Query(1, description="검색 시작 위치 (기본값: 1)")
):
    """
    네이버 블로그를 검색합니다.
    
    - **query**: 검색할 키워드 (필수)
    - **display**: 검색 결과 개수 (기본값: 5)
    - **start**: 검색 시작 위치 (기본값: 1)
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
    
    # 네이버 API 요청
    response = requests.get(url, headers=headers, params=params)
    return response.json()

# 블로그 검색 상세 정보 엔드포인트
@app.get("/blog-search/detail")
async def blog_detail(
    blog_url: str = Query(..., description="블로그 URL")
):
    """
    블로그 URL에 대한 상세 정보를 제공합니다.
    
    - **blog_url**: 블로그 URL (필수)
    """
    return {"message": "블로그 URL 정보", "url": blog_url}
