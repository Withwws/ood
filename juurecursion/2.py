def ispalindrome(n,i,l):
    # print(n,i,l)
    if i==l:
        return True
    if n[l] != n[i]:
        return False
    if i<l:
        return ispalindrome(n,i+1,l-1)
    return True
    

n = input("Enter Input : ")
i=0
l=len(n)-1
if ispalindrome(n,i,l):
    print(f"\'{n}\' is palindrome")
else:
    print(f"\'{n}\' is not palindrome")