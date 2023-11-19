def hanoi(n, source, target, auxiliary):
    if n > 0:
        
        hanoi(n-1, source, auxiliary, target)
        
        print(f"Move disk {n} from {source} to {target}")
        
        hanoi(n-1, auxiliary, target, source)

hanoi (4, 'A', 'B', 'C')