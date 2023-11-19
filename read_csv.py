import pandas as pd
import time
from pyarrow import csv
import datatable as dt
import dask.dataframe as dd
import timeit
# Decorator function to measure execution time
def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = timeit.default_timer()
        result = func(*args, **kwargs)
        end_time = timeit.default_timer()
        execution_time = end_time - start_time
        print(f"Execution time of '{func.__name__}': {execution_time} seconds")
        return result
    return wrapper

#PyArrow
@measure_time
def read_csv_pyarrow(file):
    try:
        arrow_table = csv.read_csv(file)
        df = arrow_table.to_pandas()
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
    return df

@measure_time
def read_csv_datable(file):
    try:
        datatable_frame = dt.fread(file)
    except Exception as e:
        print(f"An error occurred: {e}")

@measure_time
def read_csv_dask(file):
    try:
        dask_dataframe = dd.read_csv(file)
        df = dask_dataframe.compute() 
    except Exception as e:
        print(f"An error occurred: {e}")
    return df

@measure_time
def read_csv_c(file):
    df = pd.read_csv(file,engine="c")
    return df

@measure_time
def read_csv(file):
    df = pd.read_csv(file)
    return df

file_to_read = 'creditcard_2023.csv'

df = read_csv(file_to_read)
df_c = read_csv_c(file_to_read)
arrow_df = read_csv_pyarrow(file_to_read)
dask_df = read_csv_dask(file_to_read)