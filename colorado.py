import pandas as pd
import numpy as np


pd.set_option('display.max_rows', 100) 


df3 = pd.read_csv('/Users/taylormcwilliam/Downloads/address/us_CO_corelogic_parcelpoints_666850826424156160_sep2023.csv')
df2 = pd.read_csv('/Users/taylormcwilliam/Downloads/address/us_gadberry_addresssample_co_666852927297552384.csv')
df1 = pd.read_csv('/Users/taylormcwilliam/Downloads/address/us_CO_willowbend_address_689371548473098240_nov2023.csv')


df1.columns = df1.columns.str.lower()
df2.columns = df2.columns.str.lower()
df3.columns = df3.columns.str.lower()


df1['std_addr'] = df1['pridelvno'].astype(str) + " " +  df1['predrctnl'].astype(str) + " " + df1['streetname'].astype(str) + " " + df1['suffix'].astype(str)
df2['std_addr'] = df2['street_number'].astype(str) + " "  + df2['parsed_predir'].astype(str) + " " + df2['street'].astype(str) + " " + df2['unit_num'].astype(str)

df2 = df2.rename(columns={
    'zip': 'zipcode',
    'city': 'city',
    'state': 'state',
    'geo_lon': 'lon',
    'geo_lat': 'lat',
    'std_addr': 'std_addr'
    
})

df3 = df3.rename(columns={
    'zip': 'zipcode',
    'city': 'city',
    'state': 'state',
    'longitude': 'lon',
    'latitude': 'lat',
    'std_addr': 'std_addr'
})

# Merge df1 and df2
merged_df1_df2 = df1.merge(df2, on='std_addr', how='outer', indicator=True)
merged_df1_df2.rename(columns={'_merge': 'df1_df2'}, inplace=True)

# Merge df1_df2 and df3
merged_all = merged_df1_df2.merge(df3, on='std_addr', how='outer', indicator=True)
merged_all.rename(columns={'_merge': 'df1_df2_df3'}, inplace=True)

# Print the head of the merged dataframe
print(merged_all.head())

''' both: all dataframes, left_only: df1, right_only: df2'''

'''merged_df1_df2 = df1.merge(df2, on=['zipcode', 'city', 'std_addr', 'lon', 'lat'], how='outer', indicator='Exist')
merged_df1_df2['Exist'] = merged_df1_df2['Exist'].map({'both': 'df1_df2', 'left_only': 'df1', 'right_only': 'df2'})


merged_all = merged_df1_df2.merge(df3, on=['zipcode', 'city', 'std_addr', 'lon', 'lat'], how='outer', indicator='Exist2')
merged_all['Exist2'] = np.where(merged_all['Exist2'] == 'both', 'df1_df2_df3', merged_all['Exist'])

diff_df = merged_all[merged_all['Exist2'] != 'df1_df2_df3']

# List of changed or merged columns
changed_columns = ['std_addr', 'zipcode', 'city', 'state', 'lon', 'lat']


print(df2[changed_columns].head())


diff_df.to_csv('diff_df.csv', index=False)


print(df1.columns)
print(df2.columns)
print(df3.columns)

'''
