def is_not_blank(s):
    return bool(s and not s.isspace())

# First Split: If there is any "-" sign
x = -121
strnum= str(x)        # Converting to string
sep = strnum.split("-")   # Seperate if "-" is present, keeping it in a list


# Second Split: Splitting the digits, storing into an array
y = [int(a) for a in sep[-1]]   # x[-1]=last/only item in the list, which should be a number


# recursive array
recarr=[]
j=-1
for i in range(len(y)):
    recarr.append(y[j])
    j=j-1
# print(recarr)
# print(x[0])


if y == recarr and is_not_blank(sep[0]):
    print("True")
else:
    print("False")