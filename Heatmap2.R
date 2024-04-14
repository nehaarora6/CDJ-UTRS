remotes::install_github("MikkoVihtakari/ggOceanMaps")
library(ggOceanMaps)

# quick map using coral_df dataframe
qmap(coral_df, color = I("red"))

# base map using the coral df dataframe (shows depth)
basemap(data = coral_df, bathymetry = TRUE)

# base map testing for entire world
dt <- data.frame(lon = c(-180, -180, 180, 180), lat = c(-90, 90, 90, -90))

basemap(data = dt, bathymetry = TRUE)

# base map testing with severity (only shows 2 points)
my_map <- basemap(data = coral_df, bathymetry = TRUE)
my_map + geom_point(aes(x = lon, y = lat, color = factor(value)), size = 3)

# custom limits
custom_limits <- c(min_lon, max_lon, min_lat, max_lat)

# Call basemap function with custom limits
my_map <- basemap(limits = custom_limits, bathymetry = TRUE)