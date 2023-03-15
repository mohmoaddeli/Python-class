

ls = []
print()
print("write down as many as number you want to sum.")
print("put the '=' character to stop taking number and give you the summation")
while True:
    num = (input("number : "))
    if num == "=":
        break
    ls.append(float(num))
summ = sum(ls)
print("summation is : ", summ)
