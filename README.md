# Rate Limiter from Scratch (Redis-free)

A production-inspired **rate limiter built from scratch** using **Python + FastAPI**, without Redis or any external database.

This project demonstrates how rate limiting works internally, the concurrency challenges involved, and why distributed systems rely on Redis in real-world deployments.

---

## What This Project Does

- Implements a **Sliding Window Rate Limiting algorithm**
- Enforces **per-IP request limits**
- Uses **in-memory storage**
- Is **concurrency-safe**
- Exposes rate limit information via HTTP headers
- Includes a **load test simulating 1000 concurrent requests**

---

## Why This Matters

Most developers *use* rate limiters.
Few understand **how they work internally**.

This project helps you understand:
- Time window algorithms
- Concurrency problems
- Middleware behavior in FastAPI
- Why in-memory solutions fail at scale
- Why Redis is the industry standard

This is a **backend interview favorite**.

---

## Tech Stack

- Python 3.11+
- FastAPI
- Uvicorn
- Standard library only (no Redis, no DB)

---

## Project Structure

RateLimiter/
- main.py  
  FastAPI application and rate limiting middleware

- rate_limiter.py  
  Sliding Window rate limiter implementation

- load_test.py  
  Simulates 1000 concurrent requests

- requirements.txt  
  Project dependencies

---

## Rate Limiting Strategy

### Sliding Window Algorithm

For each client (IP address):

1. Maintain a list of request timestamps
2. Remove timestamps older than the configured time window
3. If the number of remaining requests exceeds the limit, reject the request
4. Otherwise, allow the request and store the current timestamp

This approach avoids burst issues common in fixed window algorithms.

---

## Configuration

The rate limiter is configured with:

- Maximum requests: 10
- Time window: 60 seconds
- Scope: Per IP address

These values can be modified in main.py.

---

## Running the Application

Install dependencies:

pip install -r requirements.txt

Start the server:

uvicorn main:app --reload

The API will be available at:

http://127.0.0.1:8000

---

## Rate Limit Headers

Successful responses include:

X-RateLimit-Limit: 10  
X-RateLimit-Remaining: <remaining_requests>

Blocked responses return:

HTTP 429 Too Many Requests  
X-RateLimit-Remaining: 0

---

## Load Testing

A simple load test is included to simulate concurrent traffic.

Run:

python3 load_test.py

Expected output:

200 OK: 10  
429: 990

This confirms that the rate limiter correctly enforces limits under concurrent load.

---

## Implementation Notes

- Uses in-memory storage with deque for efficient operations
- Uses threading.Lock to prevent race conditions
- Implemented as FastAPI middleware
- Returns HTTP 429 responses directly from middleware

---

## Limitations

- In-memory only; data is lost on restart
- Not suitable for multi-instance deployments
- Lock contention under heavy load

These limitations explain why production systems typically use Redis-based rate limiting.

---

## Future Improvements

- Token Bucket algorithm
- Async-safe implementation
- Per-user or per-route limits
- Redis-backed distributed rate limiter
- Metrics and observability

