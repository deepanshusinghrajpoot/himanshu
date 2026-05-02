# Python – Deep Copy of List (handles nested lists/objects)

import copy   # import copy module for deepcopy
import json   # optional: for JSON-based deep copy

# Original list with nested structures
original_list = [1, 2, [3, 4], {"a": 5}]






# 1️⃣ Using copy.deepcopy() – handles any nested objects
deep_copy1 = copy.deepcopy(original_list)
deep_copy1[2][0] = 99      # modifying copy
deep_copy1[3]["a"] = 100

print("Original List:", original_list)   # [1, 2, [3, 4], {'a': 5}]
print("Deep Copy 1  :", deep_copy1)     # [1, 2, [99, 4], {'a': 100}]







# 2️⃣ Using list comprehension – only works for 1-level nested lists
shallow_list = [[1, 2], [3, 4]]
deep_copy2 = [sublist[:] for sublist in shallow_list]
deep_copy2[0][0] = 99

print("Original Shallow:", shallow_list)  # [[1, 2], [3, 4]]
print("Deep Copy 2      :", deep_copy2)   # [[99, 2], [3, 4]]











# 3️⃣ Using JSON serialization – works for JSON-serializable elements
deep_copy3 = json.loads(json.dumps(original_list))
deep_copy3[2][0] = 777
deep_copy3[3]["a"] = 888

print("Original List (JSON):", original_list)  # [1, 2, [3, 4], {'a': 5}]
print("Deep Copy 3 (JSON) :", deep_copy3)      # [1, 2, [777, 4], {'a': 888}]

# ✅ Best Practice:
# Use copy.deepcopy() for any nested lists/objects.
# Use list comprehension for shallow 1-level nested lists (faster).
# JSON method only for JSON-serializable data.
