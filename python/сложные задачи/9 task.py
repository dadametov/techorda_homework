def hanoiTower(n, source=1, target=3, auxiliary=2):
    if n == 1:
        print(f"Диск 1 с башни {source} переложить в башню {target}")
    else:
        hanoiTower(n - 1, source, auxiliary, target)
        print(f"Диск {n} с башни {source} переложить в башню {target}")
        hanoiTower(n - 1, auxiliary, target, source)

# Пример использования:
n = 5  
hanoiTower(n)
