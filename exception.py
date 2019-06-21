try:
    n=int(input())
    n=n/0
    print(n)
except Exception:
    print("exception handled")
finally:
    print("run")