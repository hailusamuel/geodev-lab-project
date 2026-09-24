## Question
Where are the gaps in water source coverage in the Shebelle Transboundary Basin (Ethiopia-Somalia) relative to population?

## Operations
0. Merge water sources from different sources after reprojecting to EPSG: 32638.
1. Aggregate water sources within 30m distance from each other while appending unique attribute values (handling duplicates).
2. Buffer 2km from water sources, dissolved - areas covered by water sources.
3. Convert grided worldpop data to vector - representing populations (settlement).
4. Make buffer of 1km from settlement (dissolved) were water sources can be placed.
5. Make the difference of 4 and 2 - representing settlement areas not covered by water sources.
6. Clip the difference by basin boundary (study area) - representing settlement areas not covered by water sources in the study area.

## Expected
Good coverages of larger settlements (towns) by watersources

## Got
Some towns are not covered by watersources (such as Gode Town)

## What surprised me 🤨 
Large settlements (towns) known to have partial water source coverage are under no coverage zones.
This suggests water sources database is not complete and well distributed.

## Limitations
- Straight line distance form water sources is considered (2 km buffer) not travel distance
- Water points data base has gaps both in terms of number of sources and their distribution
- Water points data base has undefined source type values ('Unknown', 'Other')

## What I still need
- Road network with surface, to calculate travel distance from water sources
- Additional water sources data from different sources to enrich the database






