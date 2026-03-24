import math

names_list=["Егор", "Даниил", "Марина", "Наталья"]
age_list=[20, 15, 30, 99]
word="Отличная, хорошая строка!"
generate_list=[i**2 for i in range(50) if i>=1 and i<=10]

generate_dict={x:x**2 for x in range(20) if x>=1 and x<=10}
generate_dict_n_a={name:age for name,age in zip(names_list,age_list)}

generate_set={s for s in word if s!=","}

print("\nГенерация списка с квадратами с условием:")
print(f"{generate_list}\n")

print("Генерация словаря с условием:")
print(f"{generate_dict}\n")
print("Генерация словаря из двух списков:")
print(f"{generate_dict_n_a}\n")

print("Генерация множества с условием:")
print(f"{generate_set}\n")
