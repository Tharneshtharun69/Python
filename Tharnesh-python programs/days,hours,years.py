birth_date=eval(input("Enter the birth date without zero:"))
birth_month=eval(input("Enter the birth month without zero:"))
birth_yy=eval(input("Enter the birth year:"))
current_yy=eval(input("Enter the current year:"))
months_per_year=12
days_per_month=30
hours_per_day=24
days_per_year=365
no_of_years=current_yy-birth_yy
no_of_days=days_per_year*no_of_years
no_of_months=(no_of_years)*12
no_of_hours=no_of_days*hours_per_day
print(no_of_years,"years",no_of_days,"days",no_of_months,"months",no_of_hours,"hours")

