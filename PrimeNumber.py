number=4

if number>1:
    for i in range(2,number//2):
        if number%i==0:
            print("Not Prime")
            break
    else:
        print("Prime")