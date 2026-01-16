'''Read this question and Solution for firm idea
SCENARIO:
A background job processes records in fixed-size batches to avoid
overloading downstream services.

TASK:
Write a generator function `batch_records(records, batch_size)` that:
- Accepts a list of records and an integer batch_size
- Yields records in batches of size batch_size
- Yields the remaining records if the last batch is smaller
'''

from typing import List, Dict, Generator


def batch_records(records: List[Dict], batch_size: int) -> Generator[List[Dict], None, None]:
    """
    Yield records in fixed-size batches.
    """
    if records is None:
        raise ValueError("Records cannot be None")

    if not isinstance(batch_size, int) or batch_size <= 0:
        raise ValueError("batch_size must be a positive integer")

    total = len(records)

    for start in range(0, total, batch_size):
        yield records[start : start + batch_size]


def main() -> None:
    records = [
        {"id": 1, "event": "user_signup"},
        {"id": 2, "event": "user_login"},
        {"id": 3, "event": "profile_update"},
        {"id": 4, "event": "password_change"},
        {"id": 5, "event": "user_logout"},
        {"id": 6, "event": "email_verification"},
        {"id": 7, "event": "subscription_renewal"},
    ]

    batch_size = 3

    for batch in batch_records(records, batch_size):
        print(batch)


if __name__ == "__main__":
    main()

# [{'id': 1, 'event': 'user_signup'}, {'id': 2, 'event': 'user_login'}, {'id': 3, 'event': 'profile_update'}]
# [{'id': 4, 'event': 'password_change'}, {'id': 5, 'event': 'user_logout'}, {'id': 6, 'event': 'email_verification'}]
# [{'id': 7, 'event': 'subscription_renewal'}]