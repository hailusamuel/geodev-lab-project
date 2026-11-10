import geopandas as gpd
print(gpd.list_layers("Shebelle_basin_boundary.gpkg"))

basin = gpd.read_file("Shebelle_basin_boundary.gpkg", layer="Basin")

print(basin.head())
print("Rows and columns:", basin.shape)
print(basin.geom_type.value_counts())
print("CRS:", basin.crs)
print("Bounds:", basin.total_bounds)