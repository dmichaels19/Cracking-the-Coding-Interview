# 1. Get (a, b) counts
# 2. Make generator that finds solution
# 3. Iterate over generator
# 4. From pattern, string, and a, b lengths
def get_counts(pattern):
  a_count, b_count = 0, 0
  for c in pattern:
    if c=='a':
      a_count += 1
    else:
      b_count += 1
  return (a_count, b_count)
  
def solve_equation(a_count, b_count, str_length):  
  # a_count*a_length + b_count*b_length = str_Length
  for a_length in range(1, str_length):
    b_length = (str_length - a_count*a_length) / b_count
    if b_length.is_integer():
        if a_count*a_length + b_count*b_length == str_length:
            if b_length > 0:
                yield (int(a_length), int(b_length))
  
    
def check_string(a_len, b_len, string, pattern):
  a = None
  b = None
  string_i = 0
  for i in range(len(pattern)):
    if pattern[i] == 'a':
      if a is None:
        a = string[string_i:string_i+a_len]
      else:
        if string[string_i:string_i+a_len] != a:
          return False
      string_i += a_len
    else:
      if b is None:
        b = string[string_i:string_i+b_len]
        print(b)
      else:
        if string[string_i:string_i+b_len] != b:
          return False
      string_i += b_len
  return (a, b)

def pattern_matching(pattern, value):
  a_count, b_count = get_counts(pattern)
  for a_length, b_length in solve_equation(a_count, b_count, len(value)):
    vals = check_string(a_length, b_length, value, pattern)
    if vals:
        return vals
        break
  else:
    return False
  
print(pattern_matching("aabab", "catcatgocatgo"))
