# Implement an in-memory rate limiter that allows N requests per user per T seconds
# Return T/F
# Requirements
# Function: allow_request(user_id) -> bool
# Configurable N and T
# If limit exceeded → return False

# Algorithm Name: Sliding Window Rate Limiter

import time
from collections import deque, defaultdict

# --- Configuration ---
N = 5   # Max requests
T = 10  # Seconds window

# In-memory storage: Maps user_id -> deque of timestamps
# Using defaultdict avoids checking if key exists
request_history = defaultdict(deque)

def allow_request(user_id):
    now = time.time()

    # 1. Retrieve the user's history
    user_timestamps = request_history[user_id]

    # 2. Cleanup: Remove timestamps that are older than T seconds (Sliding Window)
    # We check the left side (oldest) of the deque
    while user_timestamps and user_timestamps[0] <= now - T:
        user_timestamps.popleft()

    # 3. Check Capacity
    if len(user_timestamps) < N:
        # Limit not exceeded: Record this request and return True
        user_timestamps.append(now)
        return True
    else:
        # Limit exceeded
        return False

# --- Testing the implementation ---
if __name__ == "__main__":
    print(f"Config: {N} requests per {T} seconds")

    # Simulate 5 allowed requests
    for i in range(N):
        result = allow_request("user1")
        print(f"Request {i+1}: {result}") # Should be True

    # Simulate 1 blocked request immediately after
    result = allow_request("user1")
    print(f"Request {N+1} (Immediate): {result}") # Should be False

    # Simulate waiting for the window to pass
    print("Waiting for window to slide...")
    time.sleep(T + 0.1)

    # Simulate request after wait
    result = allow_request("user1")
    print(f"Request After Wait: {result}") # Should be True
