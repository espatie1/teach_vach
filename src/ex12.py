def run_editor(s):
    while '>1' in s or '>2' in s or '>3' in s:
        if '>1' in s:
            s = s.replace('>1', '33>', 1)
        if '>2' in s:
            s = s.replace('>2', '2>', 1)
        if '>3' in s:
            s = s.replace('>3', '1>', 1)
    return s

n = 0
while True:
    input_str = '>' + '1' * 37 + '2' * n + '3' * 37
    
    result_str = run_editor(input_str)
    
    current_sum = 0
    for char in result_str:
        if char.isdigit():
            current_sum += int(char)
            
    if current_sum % 17 == 0:
        print(n)
        break
        
    n += 1