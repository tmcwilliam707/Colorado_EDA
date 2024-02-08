import pandas as pd
import numpy as np


pd.set_option('display.max_columns', None)

# Load the CSV files
df3 = pd.read_csv('/Users/taylormcwilliam/Downloads/address/us_CO_corelogic_parcelpoints_666850826424156160_sep2023.csv')
df2 = pd.read_csv('/Users/taylormcwilliam/Downloads/address/us_gadberry_addresssample_co_666852927297552384.csv')
df1 = pd.read_csv('/Users/taylormcwilliam/Downloads/address/us_CO_willowbend_address_689371548473098240_nov2023.csv')

df1.columns = df1.columns.str.lower()
df2.columns = df2.columns.str.lower()
df3.columns = df3.columns.str.lower()

df2 = df2.rename(columns={
    'zip': 'zipcode',
    'city': 'city',
    'state': 'state',
    'geo_lon': 'lon',
    'geo_lat': 'lat'
})

df3 = df3.rename(columns={
    'zip': 'zipcode',
    'city': 'city',
    'state': 'state',
    'longitude': 'lon',
    'latitude': 'lat'
})

merged_df1_df2 = df1.merge(df2, on=['zipcode', 'city', 'state', 'lon', 'lat'], how='outer', indicator='Exist')
merged_df1_df2['Exist'] = merged_df1_df2['Exist'].map({'both': 'df1_df2', 'left_only': 'df1', 'right_only': 'df2'})


merged_all = merged_df1_df2.merge(df3, on=['zipcode', 'city', 'state', 'lon', 'lat'], how='outer', indicator='Exist2')
merged_all['Exist2'] = np.where(merged_all['Exist2'] == 'both', 'df1_df2_df3', merged_all['Exist'])


diff_df = merged_all[merged_all['Exist2'] != 'df1_df2_df3']
print(diff_df.to_string(index=False))
'''


print(df1.columns)
print(df2.columns)
print(df3.columns)
'''
