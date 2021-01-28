# Problem Statement

# Objectives

# Process

# Notable Findings

# Dataset Summary

**The United States Accident Dataset** is a nationwide collection of accident data from **49 states**. It contains over **4 million samples** occuring between **February of 2016** and **December of 2019.** 

This dataset was initially created and introduced as a scholarly publication by professors and Phd students at Ohio State University. It was then presented at the International Conference on Advances in Geographic Information Systems in 2019. 

You can find the publication here: https://arxiv.org/abs/1906.05409
You can find more about this dataset here: https://smoosavi.org/datasets/us_accidents


**Citations:**

Moosavi, Sobhan, Mohammad Hossein Samavatian, Srinivasan Parthasarathy, and Rajiv Ramnath. “A Countrywide Traffic Accident Dataset.”, arXiv preprint arXiv:1906.05409 (2019).

Moosavi, Sobhan, Mohammad Hossein Samavatian, Srinivasan Parthasarathy, Radu Teodorescu, and Rajiv Ramnath. “Accident Risk Prediction based on Heterogeneous Sparse Data: New Dataset and Insights.” In proceedings of the 27th ACM SIGSPATIAL International Conference on Advances in Geographic Information Systems, ACM, 2019.


# Data Dictionary

Also located here: https://smoosavi.org/datasets/us_accidents

| Index | Attribute|Description|Nullable|
|-----------: | -----------:| -----------:| -----------: |
|1|ID|This is a unique identifier of the accident record.|No|
|2 | Source | Indicates source of the accident report (i.e. the API which reported the accident.). | No |
|3 | TMC | A traffic accident may have a Traffic Message Channel (TMC) code which provides more detailed description of the event. | Yes |
|4 | Severity | Shows the severity of the accident, a number between 1 and 4, where 1 indicates the least impact on traffic (i.e., short delay as a result of the accident) and 4 indicates a significant impact on traffic (i.e., long delay). | No |
|5 | Start_Time | Shows start time of the accident in local time zone. | No |
|6 | End_Time | Shows end time of the accident in local time zone. End time here refers to when the impact of accident on traffic flow was dismissed. | No |
|7 | Start_Lat | Shows latitude in GPS coordinate of the start point. | No |
|8 | Start_Lng | Shows longitude in GPS coordinate of the start point. | No |
|9 | End_Lat | Shows latitude in GPS coordinate of the end point. | Yes |
|10 | End_Lng | Shows longitude in GPS coordinate of the end point. | Yes |
|11 | Distance(mi) | The length of the road extent affected by the accident. | No |
|12 | Description | Shows natural language description of the accident. | No | 
|13 | Number | Shows the street number in address field. | Yes |
|14 | Street | Shows the street name in address field. | Yes |
|15 | Side | Shows the relative side of the street (Right/Left) in address field. | Yes |
|16 | City | Shows the city in address field. | Yes |
|17 | County | Shows the county in address field. | Yes |
|18 | State | Shows the state in address field. | Yes |
|19 | Zipcode | Shows the zipcode in address field. | Yes |
|20 | Country | Shows the country in address field. | Yes |
|21 | Timezone | Shows timezone based on the location of the accident (eastern, central, etc.). | Yes |
|22 | Airport_Code | Denotes an airport-based weather station which is the closest one to location of the accident. | Yes |
|23 | Weather_Timestamp | Shows the time-stamp of weather observation record (in local time). | Yes |
|24 | Temperature(F) | Shows the temperature (in Fahrenheit). | Yes |
|25 | Wind_Chill(F) | Shows the wind chill (in Fahrenheit). | Yes |
|26 | Humidity(%) | Shows the humidity (in percentage). | Yes |
|27 | Pressure(in) | Shows the air pressure (in inches). | Yes |
|28 | Visibility(mi) | Shows visibility (in miles). | Yes |
|29 | Wind_Direction | Shows wind direction. | Yes |
|30 | Wind_Speed(mph) | Shows wind speed (in miles per hour). | Yes |
|31 | Precipitation(in) | Shows precipitation amount in inches, if there is any. | Yes |
|32 | Weather_Condition | Shows the weather condition (rain, snow, thunderstorm, fog, etc.) | Yes |
|33 | Amenity | A POI annotation which indicates presence of amenity in a nearby location. | No |
|34 | Bump | A POI annotation which indicates presence of speed bump or hump in a nearby location. | No |
|35 | Crossing | A POI annotation which indicates presence of crossing in a nearby location. | No
|36 | Give_Way | A POI annotation which indicates presence of give_way in a nearby location. | No | 
|37 | Junction | A POI annotation which indicates presence of junction in a nearby location. | No | 
|38 | No_Exit | A POI annotation which indicates presence of no_exit in a nearby location. | No |
|39 | Railway | A POI annotation which indicates presence of railway in a nearby location. | No |
|40 | Roundabout | A POI annotation which indicates presence of roundabout in a nearby location. | No | 
|41 | Station | A POI annotation which indicates presence of station in a nearby location. | No |
|42 | Stop | A POI annotation which indicates presence of stop in a nearby location. | No |
|43 | Traffic_Calming | A POI annotation which indicates presence of traffic_calming in a nearby location. | No |
|44 | Traffic_Signal | A POI annotation which indicates presence of traffic_signal in a nearby location. | No |
|45 | Turning_Loop | A POI annotation which indicates presence of turning_loop in a nearby location. | No
|46 | Sunrise_Sunset | Shows the period of day (i.e. day or night) based on sunrise/sunset. | Yes |
|47 | Civil_Twilight | Shows the period of day (i.e. day or night) based on civil twilight. | Yes |
|48 | Nautical_Twilight | Shows the period of day (i.e. day or night) based on nautical twilight. | Yes |
|49 | Astronomical_Twilight | Shows the period of day (i.e. day or night) based on astronomical twilight. | Yes | 


# Data Sharing and Workflow

Data Sharing and workflow has been a challenge on this project. With four people in production of this model and all other aspects of the project it was difficult to handle a large dataset that numbered over 3 million samples after cleaning. 

We initially attempted to use a combination of Github and Google Colab but had issues with our data being removed from the Colab environment every time a notebook session was closed. This lead us to have to reload the data into Colab at the start of each new session. This become tiresome. We also had challenges with sharing updated or modified CSVs. File size was not only an issue with Colab but even Github with large file sharing extension was unable to handle the size of our data which was around 3.14GB after pushing up to Google Big Query. 

To solve this problem of sharing the data from a common location and allowing us to update our source data we moved to Google Big Query. This was still challenging as we had issues with permissioning all team members to access the data. 

#### TO DO: Jaco and Nat Document How they set up. 

Steps to Setup Bigquery

* Edit Permissions
    * Change Each users role to BigQuery User and BigQuery Data Editor.


Choose Project dsi-team-project and then choose open. 


# Kepler.gl Installation and Usage

Kepler.gl is a powerful open source  and interctive geospatial analysis tool for large-scale data sets. It can be used in the web at kepler.gl and also within Jupyter Notebook.

### Using Kepler.gl via web

https://kepler.gl/

### Using Kepler.gl via Jupyter

Using Kepler.gl in Jupyter Notebook Documentation:
https://docs.kepler.gl/docs/keplergl-jupyter

An explanatory Medium article walking through Keppler in Jupyter from installation to visualization:
https://medium.com/vis-gl/introducing-kepler-gl-for-jupyter-f72d41659fbf

**Install Kepler.gl**

`pip install keplergl`

**If using Jupter Lab you also need to install the JupyterLab extension.**

* Jupyter also requires node greater than verion 10.15.0
* With Homebrew installed on Mac you can install node this way. 

`brew install node@10`

**Finally, install Jupyter Lab extension**

`jupyter labextenstion install @jupyter-widgets/jupyterlab-manager keplergl-jupyter`
* Note: We had difficulty getting Keppler to work within Jupyter Lab. After switching to Jupyter Notebook it deployed correctly. 


**Kepler.gl Jupyter Notebook Dependencies**

* Python greater than version 2
* ipywidgets greter than version 7


_______________________

# Geopandas Installation and Usage

GeoPandas is an open source project to make working with geospatial data in python easier. GeoPandas extends the datatypes used by pandas to allow spatial operations on geometric types. Geometric operations are performed by shapely. Geopandas further depends on fiona for file access and descartes and matplotlib for plotting. Like it's name suggests, Geopandas is designed to work similarly to the Pandas library but more specifically for Geospatial data. 

**Geopandas User Guide**
https://geopandas.org/

**Geopandas Examples Gallery**
https://geopandas.org/gallery/index.html

**Geopandas Install Documentation:**

https://geopandas.org/install.html

**install Geopandas**

`conda install --channel conda-forge geopandas`

or 

`conda install --channel conda-forge geopandas`

or 

`pip install geopandas`

**See Geopandas install documentation above for more information on each install method and for alternative methods of install directly from Github.**

**GEOPANDAS DEPENDENCIES** Also found in the above Geopandas documentation. 

* numpy
* pandas (version 0.23.4 or later)
* shapely (interface to GEOS)
* fiona (interface to GDAL)
* pyproj (interface to PROJ; version 2.2.0 or later)

**See install link above for further, optional dependencies:**


