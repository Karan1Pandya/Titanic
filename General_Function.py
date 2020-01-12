import pandas as pd
import numpy as np


def iqr_outliers(num_array):
    """
    Finds outliers based on IQR method
    Params:
    -------
    num_arrar: numpy array or list
    Returns:
    --------
    List of outliers if present
    """
    # Find 25th percentile / q1
    q1 = np.nanpercentile(num_array, 25)
    # Find 25th percentile / q1
    q3 = np.nanpercentile(num_array, 75)
    # Find IQR
    iqr = q3 - q1
    # Define upper and lower limits for outlier detection
    upper_limit = q3 + (1.5 * iqr)
    lower_limit = q1 - (1.5 * iqr)
    return [num for num in num_array if num > upper_limit or num < lower_limit]




def basic_explo(df):
#     df.shape
    print('rows:{},column:{}'.format((str(df.shape[0])),str(df.shape[1])))
    print(df.info())
    print("Descriptive stats for numeric columns")
    print(df.describe)
    print("Descreptive stats for catogrial columns")
    print(df.describe(include='object'))
    null_df=pd.DataFrame(df.isnull().sum())
    null_df.columns=['count']
    print(null_df[null_df['count']>0])
    df_num=df.select_dtypes(exclude='object')
    print(df_num)
    df_num_cols=df_num.columns
    for c in df_num_cols:
        print(c)
        print(iqr_outliers(df_num[c]))

if __name__ == "__main__":
    df=pd.read_csv('mall_data.txt')
    print(basic_explo(df))