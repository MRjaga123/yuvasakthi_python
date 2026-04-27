# In Python, dates are not a data type of their own, but we can use the datetime module to work with dates as date objects.

# Display the current date and time
import datetime
x=datetime.datetime.now()
print(x) # Year,Month,Day,Hour,Minute,Second,Microsecond

# Accessing Parts of the Date
import datetime
x = datetime.datetime.now()
print(x.year)          # Year
print(x.strftime("%A"))  # Weekday name

# Creating Date Objects
import datetime
x = datetime.datetime(2020, 5, 17)
print(x)

# Formatting Dates with strftime()
import datetime
x = datetime.datetime(2018, 6, 1)
print(x.strftime("%B"))   # Full month name

