import pandas as pd
from fuzzywuzzy import fuzz


pd.set_option('display.max_rows', 100) 


df3 = pd.read_csv('/Users/taylormcwilliam/Downloads/address/us_CO_corelogic_parcelpoints_666850826424156160_sep2023.csv', dtype=str)
df2 = pd.read_csv('/Users/taylormcwilliam/Downloads/address/us_gadberry_addresssample_co_666852927297552384.csv', dtype=str)
df1 = pd.read_csv('/Users/taylormcwilliam/Downloads/address/us_CO_willowbend_address_689371548473098240_nov2023.csv', dtype=str)


df1.columns = df1.columns.str.lower()
df2.columns = df2.columns.str.lower()
df3.columns = df3.columns.str.lower()

df1 = df1.rename(columns={'lat': 'latitude', 'lon': 'longitude'})
df2 = df2.rename(columns={'geo_lat': 'latitude', 'geo_lon': 'longitude'})

df3['complete_addr'] = df3['std_addr'].astype(str) + " " + df3['longitude'].astype(str) + " " + df3['latitude'].astype(str) 

df1['complete_addr'] = df1['pridelvno'].astype(str) + " " +  df1['predrctnl'].astype(str) + " " + df1['streetname'].astype(str) + " " + df1['suffix'].astype(str) + " " + df1['postdrctnl'].astype(str) + " " + df1['secdesc'].astype(str) + " " + df1['secno'].astype(str)  + " " + df1['longitude'].astype(str) + " " + df1['latitude'].astype(str) + " " + df1['dpv_confirm'].astype(str) + " " + df1['dpv_footnotes'].astype(str) 
df2['complete_addr'] = df2['street_number'].astype(str) + " " + df2['street'].astype(str) + " " + df2['unit_des'].astype(str) + " " + df2['unit_num'].astype(str) + " " + df2['longitude'].astype(str) + " " + df2['latitude'].astype(str) + " " + df2['addr_confidence'].astype(str) + " " + df2['geo_precision'].astype(str) 




'''


min_length = min(len(df1), len(df2), len(df3))

results_list = [{'df1_addr': df1['complete_addr'].iloc[i], 
                 'df2_addr': df2['complete_addr'].iloc[i], 
                 'df3_addr': df3['complete_addr'].iloc[i], 
                 'df1_df3_score': fuzz.ratio(df1['complete_addr'].iloc[i], df3['complete_addr'].iloc[i]), 
                 'df2_df3_score': fuzz.ratio(df2['complete_addr'].iloc[i], df3['complete_addr'].iloc[i])} 
                for i in range(min_length)]

results = pd.DataFrame(results_list)

print(results)


results.to_csv('/Users/taylormcwilliam/Documents/GitHub/eda_apple/levenshtein_results.csv', index=False)

'''

from fuzzywuzzy import fuzz


df1['lat_long'] = df1['latitude'].astype(str) + ',' + df1['longitude'].astype(str)
df2['lat_long'] = df2['latitude'].astype(str) + ',' + df2['longitude'].astype(str)
df3['lat_long'] = df3['latitude'].astype(str) + ',' + df3['longitude'].astype(str)


results_list = [{'df1_lat_long': df1['lat_long'].iloc[i], 
                 'df2_lat_long': df2['lat_long'].iloc[i], 
                 'df3_lat_long': df3['lat_long'].iloc[i], 
                 'df1_df3_score': fuzz.ratio(df1['lat_long'].iloc[i], df3['lat_long'].iloc[i]), 
                 'df2_df3_score': fuzz.ratio(df2['lat_long'].iloc[i], df3['lat_long'].iloc[i])} 
                for i in range(min(len(df1), len(df2), len(df3)))]




results = pd.DataFrame(results_list)


results.to_csv('/Users/taylormcwilliam/Documents/GitHub/eda_apple/levenshtein_loc_results.csv', index=False)