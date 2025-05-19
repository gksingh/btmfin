import concurrent.futures
import time
import random

def getInputA():
    print("Fetching data from API A...")
    time.sleep(10)  # Simulating delay
    print("Data received from API A")
    return "DataA"

def getInputB():
    print("Fetching data from API B...")
    time.sleep(5)  # Simulating longer delay
    print("Data received from API B")
    return "DataB"

def processData():
    print("Starting parallel execution of getInputA and getInputB...")
    
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_a = executor.submit(getInputA)
        future_b = executor.submit(getInputB)
        
        dataA = future_a.result()  # Waits for getInputA to complete
        dataB = future_b.result()  # Waits for getInputB to complete
    
    print(f"Processing received data: {dataA} and {dataB}")
    print("Processing completed.")

# Run the process
processData()
