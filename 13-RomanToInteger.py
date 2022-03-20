
# s2 = "LVIII"    #58
# s2 = "MCMXCIV"    #1994
# s2 = "III"
s2 = "MCMXCVI"  #1996
s2 = "MCDLXXVI" #1476


dict1 = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

dict2 = {
    "IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900
}

# print(len(s1))

value = []
i = 0
step = 1

while(i < len(s2)):
    # print(i)
    flag = 0

    if i < (len(s2)-1) and s2[i] != s2[i+1]:
        add_string = s2[i] + s2[i + 1]
        print(add_string)
        if add_string in dict2:
            get_value = dict2[add_string]
            print(f"got string {add_string}")
            print(f"value: {get_value} ")
            value.append(get_value)
            flag = 1
            step = 2
            print("flag")

    else:
        step = 1

    if flag !=1:
        get_value = dict1[s2[i]]
        print(f"got string_out {s2[i]}")
        print(f"out_string_value: {get_value} ")
        value.append(get_value)
        step = 1

    if i == (len(s2)-2) and flag != 1:
        step = 1
        print(f"Last step: {len(s2)-1}")

    print(f"Adding Step: {step}")
    i = i+step
    print(f"ith position: {i}")

print(sum(value))


# notes
'''
1. I could not change the step size inside the for loop. Only way was to use "while" loop and manually change position(i).
2. checked 2 chararcters and if it is not in the dictionary-2 then will go dict1 and step_size++
3. If it is found in dict-2, the step_size = 2
4. But what if, you are in the last 2 value and got something in dict-2, it will make 2 step, which will not check after!
   2 case can happen. either the last two is in dict-2 or not. if it is not in dict2, then step=1 otherwise step=2.

'''

