import csv
import time

# ==========================
# Load Data from CSV
# ==========================

records = []

with open("form-responses.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        records.append(row)

print(f"Total Records Loaded: {len(records)}")


# ==========================
# Sequential Search
# ==========================

def sequential_search(data, product_id):

    for record in data:
        if record["Product ID"] == product_id:
            return record

    return None


# ==========================
# Binary Search
# ==========================

sorted_records = sorted(records, key=lambda x: x["Product ID"])


def binary_search(data, product_id):

    low = 0
    high = len(data) - 1

    while low <= high:

        mid = (low + high) // 2

        current = data[mid]["Product ID"]

        if current == product_id:
            return data[mid]

        elif current < product_id:
            low = mid + 1

        else:
            high = mid - 1

    return None


# ==========================
# Product ID to Search
# ==========================

target = "PRD1005"


# ==========================
# Sequential Search Timing
# ==========================

start = time.perf_counter()

sequential_result = sequential_search(records, target)

end = time.perf_counter()

sequential_time = end - start


# ==========================
# Binary Search Timing
# ==========================

start = time.perf_counter()

binary_result = binary_search(sorted_records, target)

end = time.perf_counter()

binary_time = end - start


# ==========================
# Display Results
# ==========================

print("\n==============================")
print("Sequential Search")
print("==============================")
print(sequential_result)
print(f"Execution Time: {sequential_time:.10f} seconds")

print("\n==============================")
print("Binary Search")
print("==============================")
print(binary_result)
print(f"Execution Time: {binary_time:.10f} seconds")

print("\n==============================")
print("Performance Comparison")
print("==============================")

if sequential_time > binary_time:
    print("Binary Search is Faster")

elif binary_time > sequential_time:
    print("Sequential Search is Faster")

else:
    print("Both searches have approximately the same execution time")