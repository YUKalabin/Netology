n=int(input("1 <= n <= 100"))
if n % 2 == 1:
    print("Weird")
elif 2 <= n <= 5:
    print("Not Weird")
elif 6 <= n <= 20:
    print("Weird")
elif n > 20:
    print("Not Weird")