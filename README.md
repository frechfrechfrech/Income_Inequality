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
  2. Does median education rate impact income inequality?
  3. Does birth rate impact income inequality?

## Getting Started

- Take a look at the Jupyter notebook for a detailed view of imports and settings.
- All code for this project will be based in Python3

### Prerequisites

  - Numpy
  - Pandas
  - Sklearn
  - Maplotlib
  - Seaborn

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Built With

* [Scikit-learn](http://scikit-learn.org/stable/) - Modeling package
* [Seaborn](https://seaborn.pydata.org/) - Data visualization package

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Author

* **Alex Frech**

## Acknowledgments

* Adam Richards and Chris Feller for project advising
