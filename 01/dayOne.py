input_file = open("input1.txt", "r")
calorie_entries = input_file.read().split('\n')
input_file.close()

current_elf = 0
elf_totals = []

for element in calorie_entries:
    if element == '':
        elf_totals.append(current_elf)
        current_elf = 0
    else:
        current_elf += int(element)

elf_totals.append(current_elf)

elf_totals.sort()

# print(calorie_entries)
print(sum(elf_totals[-3:]))
