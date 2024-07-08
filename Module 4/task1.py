file = open("salary_file.txt", "r")
salaries = []
with open("salary_file.txt", "r") as file:
    for text in file.readlines():
     salaries.append(int(text.split(",")[1]))

total_sum = sum(salaries)
average = total_sum / len(salaries)
print(f"Загальна сума заробітної плати: {total_sum}, Середня заробітна плата: {average}")

