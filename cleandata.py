import pandas as pd
import random as rnd

"""
    replace 'Employment_Status' with the name of the column that holds the type of employment 
        The column that holds the data such as FullTime, PartTime, Casual
    
    Replace 'Employee_ID' with the column that holds a unique key for the employee
        such as a employee id number
    
    status list hold 'FullTime', 'PartTime', 'Casual'
        This is the order in which the records are prioritized
        for example if there are three records for an employee, each having one of these statuses,
        the first in this list ( FullTime ) will be kept and the others dropped
    
"""


def status_sort(row):
    return status.index(row['Employment_Status'].replace("'", ""))


status = ['FullTime', 'PartTime', 'Casual']

# import_data_pd = pd.DataFrame()

import_data_pd = pd.read_csv('sample_randomized_data.csv')
import_data_pd['status_sort_col'] = import_data_pd.apply(lambda row: status_sort(row), axis=1)
import_data_pd = import_data_pd.sort_values(["Employee_ID", "status_sort_col"], ascending=(True, True))
import_data_pd = import_data_pd.drop_duplicates(subset=['Employee_ID'], keep='first')

import_data_pd.to_csv('cleaned_data.csv', index=False)
