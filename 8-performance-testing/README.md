# Module 8 - Performance Testing

**Goal**: Learn to load test applications and measure performance

## Context

Performance testing ensures your application can handle expected load. Types:

- **Load testing** - normal expected load
- **Stress testing** - beyond normal capacity
- **Endurance testing** - sustained load over time

Note: This exercise uses the Flask app from Module 4 (E2E).

## Steps

1. Start the Flask app from Module 4:
   ```bash
   cd ../4-e2e && python app.py
   ```
2. Install Locust: `pip install locust`
3. Open `locustfile.py` and examine its structure
4. Run Locust:
   ```bash
   locust -f locustfile.py --host=http://127.0.0.1:5000
   ```
5. Open http://localhost:8089 in browser
6. Configure:
   - Number of users: 10
   - Spawn rate: 2 users/second
   - Run for 1 minute
7. Run the test and observe results
8. Check the charts - response times, requests/second, failures

## Key Metrics

- **RPS** - Requests per second
- **p50/p95/p99** - Response time percentiles
- **Failure rate** - Percentage of failed requests
- **Avg response time** - Mean response time

## Challenge

- Add more endpoints to the locustfile (subtract, multiply, divide)
- Increase load to 50 users
- Identify the breaking point
- Compare response times between endpoints

## Vojica Injac
