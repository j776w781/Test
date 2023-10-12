eggs = int(input('How many eggs: '))

cases = eggs // 24

cartons = (eggs - cases*24) // 6

singles = (eggs - cases*24 - cartons*6)

print('Cases: ', cases)

print('Cartons: ', cartons)

print('Singles: ', singles)
