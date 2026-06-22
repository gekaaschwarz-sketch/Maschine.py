# 021_sortieren.py
gewichte = [1500, 2500, 150, 400, 3000]

print("Originale Liste: " + str(gewichte))

# 1. Sortieren von klein nach groß
gewichte.sort()
print("Sortiert (leicht -> schwer): " + str(gewichte))

# 2. Sortieren von groß nach klein
gewichte.sort(reverse=True)
print("Sortiert (schwer -> leicht): " + str(gewichte))
