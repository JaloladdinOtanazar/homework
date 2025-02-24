its_name = input("Tell me your name:")
its_year_of_birth = int(input("Tell me your year of birth: "))
from datetime import datetime
current_year = datetime.now().year
its_age = current_year - its_year_of_birth
print("your age is :", its_age)
