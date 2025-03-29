import sqlite3
import pandas as pd

# Merging and Joining
# Inner Join on Chinook Database
con = sqlite3.connect('chinook.db')
df_chinook_customer = pd.read_sql_query("SELECT * FROM customers", con=con)
df_chinook_invoice = pd.read_sql_query("SELECT * FROM invoices", con=con)
merged_df = pd.merge(df_chinook_customer, df_chinook_invoice, on='CustomerId', how='inner')
invoice_count = df_chinook_invoice.groupby('CustomerId').size().reset_index(name="Total_invoices")
print(invoice_count)
print('-'*167)
# Outer Join on Movie Data
movies_data = pd.read_csv('movie.csv')
df1 = movies_data[['director_name', 'color']]
df2 = movies_data[['director_name', 'num_critic_for_reviews']]
left_join = pd.merge(df1, df2, on='director_name', how='left')
outer_join = pd.merge(df1, df2, on='director_name', how='outer')
len_left = len(left_join)
len_outer = len(outer_join)
print(f'left join:\n{left_join}\n outer join:\n{outer_join}')
print(f'\nnumber of rows in left join:{len_left}\nnumber of rows in outer join:{len_outer}')
print('-'*167)
# Grouping and Aggregating
# Grouped Aggregations on Titanic
titanic_data = pd.read_excel('titanic.xlsx')
grouped = titanic_data.groupby('Pclass').agg(
    average_age = ('Age', 'mean'),
    total_fare = ('Fare', 'sum'),
    passenger_count = ('PassengerId', 'count')
)
grouped.to_csv('grouped_titanic.csv')
print(grouped)
print('-'*167)
# Multi-level Grouping on Movie Data
group_by_color = movies_data.groupby('color').agg(
    num_critic_for_reviews = ('num_critic_for_reviews', 'sum' )
)
group_by_director = movies_data.groupby('director_name').agg(
    average_duration = ('duration', 'mean')
)
print(f'table for color:\n{group_by_color}\n')
print(f'table for duration:\n{group_by_director}\n')
print('-'*167)
# Nested Grouping on Flights
flights_data = pd.read_parquet('flights.htm')
group_flights = flights_data.groupby('Year', 'Month').agg(
    total_flight = ('sum'),
    average_delay = ('ArrDelay', 'mean'),
    maximum_departure = ('DepDelay', "max")
)
print(group_flights)
print('-'*167)
# Applying Functions
data = {
    'PassengerId': [1, 2, 3, 4],
    'Name': ['John Doe', 'Jane Doe', 'Tom Smith', 'Emily Stone'],
    'Age': [25, 16, 8, 40]
}
df = pd.DataFrame(data)
def classification(age):
    if age < 18:
        return "child"
    else:
        return "adult"
df['Age_Group'] = df['Age'].apply(classification)
print(df)
print('-'*167)
# Normalize Employee Salaries
employee_data = pd.read_csv('employee.csv')

def normalize(department):
    min_salary = department["BASE_SALARY"].min()
    max_salary = department["BASE_SALARY"].max()
    department['NORMALIZED_SALARY'] = (department['BASE_SALARY'] - min_salary) / (max_salary - min_salary)
    return department
df_normalized = employee_data.groupby('DEPARTMENT').apply(normalize)
print(df_normalized[['DEPARTMENT', 'BASE_SALARY', 'NORMALIZED_SALARY']])
print('-'*167)
# Custom Function on Movies
def size(duration):
    if duration < 60:
        return 'Short'
    elif 60 < duration < 120:
        return "Medium"
    else:
        return "Large"
movies_data['duration_category'] = movies_data['duration'].apply(size)
print(movies_data[['movie_title', 'duration', 'duration_category']])
print('-'*167)
# Using pipe
# Pipeline on Titanic
def pass_survived(df):
    return df.loc[df['Survived'] == 1].copy()
def fill_age(df):
    age_mean = df['Age'].mean()
    df['Age'] = df['Age'].fillna(age_mean)
    return df
def fare_per_age(df):
    df.loc[:,'Fare_Per_Age'] = df['Fare']/ df['Age']
    return df
pipeline = (titanic_data
            .pipe(pass_survived)
            .pipe(fill_age)
            .pipe(fare_per_age)
            )
print(pipeline[['PassengerId', 'Survived', 'Age', 'Fare', 'Fare_Per_Age']])
print("-"*167)
# Pipeline on Flights
def filter_delayed_flights(df):
    return df.loc[df['DepDelay'] > 30]
def add_delay(df):
    df['AirTime'].replace(0, pd.NA, inplace=True)
    df['Delay_Per_Hour '] = df['DepDelay'] / (df['Airtime']/60)
    return df
flights_delay_data = (flights_data
                      .pipe(filter_delayed_flights)
                      .pipe(add_delay)
                      )
print(pipeline[['DepDelay', 'AirTime', 'Delay_Per_Hour']])





