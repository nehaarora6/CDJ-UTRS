import pandas as pd
import matplotlib.pyplot as plt
#import contextily as ctx (to get background)


# Read CSV files into DataFrames
df_2018 = pd.read_csv('2018.csv')
df_2019 = pd.read_csv('2019.csv')
df_2020 = pd.read_csv('2020.csv')
df_2021 = pd.read_csv('2021.csv')
df_2022 = pd.read_csv('2022.csv')

# Concatenate all DataFrames into one
df = pd.concat([df_2018, df_2019, df_2020, df_2021, df_2022])

# Define the bounding box coordinates of Cape Cod Bay and filter data
bbox = (-70.5, 41.5, -69.5, 42.5)
filtered_data = df[(df['LAT'] >= bbox[1]) & (df['LAT'] <= bbox[3]) &
                   (df['LON'] >= bbox[0]) & (df['LON'] <= bbox[2])]

# Plot data
plt.figure(figsize=(10, 8))
plt.scatter(filtered_data['LON'], filtered_data['LAT'], c=filtered_data['SOG'], cmap='viridis', alpha=0.5)

# Label data points with vessel names
name_display_interval = 5
labelled_names = set()
for i, row in filtered_data.iterrows():
    if i % name_display_interval == 0 or row['VesselName'] not in labelled_names:
        plt.text(row['LON'], row['LAT'], row['VesselName'], fontsize=8, ha='right', va='bottom')
        labelled_names.add(row['VesselName'])

# Add titles
plt.title('Vessels in Cape Cod Bay (2018-2022)')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.colorbar(label='Speed over Ground (SOG)')

# Show plot (all 5 years together)
plt.grid(True)
plt.show()

# - - - - - - - - - - - - - - - -  

# Create plots for each year
for year, df_year in zip(range(2018, 2023), [df_2018, df_2019, df_2020, df_2021, df_2022]):
    filtered_data = df_year[(df_year['LAT'] >= bbox[1]) & (df_year['LAT'] <= bbox[3]) &
                            (df_year['LON'] >= bbox[0]) & (df_year['LON'] <= bbox[2])]
    
    # Plot the data
    plt.figure(figsize=(10, 8))
    plt.scatter(filtered_data['LON'], filtered_data['LAT'], c=filtered_data['SOG'], cmap='viridis', alpha=0.5)

    # Label data points with vessel names at regular intervals or unique names
    labelled_names = set()
    for i, row in filtered_data.iterrows():
        if i % name_display_interval == 0 or row['VesselName'] not in labelled_names:
            plt.text(row['LON'], row['LAT'], row['VesselName'], fontsize=8, ha='right', va='bottom')
            labelled_names.add(row['VesselName'])

    # Add titles
    plt.title(f'Vessels in Cape Cod Bay - {year}')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.colorbar(label='Speed over Ground (SOG)')

    # Show plot
    plt.grid(True)
    plt.show()