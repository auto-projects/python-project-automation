import os
import math
import pytest


def pytest_collection_modifyitems(session, config, items):
    current_worker = int(os.getenv("GITHUB_WORKER_ID", "1")) - 1
    total_workers = int(os.getenv("GITHUB_TOTAL_WORKERS", "1"))

    if total_workers > 1:
        tests_per_worker = math.ceil(len(items) / total_workers)
        start = current_worker * tests_per_worker
        end = start + tests_per_worker
        selected = items[start:end]
        deselected = items[:start] + items[end:]
        config.hook.pytest_deselected(items=deselected)
        items[:] = selected
