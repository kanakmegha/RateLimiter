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

