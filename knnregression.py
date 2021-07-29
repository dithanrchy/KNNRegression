def minkowski_distance(x,y):
  return sum(abs(e1-e2) for e1, e2 in zip(x,y))

def sort_list(val,n):
  for i in range(len(val)):
    min = i;
    for j in range(i+1, len(val)):
      if val[j] < val[min]:
        min = j
    val[i], val[min] = val[min],val[i]
  return val[:n]

def get_index(val,n):
  sort_value = sort_list(list(val.values()),n)
  index = []
  for i in range(len(val)):
    if val[i] in sort_value:
      index.append(i)
    if len(index) == n:
      break
  return index

def sort_distance(X,t,n):
  distance = {}
  for j in range(len(X)):
    distance[j] = minkowski_distance(X[j],t)
  index = get_index(distance,n)

  return index

def get_y_value(y,index):
  total = 0
  for i in range(len(y)):
    if i in index:
      total += y[i]

  return total

def predict(X,y,T,n):
  total = []
  for i in range(len(T)):
    index = sort_distance(X,T[i],n)
    total.append((get_y_value(y,index))/n)
  return total
