list_a = [3,2,4]
target_a = 6

def sum(list_a, target_a):
    for i in range(len(list_a)):
        for a in range(len(list_a)):
            if list_a[i] + list_a[a] == target_a and i != a:
                return [i,a]

print(sum(list_a, target_a))