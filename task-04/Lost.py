def say_hello(s):
    hello = "hello"
    i = 0
    for letter in s:
        if i < len(hello) and letter == hello[i]:
            i += 1
    return i == len(hello)



a = input()
if say_hello(a):
    print("YES")
else:
    print("NO")
