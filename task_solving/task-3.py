def count_words(s):
  d = {}
  if s  == "":
    return d 
lst = s.split()
for i in lst:
  if in d:
    d[i] = d[i]+1
  else:
    d[i] = 1
  return d

print(count_words("apple banana apple"))
print(count_words("word"))
print(count_words(""))
print(count_words("a a b"))
print(count_words("Hello hello"))
