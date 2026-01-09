from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from rate_limiter import SlidingWindowRateLimiter

app = FastAPI()

rate_limiter = SlidingWindowRateLimiter(
    max_requests=10,
    window_seconds=60
)

@app.middleware("http")
async def rate_limit_middleware(request: Request, call_next):
    client_ip = request.client.host

    allowed, current_count = rate_limiter.allow_request(client_ip)
    remaining = max(0, rate_limiter.max_requests - current_count)

    if not allowed:
        return JSONResponse(
            status_code=429,
            content={"detail": "Too Many Requests"},
            headers={
                "X-RateLimit-Limit": str(rate_limiter.max_requests),
                "X-RateLimit-Remaining": "0"
            }
        )

    response = await call_next(request)

    response.headers["X-RateLimit-Limit"] = str(rate_limiter.max_requests)
    response.headers["X-RateLimit-Remaining"] = str(remaining)

    return response

@app.get("/")
def home():
    return {"message": "Rate limited API is working 🚀"}
