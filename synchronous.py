import time

def brew_coffee():
    print("Brewing coffee...")
    time.sleep(5)
    print("Coffee is ready!")
    return "Coffee is ready"

def make_toast():
    print("Making toast...")
    time.sleep(3)
    print("Toast is ready!")
    return "Toast is ready"

def cook_eggs():
    print("Cooking eggs...")
    time.sleep(7)
    print("Eggs are ready!")
    return "Eggs are ready"

# In the syncronous version of the code, the functions are executed one after the other.
def main():
    time_start = time.time()
    result_coffee = brew_coffee()
    result_toast = make_toast()
    result_eggs = cook_eggs()
    time_end = time.time()
    print(result_coffee)
    print(result_toast)
    print(result_eggs)
    print(f"Breakfast is ready! Total time: {time_end - time_start:.2f} seconds.")

if __name__ == "__main__":
    main()