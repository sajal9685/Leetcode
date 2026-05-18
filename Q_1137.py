n=int(input("enter number="))

def tri(n):
    if n<=1:
        return n
    if n==2:
        return 1
    return tri(n-1)+tri(n-2)+tri(n-3)

print(tri(n))   