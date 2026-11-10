import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

sub_basins = pd.read_csv("Shebelle_sub_basins.csv")
list = gpd.list_layers("data/processed/Shebelle_waterpoints.gpkg")
print(list)

water_pts = gpd.read_file("data/processed/Shebelle_waterpoints.gpkg", layer="waterpoints")
print(water_pts.head(3))

joined = water_pts.merge(sub_basins, left_on="wp_id", right_on="fid", how="left")
matched = joined["Sub_Basin"].notna().sum()
print("Matched:", matched, "of", len(water_pts))

print(joined[["fid", "Sub_Basin"]].head(10))

joined.plot(column="Sub_Basin", legend=True, cmap = "viridis",figsize=(10, 10))
plt.title("Water Points by Sub-Basin")
plt.savefig("month-03/week-10/my_joined_map.png", dpi=150, bbox_inches="tight")

plt.show()
print("Map saved to month-03/week-10/my_joined_map.png")