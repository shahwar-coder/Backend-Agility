'''
SCENARIO:
A backend service processes incoming request IDs one at a time.
After each ID is produced, the function must pause and wait
until the next value is requested.

TASK:
Write a function `request_id_stream(ids)` that:
- Uses `yield` to return one request ID at a time
- Pauses execution after each `yield`
- Resumes from the same point on the next iteration

GOAL:
Understand how `yield` returns a value *and* preserves function state.
'''

from typing import Iterable, Generator
def request_id_stream(ids: Iterable)->Generator[str, None, None]:
    '''Yield request ids'''

    # if not ids: # Not this because empty data is generally acceptable to not break pipelines
    #     raise ValueError("No ids found")
    
    # if not isinstance(ids, List[str]): # Things like these are wrong, List[str] is a type hint, can't put up for type check
    #     raise ValueError("Request IDs should be string")

    # if not isinstance(ids, Iterable): # This is OVERDOING...Over-restricting input type
    #     raise ValueError("ids should be a list")

    if ids is None:
        raise ValueError("ids cannot be None")
    
    for request_id in ids:
        if not isinstance(request_id, str):
            # raise ValueError("Each ID should be a string") # Better to SKIP, than raise errors everytime.
            continue
        yield request_id


def main()->None:
    try:
        ids = [
            "9b2c4d1e-7a8f-4c12-9f3b-2e7a91c4d101",
            "3f1a9b88-1c4e-4d6b-9e22-71a3f9c2b055",
            "e8c4d2a1-5f3b-4a9c-8e11-3b7f9d1a4029",
        ]
        # ids = [] # sending this will help raise Error:...
        # ids = None # sending this will help raise Error:...
        for id in request_id_stream(ids):
            print(id)
    except Exception as err:
        print(f"Error: {err}")
    # Without TRy and EXCEPT you can see TRACEBACKS and Track Error. eg. 
                                        #     Traceback (most recent call last):
                                        #   File "/Users/shahwaralamnaqvi/Documents/Interview-Folder/Interview-Questions/Python/yield/02_.py", line 60, in <module>
                                        #     main()
                                        #     ~~~~^^
                                        #   File "/Users/shahwaralamnaqvi/Documents/Interview-Folder/Interview-Questions/Python/yield/02_.py", line 54, in main
                                        #     for id in request_id_streams(ids):
                                        #               ~~~~~~~~~~~~~~~~~~^^^^^
                                        #   File "/Users/shahwaralamnaqvi/Documents/Interview-Folder/Interview-Questions/Python/yield/02_.py", line 28, in request_id_streams
                                        #     raise ValueError("ids cannot be None")
                                        # ValueError: ids cannot be None
    # If you want clearer UX - Use TRY, EXCEPT inside main() eg. Error: ids cannot be None

if __name__=="__main__":
    main()


# 9b2c4d1e-7a8f-4c12-9f3b-2e7a91c4d101
# 3f1a9b88-1c4e-4d6b-9e22-71a3f9c2b055
# e8c4d2a1-5f3b-4a9c-8e11-3b7f9d1a4029

'''
# Key Points (Solution)
- Uses yield to return one request ID at a time.
- After each yield, function execution is paused.
- On the next iteration, execution resumes from the same point.
- Generator preserves local state automatically.
- Accepts any Iterable of IDs (list, tuple, stream, etc.).
- Skips invalid (non-string) IDs instead of failing the pipeline.
- Raises an error only for invalid boundaries (ids is None).

# Key Points (Understanding yield & State)
- yield returns a value AND suspends the function.
- Local variables and loop position are saved.
- Next call resumes exactly after the last yield.
- No re-execution from the top unless generator is recreated.

# Key Points (Why This Is Backend-Style)
- Matches request-by-request processing in servers.
- Prevents eager loading or pre-processing.
- Enables backpressure and controlled consumption.
- Ideal for queues, streams, and async pipelines.

# Key Points (Control Flow & Robustness)
- Empty iterable is acceptable and yields nothing.
- Invalid items are skipped, not fatal.
- Errors are raised only for truly invalid input (None).

# Important Note
- yield is not just “return multiple values”.
- It transforms the function into a stateful iterator.
- This pattern is foundational for streaming systems.
'''
