# Income_Inequality
Using census data to predict magnitude of income inequality in a county 
This 2015 data was obtained from the US Census Bureau Website, in particular through the Fact Finder interface. All downloaded data was read into pandas, minimally processed, and saved as a csv files. Data are located in the ./data folder.

## Questions

  1. Can I predict income inequality in a county (measured by difference between top income quintile and bottom income quintile) based on factors like:
     - Educational attainment - 
     - Proportion of population major ethnic groups - 
     - Population density - *Master*
     - Birth rate - *all_data*
     - Unemployment rate - need to find
     - Target - diff between lowest and highest quintile https://factfinder.census.gov/faces/tableservices/jsf/pages/productview.xhtml?src=bkmk
          - this will be positive, bounded by zero. 
          - likely NA's for some low-pop counties
  2. Do counties in population-dense states have meaningfully different income inequality vs low-density states?


## Getting Started

- First pane in the Jupyter notebook contains all necessary imports. Additional helper functions are defined throughout the Jupyter notebook.
- All code for this project will be based in Python3

### Prerequisites

  - Numpy
  - Pandas
  - Sklearn
  - Maplotlib
  - Seaborn
  
## Built With

* [Scikit-learn](http://scikit-learn.org/stable/) - Modeling
* [Seaborn](https://seaborn.pydata.org/) - Data Visualization
* [Scipy] (https://www.scipy.org) - Statistical Analysis


## Author

* **Alex Frech**

## Acknowledgments

* Adam Richards, Chris Feller for project advising
* Amelia Maier for correlation heat map
