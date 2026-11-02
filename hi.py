
arr = [40, 50, 30, 40, 50, 30, 30]

freq = {}

# Count frequency of each element
for x in arr:
    freq[x] = freq.get(x, 0) + 1

maxcount = 0
res = None

# Find the most frequent element
for x in freq:
    if freq[x] > maxcount or (freq[x] == maxcount and (res is None or x > res)):
        maxcount = freq[x]
        res = x

print("Most frequent element:", res)

