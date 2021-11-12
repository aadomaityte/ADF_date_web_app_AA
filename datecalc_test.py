#Importing calculator functions from the datecalc file
from datecalc import duration
from datecalc import when

#Importing package needed for functions to work
from datetime import datetime, timedelta


#Duration - calculates the difference between two dates in days

# 1 - Test that calculator is working out the date difference correctly
def test_duration():   
    start_date = datetime(2021,11,11)
    end_date = datetime(2021,12,25)
    diff_calculation = duration(start_date, end_date)
    assert diff_calculation == 44

# 2 - Test that the calculation sum is a whole number (integer)
def test_duration_type_int():   
    start_date = datetime(2021,11,1)
    end_date = datetime(2021,11,10)
    diff_calculation = duration(start_date, end_date)
    sum_type = type(diff_calculation)
    assert sum_type == int

# 3 - Test that the calculation sum type is a positive integer even if calculating dates backwards
def test_duration_type_positive_int():   
    start_date = datetime(2021,11,11)
    end_date = datetime(2021,11,1)
    diff_calculation = duration(start_date, end_date)
    is_positive_integer = diff_calculation > 0
    assert is_positive_integer == True

# 4 - Test that the calculation sum is positive integer even if calculating dates backwards
def test_duration_positive_int():   
    start_date = datetime(2021,11,11)
    end_date = datetime(2021,11,1)
    diff_calculation = duration(start_date, end_date)
    assert diff_calculation == 10

# 5 - Test that the calculation returns zero if same days are selected 
def test_duration_zero():   
    start_date = datetime(2021,11,11)
    end_date = datetime(2021,11,11)
    diff_calculation = duration(start_date, end_date)
    assert diff_calculation == 0


#When - calculates a new date, by adding an amount of days to a given date

# 1 - Test that the calculation is returning the correct date 
def test_when():
    start_date = datetime(2021,11,1)
    days_between = int(10)
    when_calculation = when(start_date, days_between)
    assert when_calculation == datetime(2021,11,11)  

# 2 - Test that the calculation returns a date that is in a datetime format
def test_when_type_int():
    start_date = datetime(2021,11,1)
    days_between = int(5)
    end_date_calculation = when(start_date, days_between)
    assert type(end_date_calculation) == datetime

# 3 - Test that the calculation returns same start date if days selected is zero
def test_when_zero():
    start_date = datetime(2021,11,1)
    days_between = int(0)
    end_date_calculation = when(start_date, days_between)
    assert end_date_calculation == start_date
