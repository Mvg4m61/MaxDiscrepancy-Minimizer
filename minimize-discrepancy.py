def minimize():
    l1 = []
    n = int(input("\nEnter number of packets: "))
    for i in range(n):
        num = int(input("Enter number of sweets respectively (Must be a positive integer): "))
        l1.append(num)
    m = int(input("\nEnter number of children: "))
    ex = n-m
    l1.sort(reverse=True)
    l2 = l1[m:]
    l1 = l1[:m]
    print(l1)
    print(l2)
    for e in l2:
        l1[-1]+=e
        l2.remove(e)
        l1.sort(reverse=True)
    diff = l1[0]-l1[-1]
    print("\nMinimum difference between richest and poorest kid: ",diff)
        
minimize()