def prime(n):
    k=5
    k2=2

    if n==2 or n==3:
        return True
    elif n%2==0 or n%3==0:
        return False
    else:
        while (k<=n):
            if k==n:
                return True
            elif n%k==0:
                return False
            else:
                k+=k2
                k2=6-k2        
                

n=input("請輸入正整數：")

is_prime=False
max_prime=0
for i in range(0,len(n)):
    for j in range(i,len(n)):
         if (prime(int(n[i:j+1]))):
             if (int(n[i:j+1])>max_prime):
                max_prime= int(n[i:j+1])
             is_prime=True

if (is_prime):
    print("子字串中最大的質數為：%d" %(max_prime))
else:
    print("子字串中最大的質數為：No prime found")



