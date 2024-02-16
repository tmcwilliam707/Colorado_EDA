import pandas as pd
from geopy.distance import geodesic
import numpy as np
from scipy.spatial import cKDTree


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






# Convert the latitudes and longitudes to numpy arrays
coords_df1 = np.array(list(zip(df1['latitude'].astype(float), df1['longitude'].astype(float))))
coords_df2 = np.array(list(zip(df2['latitude'].astype(float), df2['longitude'].astype(float))))
coords_df3 = np.array(list(zip(df3['latitude'].astype(float), df3['longitude'].astype(float))))

#Create a KDTree for df3
tree = cKDTree(coords_df3)

#Find the closest point in df3 for each point in df1 and df2'
df1['closest_df3_index'], df1['distance_to_closest_df3'] = tree.query(coords_df1, k=1)
df2['closest_df3_index'], df2['distance_to_closest_df3'] = tree.query(coords_df2, k=1)

#Convert the distances to kilometers'
df1['distance_to_closest_df3'] = df1['distance_to_closest_df3'].apply(lambda x: geodesic(x).kilometers)
df2['distance_to_closest_df3'] = df2['distance_to_closest_df3'].apply(lambda x: geodesic(x).kilometers)

# Calculate the total distance for each dataframe
df1['total_distance'] = df1['distance_to_closest_df3'].sum()
df2['total_distance'] = df2['distance_to_closest_df3'].sum()


# Concatenate the dataframes
df = pd.concat([df1, df2, df3], ignore_index=True)

# Drop the columns with all null values
df = df.dropna(how='all', axis=1)

# Write df to a CSV file
#df.to_csv('location_kerneys_merged.csv', index=False)


print(df)