# ----------
# Data Types
# ----------

# int

a = 1
b = 33
c = a + b
print(c)


# str

a = "hello"
b = "world"
c = a + ' ' + b
print(c)

# list

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)
print(len(c))
print(c[0])
c.append(33)
print(c)
last = c.pop()
print(c[2:5])

# dict

d = {
  'name': 'Ali',
  'age': 33
}

print(d)
print(d['name'])
d['/'] = None
print(d)

print(d.keys())
print(d.values())

for k in d:
  print(k)

for k in d:
  print(d[k])

for k in d:
  print(f"{k}: {d[k]}")


for i in c:
  print(i)

for v in d.values():
  print(v)

for k, v in d.items():
  print(k, v)