import pandas as pd
import random as rnd
import datetime
from list_of_names import list_of_boys_firstnames, list_of_girls_firstnames, list_of_lastnames
from list_of_jobs import list_of_titles

employee = []
status = ['FullTime', 'PartTime', 'Casual']
First_Names = list_of_boys_firstnames + list_of_girls_firstnames


for x in range(10000, 20000):
    entry_count = rnd.randrange(1, 4)
    employee_status = rnd.randrange(0, 3)

    Hire_Date = str(rnd.randrange(1, 13)) + '-' + str(rnd.randrange(1, 30)) + '-' + str(rnd.randrange(1990, 2023))

    start_date = datetime.date(1980, 1, 1)
    end_date = datetime.date(2022, 4, 30)

    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = rnd.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)

    for entry in range(0, entry_count):
        First_Name = "'" + str(rnd.choice(First_Names)) + "'"
        Last_Name = "'" + str(rnd.choice(list_of_lastnames)) + "'"

        employee.append([x, First_Name, Last_Name,
                         "'" + str(random_date) + "'", "'" + status[employee_status] + "'",
                         "'" + rnd.choice(list_of_titles) + "'"])

        employee_status = employee_status + 1
        if employee_status > 2:
            employee_status = 0

sample_data_pd = pd.DataFrame(employee, columns=['Employee_ID', 'First_Name', 'Last_Name', 'Hire_Date',
                                                 'Employment_Status', 'Job_Title'])

sample_data_pd.to_csv('sample_data.csv', index=False)

# Show the sample data created
# pd.set_option('display.max_rows', None)
# print(result)

sample_data_pd = sample_data_pd.sample(frac=1).reset_index(drop=True)
sample_data_pd.to_csv('sample_randomized_data.csv', index=False)

