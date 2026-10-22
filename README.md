# MY Geodev Lab Africa Project
Where are the gaps in borehole coverage in the Shebelle Transboundary Basin (Ethiopia-Somalia) relative to population?

Built over twelve months with Geodev Lab Africa, Cohort One.

project-brief.md outlines the data sources used in the project with a source link for every dataset.

data-notes.md describes data download & preparation, CRS conversation as well as quality checks and issues. 

month-1-summary.md summarizes data processing (operations) expected results, abnormal behaviour, limitations and what is needed.

Water sources coverage gaps.png is the map produced in response to the project question 🙋.

# Month 2: development environment and early Python
Week 5: set up Python, VS Code and the terminal

hello.py - file created in VS code to check the terminal reads python file (working python extension)
screenshots/week5.png - screenshot of the VS code terminal running python commands

Week 6: set up the project with uv and add pandas

check.py - file created in VS code to check pandas is installed (prints pandas version)
project.toml - automatically created by uv init (start project) showing project descriptions and list of dependacy

uv.lock - automatically created by uv add (install package) and updated after every package installation; not to be edited manaually

screenshots/week6.png - screenshot of the VS code terminal uv running python commands

Week 7: python, the variable, the type, the list, the loop, the condition and the function

analyse.py ready wards.csv, converts each area and classifies each ward based on size

Week 8: inspect_data.py summarizes shebelle_waterpoints.csv
it gives count, minimum, maximum and average for the columns of 'SWL_elv', 'TDS', 'Transmissi' and 'SWL(m)'
it also prints the count of non-numeric values not converted to float, and return the summaries for numeric columns
if the count of float values is zero for a given column, it displays  "There are no values in the column."
