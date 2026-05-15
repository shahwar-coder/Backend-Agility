'''Read this for clear benefits
SCENARIO:
A backend pipeline validates data step by step.
As soon as a valid record is found, it should be sent forward
without finishing the entire function.

TASK:
Write a function `valid_record_stream(records)` that:
- Iterates over records
- Uses `yield` to emit each valid record immediately
- Continues execution from where it left off on the next call

GOAL:
Understand how `yield` replaces `return` for producing multiple values
over time instead of all at once.
'''

from typing import Iterable, Dict, Generator


REQUIRED_FIELDS = {"id", "email", "is_active"}


def valid_record_stream(records: Iterable[Dict[str, object]]) -> Generator[Dict[str, object], None, None]:
    """
    Stream valid records one by one.

    A record is considered valid if:
    - It is a dictionary
    - Required fields are present
    - email is a non-empty string
    - is_active is True
    """
    if records is None:
        raise ValueError("records cannot be None")

    for record in records:
        # ---- Type validation ----
        if not isinstance(record, dict):
            continue

        # ---- Required keys validation ----
        if not REQUIRED_FIELDS.issubset(record.keys()):
            continue

        record_id = record.get("id")
        email = record.get("email")
        is_active = record.get("is_active")

        # ---- Domain validation ----
        if not isinstance(record_id, str):
            continue

        if not isinstance(email, str) or not email.strip():
            continue

        if is_active is not True:
            continue

        # ---- Emit immediately ----
        yield record


def main() -> None:
    records = [
        {"id": "u101", "email": "", "is_active": True},
        {"id": "u102", "email": 12345, "is_active": True},
        {"id": "u103", "email": "alice@example.com", "is_active": True},
        {"id": "u104", "email": "bob@example.com", "is_active": False},
        {"id": "u105", "email": "carol@example.com", "is_active": True},
        {"email": "dave@example.com", "is_active": True},
        {"id": "u106", "email": "eve@example.com", "is_active": True},
    ]

    print("Valid records:")
    for valid in valid_record_stream(records):
        print(valid)


if __name__ == "__main__":
    main()

'''
# Key Points (What This Solution Demonstrates)
- Uses `yield` to emit valid records immediately.
- Does NOT wait for the entire dataset to be processed.
- Execution pauses after each `yield` and resumes from the same spot.
- Replaces the need for building and returning a full list.

# Key Points (Validation Flow)
- Skips non-dictionary records.
- Ensures required fields: id, email, is_active.
- Validates domain rules:
  - id must be a string
  - email must be a non-empty string
  - is_active must be True
- Invalid records are ignored safely (no pipeline break).

# Key Points (Why yield Instead of return)
- `return` → sends everything at once and ends the function.
- `yield` → sends one value and *remembers state*.
- Allows downstream consumers to start work immediately.
- Ideal for pipelines, validators, and streaming workflows.

# Key Points (Backend Benefits)
- Reduces latency (first valid record is available instantly).
- Memory efficient (no accumulation).
- Supports large or infinite streams.
- Matches real backend validation pipelines.

# Key Mental Model
- yield = "send now, pause, continue later"
- Generator = stateful iterator
- Validation + streaming = clean, scalable backend design
'''
