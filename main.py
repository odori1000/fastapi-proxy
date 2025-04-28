from fastapi import FastAPI, Query, HTTPException
import requests

# 확실한 앱 인스턴스 생성
app = FastAPI(
    title="네이버 블로그 검색 API",
    description="네이버 블로그 검색을 위한 API 프록시 서비스",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# 네이버 API 인증 정보
NAVER_CLIENT_ID = "_MUs39d7RiLsvPw6kEAK"
NAVER_CLIENT_SECRET = "TO1beTvQkM"

# 루트 경로 정의
@app.get("/", tags=["기본"])
async def root():
    """
    기본 환영 메시지를 반환합니다.
    """
    return {"message": "네이버 블로그 검색 API에 오신 것을 환영합니다!"}

# 블로그 검색 API 엔드포인트
@app.get("/api/blog-search", tags=["블로그"])
async def blog_search(
    query: str = Query(..., description="검색할 키워드"),
    display: int = Query(5, ge=1, le=100, description="검색 결과 개수 (1-100)"),
    start: int = Query(1, ge=1, le=1000, description="검색 시작 위치 (1-1000)")
):
    """
    네이버 블로그 검색 API를 사용하여 블로그 포스트를 검색합니다.
    
    - **query**: 검색할 키워드
    - **display**: 검색 결과 개수 (기본값: 5, 최대 100)
    - **start**: 검색 시작 위치 (기본값: 1, 최대 1000)
    """
    # 네이버 API 엔드포인트
    url = "https://openapi.naver.com/v1/search/blog.json"
    
    # 헤더 설정
    headers = {
        "X-Naver-Client-Id": _MUs39d7RiLsvPw6kEAK,
        "X-Naver-Client-Secret": TO1beTvQkM
    }
    
    # 파라미터 설정
    params = {
        "query": query,
        "display": display,
        "start": start
    }
    
    try:
        # API 요청
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # 오류 상태 코드 확인
        return response.json()
    except requests.RequestException as e:
        # 오류 처리
        raise HTTPException(status_code=500, detail=f"네이버 API 요청 실패: {str(e)}")

# 헬스 체크 엔드포인트
@app.get("/health", tags=["시스템"])
async def health_check():
    """
    API 서버의 상태를 확인합니다.
    """
    return {"status": "healthy"}
