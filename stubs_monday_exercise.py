import os
import random
from datetime import datetime


# ============================================================
# INSTRUCTIONS
# ============================================================
# Each function below has a dependency problem.
# It reaches out to something external that your test cannot control.
#
# For each function:
#   1. Fix the function so the dependency can be injected
#   2. Write a test that passes every time
#
# Your fix must:
#   - add a parameter with default None
#   - use the real dependency only if the parameter is None
#
# Submit this file to Blackboard via GitHub link when done.
# ============================================================


# ------------------------------------------------------------
# Exercise 1 -- datetime dependency
# ------------------------------------------------------------
# This function checks whether a store is open based on the
# current time. A test that calls it without controlling the
# time will pass sometimes and fail sometimes.
#
# Fix: add a parameter so the time can be injected.
# Then write test_store_open() and test_store_closed() below.

def get_store_status(now=None):   # added `now=None` so a datetime can be injected
    if now is None:               # if nothing is injected, use the real clock
        now = datetime.now()
    hour = now.hour
    if 9 <= hour < 21:
        return "Store is open"
    else:
        return "Store is closed"


def test_store_open():
    assert get_store_status(now=datetime(2025, 1, 1, 12, 0, 0)) == "Store is open"    # injected noon

def test_store_closed():
    assert get_store_status(now=datetime(2025, 1, 1, 23, 0, 0)) == "Store is closed"  # injected 11 PM


# ------------------------------------------------------------
# Exercise 2 -- random dependency
# ------------------------------------------------------------
# This function assigns a student to a study group at random.
# A test that calls it without controlling randomness cannot
# assert a specific result reliably.
#
# Fix: add a parameter so the random source can be injected.
# Then write test_assign_study_group() below.
# Use == to assert an exact value -- not "result in [...]"

def assign_study_group(random_source=None):  # added `random_source=None` so randomness can be injected
    if random_source is None:                 # if nothing is injected, use the real random module
        random_source = random
    return random_source.choice(["Group A", "Group B", "Group C"])

def test_assign_study_group():
    class FakeRandom:                                                   # fake random that always returns the first option
        def choice(self, options):
            return options[0]
    assert assign_study_group(random_source=FakeRandom()) == "Group A"  # inject fake, assert exact value


# ------------------------------------------------------------
# Exercise 3 -- environment variable dependency
# ------------------------------------------------------------
# This function returns an API URL based on an environment
# variable. A test that calls it without controlling the
# environment cannot predict which URL it gets back.
#
# Fix: add a parameter so the env value can be injected.
# Then write test_api_url_production() and
# test_api_url_staging() below.

def get_api_url(env=None):       # added env=None so the environment can be injected
    if env is None:              # if nothing is injected, read the real environment variable
        env = os.getenv("APP_ENV")
    if env == "production":
        return "https://api.example.com"
    else:
        return "https://staging.example.com"

def test_api_url_production():
    assert get_api_url(env="production") == "https://api.example.com"   # injected "production" directly

def test_api_url_staging():
    assert get_api_url(env="staging") == "https://staging.example.com"  # injected "staging" directly
