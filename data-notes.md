## CRS
All source layers are arrived in EPSG: 4326
All layers Reprojected to EPSG: 32638 (UTM 38N) as most of the basin is in this zone; then clipped to the study area.
Basin area: 297,230.7 sq.kms

## Data Preparation
1. Study area: Shebelle Basin, extracted form hydrosheds level 4 data
2. Population data: Downloaded worldpop data for Ethiopia and Somalia, mosaic (merge) the raster and clipped by the basin
the data ranges from 0 to 1,100 population per grid

## Quality issues
Projecting the worldpop data to EPSG: 32638 resulted 93.7m X 93.7m grids, however the data is originated with 100m grid size.
Reprojecting the data with 100m cell size reduced the range severely, so the default 93.7m cell size is taken as it agree with
the range of values from non-projected data.

##Working files in data/processed, row files intact
