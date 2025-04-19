def DictInsert(dictionary,addition,insertposition):
  convert = list(dictionary.items())
  new = list(addition.items())[0]
  convert.insert(insertposition,new)
  return dict(convert)

#example
a = {"first": 1, "second" :2}

b = {"newfirst" : 0}

a = DictInsert(a,b,0)

print(a)
