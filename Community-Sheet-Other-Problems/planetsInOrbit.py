from collections import Counter

def distraction(n, planets):
    orbit = Counter(planets)
    count = 0
    for planet in orbit:
        if orbit.get(planet) > 1:            
            count += min(n, orbit.get(planet))
        else:
            count += 1
    return count


testCases = int(input())
for i in range(testCases):
    size, n = list(map(int, input().split(" ")))
    planets = list(map(int, input().split(" ")))
    print(distraction(n, planets))

