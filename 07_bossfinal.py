def sumv(v1, v2):
    vector3 = []
    for a, b in zip(v1, v2):
        vector3.append(a + b)
    return vector3

vector1 = [80, 100, 19, 312, 1, 3, 99]
vector2 = [1, 199, 12, 15, 10, 20, 30]

print(sumv(vector1, vector2))