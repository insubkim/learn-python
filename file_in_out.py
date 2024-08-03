print('\n* READ *\n')

f = open('class.py', 'r')

print('=' * 50)
print(f.read())
print('=' * 50)

f.close()

print('\n* READLINE *\n')

f = open('class.py', 'r')

print('=' * 50)
print(f.readline())
print('=' * 50)

f.close()

print('\n* READLINES *\n')

f = open('class.py', 'r')

print('=' * 50)
l = f.readlines()

for line in l:
  print(line.rstrip())


print('=' * 50)

f.close()

print('\n* READ *\n')

f = open('class.py', 'r')

print('=' * 50)
l = f.read()

print(l)

print('=' * 50)

f.close()

print('\n* with open *\n')

print('=' * 50)

with open('class.py', 'r') as f:
  print(f.readline())
  
print('=' * 50)
