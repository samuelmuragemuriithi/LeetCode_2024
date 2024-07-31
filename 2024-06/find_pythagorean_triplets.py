def find_pythagorean_triplets(N):
    triplets = []
    for a in range(1, N):
        for b in range(a, N):
            c = N - a - b
            if c > 0:
                if a * a + b * b == c * c:
                    triplets.append([a, b, c])
    return triplets

# Test the function with N = 1000
N = 1000
triplets = find_pythagorean_triplets(N)
print(triplets)
