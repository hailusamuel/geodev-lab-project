# Week 10: Geopandas, layers as tables

## What this folder contains:
- csv_to_points.py: convert csv table coordinates to point shapefile
- explore_layer.py: check the property of vector (rows, columns, crs, geometry, etc)
- explore_pandas.py: first look at the ward population table
- facilities_map.png: map of health facilities by ward
- filter_sort.py: filtering data by criteria and ordering by ascending/descending values
- geom_props.py: checking the geometry (validity, centroid)
- join_population.py: joins population to ward polygons after cleaning names
- make_map.py: making map of health facilities by ward
- save_outputs.py: copying vector file to another folder and saving as table without geometry information
- wards_table.csv: saved table from vector file

- my_explore.py: display the layer properties of Shebelle_basin_boundary.gpkg
- my_join.py: joining water points layer with sub-basins table
- my_joined_map.png: map showing water points based on their sub-basin from my_join.py
- my_points.py: saving a csv table with coordinates to a point geopackage layer
- my_waterpoints_map.png: map showing water points in the Shebelle Basin from my_points.py


## How to run it
From the repository root:
uv run month-03/week-10/join_population.py

## What I found
- the results of bounds of Shebelle_basin_boundary.gpkg is similar to the extent bounds from QGIS. the terminal displayes min X, min Y and max X and max Y values respectivly

# What went wrong and how I fixed it
- wehen joining one table to one layer based on int join field, cleaning functions for text field (strip(), upper(), replace()) generate error (the functions are not applicable for int field)

- this is fixed by removing the cleaning function; all the fields are joined 100% on the first try