motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)
motorcycles.append('kawasaki')
print(motorcycles)
motorcycles.insert(1, 'ninja')
print(motorcycles)
del motorcycles[1]
print(motorcycles)

popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)
