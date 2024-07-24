def fix_start(s):
  char = s[0]
  length = len(s)
  s = s.replace(char, '*')
  s = char + s[1:]

  return s