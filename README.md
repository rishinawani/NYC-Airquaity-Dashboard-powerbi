# NYC-Airquaity-Dashboard-powerbi
This project involved an end-to-end data pipeline, analyzing New York City's air quality data (2017–2022) to uncover trends and actionable insights.
## ETL Process
#### Sourced data from a government website on air quality.
#### Cleaned and transformed data using Python to handle inconsistencies and prepare it for analysis.
#### Transferred the processed data into PGadmin.
#### Built a custom API in Python to seamlessly connect the database to Power BI for reporting.
## Data Modeling
![datamode](https://github.com/rishinawani/NYC-Airquaity-Dashboard-powerbi/blob/main/datamodel.PNG)
#### Transformed a single, large dataset into a star schema for better analysis:
#### Fact Table: Air quality metrics.
#### Dimension Tables: Geographic data and health-related metrics.
#### Normalized data, created indexes for performance, and defined one-to-many relationships between tables to ensure data integrity and scalability.
## Visualisation
 #### Regional Pollution Trends: Visualized pollution levels across five regions, showing a notable drop in 2021–2022.
 #### Seasonal Analysis: Highlighted higher pollution levels during summer compared to winter.
 #### Health Impact Analysis: Tracked health cases related to pollution, revealing time-based patterns.
 #### Pollutant Composition: Identified Nitrogen Dioxide (NO₂) as the largest pollutant contributor, followed by ozone.
![dashoard](https://github.com/rishinawani/NYC-Airquaity-Dashboard-powerbi/blob/main/dashoard_y.PNG)



