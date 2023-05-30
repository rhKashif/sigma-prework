from datetime import datetime, date

current_day = datetime.now().day
current_month = datetime.now().month
current_year = datetime.now().year


input_date = input("Enter your date of birth (e.g 5-7-2002): ")
input_date_list = input_date.split("-")
output_date_list = [eval(i) for i in input_date_list]

diff_day = current_day - output_date_list[0]
diff_month = current_month - output_date_list[1]
diff_year = current_year - output_date_list[2]

if diff_day < 0:
    diff_month -= 1
if diff_month < 0:
    diff_year -=1

print(f"You are {diff_year} years old!")