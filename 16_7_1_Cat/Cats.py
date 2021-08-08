from class_Cat import Cat


cat_1 = Cat('Baron', 'man', 2)
cat_2 = Cat('Sam', 'man', 2)

print()
for key, value in cat_1.getDescription().items():
  print("{0}: {1}".format(key, value))

print()

for key, value in cat_2.getDescription().items():
  print("{0}: {1}".format(key, value))
