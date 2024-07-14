import re

def generator_numbers(text: str):
    numbers = re.findall(r"\b\d+\.\d+\b", text)
    return [float(number) for number in numbers]
              
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."          
result = generator_numbers(text)
total_income = sum(result)     
print(f"Загальний дохід: {total_income}")

   
    