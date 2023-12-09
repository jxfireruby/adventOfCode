stats = {"J": 3, "H": 2}
del stats['J']
print(max(stats, key=stats.get))