
given = ['flower','flow','flight']
# given = ["dog","racecar","car"]
given = ["car","cir"]

shortest_word = min(given, key=len)
word_count = len(given)

# print (shortest_word)
# print(len(shortest_word))
# print(len(given))

nested = []

# Creating nested array, represents each word and its charecters
for i in range(word_count):
    nested.append([])
    for j in range(len(given[i])):
        var = list(given[i])
        nested[i].append(var[j])

# print(nested)

lcp = []
red_flag = 0

for i in range(len(shortest_word)):
    if red_flag == 1:
        break
    store = []
    temp_match1 = nested[0][i]
    for j in range(word_count):
        temp_match2 = nested[j][i]
        print(j,i)
        if temp_match1 != temp_match2:
            red_flag = 1
            print("break")
            break
        else:
            store.append(temp_match1)
            print(store)

    # print(store)

    if len(store) == word_count:
        lcp.append(store[0])

# print(lcp)

if lcp:
    lcp = "".join(lcp)
    return_lcp = lcp
    print(return_lcp)
else:
    return_empty = ""
    print(return_empty)





