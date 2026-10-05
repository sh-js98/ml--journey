def word_count(text):
    words = text.split()
    counts={}
    for word in words:
        if word in counts:
            counts[word] +=1
        else:
            counts[word] = 1

    return counts
def dedupe(word_list):
    result = []
    for item in word_list:
        if item not in result:
                result.append(item)
    return result
def transpose(matrix):
     result = []
     for col in range(len(matrix[0])):
          new_row = []
          for row in matrix:
                new_row.append(row[col])
          result.append(new_row)
     return result
def merge_dicts(d1, d2):
     result = dict(d1)
     for key in d2:
         if key in result:
           result[key] += d2[key]
         else:
           result[key] = d2[key]
     return result   

result = word_count("I like coding and I like coffee & coffee")
print(result)
print(dedupe([3, 3, 5, 5, 3, 1,5]))
print(transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

d1 = {'apples': 2, 'banana': 1}
d2 = {'apples': 3, 'orange': 1}
result = merge_dicts(d1, d2)
print(result)