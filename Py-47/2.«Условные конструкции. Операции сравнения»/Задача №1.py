
if __name__ == '__main__':
    n = int(raw_input().strip())


    n = int(input())
if n % 2 == 1:
    print("Weird")
elif 2 <= n <= 5:
    print("Not Weird")
elif 6 <= n <= 20:
    print("Weird")
elif 20 < n <= 100:
    print("Not Weird")
else:
    print("Error")
    