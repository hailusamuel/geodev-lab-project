import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

water_pts = pd.read_csv("Shebelle_waterpoints.csv")
water_pts_gdf = gpd.GeoDataFrame(water_pts, geometry=gpd.points_from_xy(water_pts.X, water_pts.Y), crs="EPSG:32638")

print(water_pts_gdf.head())
print("Rows and columns:", water_pts_gdf.shape)
print("Geometry types:", water_pts_gdf.geom_type.value_counts())
print("CRS:", water_pts_gdf.crs)
print("Bounds:", water_pts_gdf.total_bounds)

water_pts_gdf.to_file("data/processed/Shebelle_waterpoints.gpkg", layer="waterpoints")
print("Saved", len(water_pts_gdf), "water points to data/processed/Shebelle_waterpoints.gpkg")

basin = gpd.read_file("Shebelle_basin_boundary.gpkg", layer="Basin")
fig, ax = plt.subplots(figsize=(10, 10))
basin.boundary.plot(ax=ax, color="blue", linewidth=2)
water_pts_gdf.plot(ax=ax, color="red", markersize=10)
ax.set_title("Water Points in Shebelle Basin")
ax.set_axis_off()
fig.savefig("month-03/week-10/my_waterpoints_map.png", dpi=150, bbox_inches="tight")
print("Map saved to month-03/week-10/my_waterpoints_map.png")