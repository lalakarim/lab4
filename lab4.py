numbers = [10, 7, 3, 20, 12, 15, 8, 13, 25, 9]
with open("ededi_massiv.txt", "w") as file:
    for number in numbers:
        file.write(str(number) + "\n")
not_divisible_by_5 = []
with open("ededi_massiv.txt", "r") as file:
    for line in file:
        num = int(line.strip())
        if num % 5 != 0:
            not_divisible_by_5.append(num)

with open("bolunmeyenler.txt", "w") as new_file:
    for num in not_divisible_by_5:
        new_file.write(str(num) + "\n")

total_sum = sum(not_divisible_by_5)
print("5-ə bölünməyən ədədlərin cəmi:", total_sum)
