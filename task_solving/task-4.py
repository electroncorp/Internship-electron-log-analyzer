def diff_from_average(data):
    d = []
    if len(data) == 0 :

        
        return d
    avg = sum(data) / len(data)

    for i in data:
        diff = i - avg
        diff = round(diff,2)
        d.append(diff)
    return d
print(diff_from_average([55,95,62,36,48]))
print(diff_from_average([10,10,10]))
print(diff_from_average([1.5,2.25]))
print(diff_from_average([]))
print(diff_from_average([100]))
