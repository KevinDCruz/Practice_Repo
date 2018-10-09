#Print first non repeated character from String?


char_order = []
ctr = {}

def first_non_repeating(str):
  for c in str:
    if c in ctr:
      ctr[c] += 1
      print(ctr)

    else:
      ctr[c] = 1
      char_order.append(c)
      print(char_order)

  for c in char_order:
    if ctr[c] == 1:
      return c
  return None

#print(first_non_repeating('abcdef'))
print(first_non_repeating('abcabcdef'))
#print(first_non_repeating('aabbcc'))
