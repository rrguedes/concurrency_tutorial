# Description: This file demonstrates how to use async functions in Python. We will use the asyncio library to create async functions and run them in the main function.
import time
import asyncio

async def brew_coffee() -> str:
    print("Brewing coffee...")
    # time.sleep(5)  Note that not all functions are waitable. Thus, we use asyncio.sleep() instead of time.sleep()
    await asyncio.sleep(5) # await means that the following code is waitable, and the function brew_coffee can be paused and resumed later. This is a coroutine function.
    print("Coffee is ready!")
    # an async function does not return a value, but a coroutine object. there is something else we need to do to get the return value. Take a look at the main function.
    return "Coffee is ready"

async def make_toast() -> str:
    print("Making toast...")
    await asyncio.sleep(3)
    print("Toast is ready!")
    return "Toast is ready"

async def cook_eggs() -> str:
    print("Cooking eggs...")
    await asyncio.sleep(7)
    print("Eggs are ready!")
    return "Eggs are ready"

# In the syncronous version of the code, the functions are executed one after the other.
# Note that we have changed main() to an async function. This is because we are using await in the main function.
async def main():
    time_start = time.time()
    # result_coffee = await asyncio.create_task(brew_coffee())
    # result_toast = await asyncio.create_task(make_toast())
    # resulst_eggs = await asyncio.create_task(cook_eggs())

    # you can also call all the functions in a batch, which in my tests produced better results compared to the method above
    result_coffee, result_toast, resulst_eggs = await asyncio.gather(brew_coffee(), make_toast(), cook_eggs())

    time_end = time.time()
    print(result_coffee)
    print(result_toast)
    print(resulst_eggs)
    print(f"Breakfast is ready! Total time: {time_end - time_start:.2f} seconds.")

if __name__ == "__main__":
    # Likewise, the way we run the main function is different. We use asyncio.run() to run the main function.
    # asyncio.run() creates a event loop and runs the provided function, and closes the loop when the function is done.
    # You may understand the loop as watcher that checks for pauses and resumes in the async functions.
    asyncio.run(main()) # asyncio.run() is the entry point for running an async function. It creates a new event loop, runs the provided function, and closes the loop when the function is done.