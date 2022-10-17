# Программа сделана на языке Python, так как для меня он проще. В случае необходимости могу переписать и на C#

arrays = ["rtgretgergs", "fwe", "385", "nvebrbfoiehroi", "woijefoihnreo", "b"]

result = []

for i in arrays:
    if len(i) <= 3:
        result.append(i)

print(result)