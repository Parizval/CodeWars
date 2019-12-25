def order(sentence):
  words = sentence.split(" ")
  strings = []
  for i in range(1,10):
    for j in words:
        if str(i) in j : strings.append(j)
  return " ".join(strings)