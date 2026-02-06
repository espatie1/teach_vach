import math

def decimal_to_binary(n):
  if n == 0:
    return "0"
  return bin(n)[2:]

def binary_to_decimal(bin_str):
  return int(bin_str, 2)

def apply_transformation_rules(n, binary_n):
  if n % 2 != 0:
    prefix = "10"
    suffix_replacement = "0"
    modified_binary = prefix + binary_n[:-1] + suffix_replacement
  else:
    prefix = "11"
    suffix_replacement = "1"
    modified_binary = prefix + binary_n[:-1] + suffix_replacement
  return modified_binary

def calculate_r(n):
  binary_n_str = decimal_to_binary(n)
  modified_binary_r_str = apply_transformation_rules(n, binary_n_str)
  r = binary_to_decimal(modified_binary_r_str)
  return r

start_n = 20
min_r_found = float('inf')
n_check_limit = 100

print(f"Ищем минимальное R для N >= {start_n}")
print("-" * 30)

found_minimum = False
for current_n in range(start_n, n_check_limit):
  current_r = calculate_r(current_n)
  if current_r is not None:
    if current_r < min_r_found:
      min_r_found = current_r
      found_minimum = True

print("-" * 30)

if found_minimum:
  print(f"Минимальное число R, которое может быть результатом работы алгоритма,")
  print(f"при условии, что N не меньше {start_n}, равно: {min_r_found}")
