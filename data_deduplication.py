print("=== Data Deduplication System ===")

data = input("Enter items separated by commas: ")

items = data.split(",")

unique_items = []
for item in items:
    item = item.strip()
    if item and item not in unique_items:
        unique_items.append(item)

print("\nOriginal Data:", items)
print("Unique Data:", unique_items)
print("Duplicate items removed successfully!")