library(ggplot2)
library(mapdata)
library(readr)
library(dplyr)

# import data set
coraldata <- read_csv("coraldata.csv", show_col_types = FALSE)
head(coraldata, 5)
colnames(coraldata)

# create new csv to simplify
refineddata <- select(coraldata, "LON", "LAT", "SEVERITY_CODE")
head(refineddata, 10)

# covert data to dataframe
coral_df <- data.frame(lon = refineddata$LON, lat = refineddata$LAT, value = refineddata$SEVERITY_CODE)
head(coral_df)

# get world map data
world_map <- map_data("world")
head(world_map,10)

# create heat map using ggplot2
ggplot() +
  geom_polygon(data = world_map, aes(x = long, y = lat, group = group), fill = "white", color = "grey") +
  geom_point(data = coral_df, aes(x = lon, y = lat, fill = value), size = 2, shape = 21) +
  scale_fill_gradient(low = "white", high = "red") +
  labs(x = "Longitude", y = "Latitude", title = "Severity Heat Map")

