print("HELLO WORLD")
print('HELLO WORLD')
print(
  '''HELLO 
      WORLD''')
print(
  """HELLO 
  WORLD""")

hi ="""
HELLO
WORLD
"""

print(hi)

head = 'HEAD'
tail = 'TAIL'

print(head + tail)
print(head * 2)

print(len(head + tail))

print(head[0])

dragon = head + 'body' + tail
print(dragon[-4:])

print(dragon.count('T'))
print(dragon.find('D'))
# print(dragon.index('Z')) 

print("-".join(dragon))

print(dragon.upper())
print(dragon.lower())

print("{0:>20}".format(dragon))
print("{0:>20}".format(dragon).lstrip())

print(dragon.replace('body', '============='))
print(dragon)

dragon_slash = '-'.join(dragon)
print(dragon_slash)

dragon_part = dragon_slash.split('-')
print(dragon_part)
