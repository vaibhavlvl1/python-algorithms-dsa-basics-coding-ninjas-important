# tower of hanoi


def tower_of_hanoi(n,a,b,c):
    if n==1:
        print(f"move {n} th disk from {a} to {c}")
        return
    else:
        tower_of_hanoi(n-1,a,c,b)
        print(f"move {n} th disk from {a} to {c}")
        tower_of_hanoi(n-1,b,a,c)
        
    



tower_of_hanoi(2,"a","b","c")