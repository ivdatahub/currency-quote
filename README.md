# currency-quote-wrapper: Complete solution for extracting currency pair quotes data

![Project Status](https://img.shields.io/badge/status-done-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue) 
![GitHub release (latest by date)](https://img.shields.io/github/v/release/IvanildoBarauna/currency-quote-wrapper)
![Python Version](https://img.shields.io/badge/python-3.9-blue) 
![GitHub Workflow Status](https://github.com/IvanildoBarauna/currency-quote-wrapper/actions/workflows/CI-CD.yaml/badge.svg)
[![codecov](https://codecov.io/gh/IvanildoBarauna/currency-quote-wrapper/branch/main/graph/badge.svg?token=GEGNHFM6P)](https://codecov.io/gh/IvanildoBarauna/currency-quote-wrapper)

## Project Stack

<img src="https://github.com/devicons/devicon/blob/master/icons/python/python-original.svg" Alt="Python" width="50" height="50"> <img src="https://github.com/devicons/devicon/blob/master/icons/docker/docker-original.svg" Alt="Docker" width="50" height="50"> <img src="https://github.com/devicons/devicon/blob/master/icons/poetry/poetry-original.svg" Alt="Poetry" width="50" height="50"> <img src="https://github.com/devicons/devicon/blob/master/icons/pandas/pandas-original.svg" Alt="Pandas" width="50" height="50"> <img src="https://github.com/devicons/devicon/blob/master/icons/jupyter/jupyter-original.svg" Alt="Jupyter" width="50" height="50"> <img src="https://github.com/devicons/devicon/blob/master/icons/matplotlib/matplotlib-original.svg" Alt="Matplotlib" width="50" height="50"> <img src="https://github.com/devicons/devicon/blob/master/icons/githubactions/githubactions-original.svg" Alt="GitHub Actions" width="50" height="50">

## Project description

* ADD DESCRIPTION

## Contributing

See the following docs:

- [Contributing Guide](https://github.com/IvanildoBarauna/currency-quote-wrapper/blob/main/CONTRIBUTING.md)
- [Code Of Conduct](https://github.com/IvanildoBarauna/currency-quote-wrapper/blob/main/CODE_OF_CONDUCT.md)

## Project Highlights:

- Comprehensive Testing: Development of tests to ensure the quality and robustness of the code at various stages of the ETL process

- Parallelism in Models: Use of parallelism in the data transformation and loading stages, increasing efficiency and reducing processing time.

- Fire-Forget Messaging: Use of messaging (queue.queue) in the fire-forget model to manage files generated between the transformation and loading stages, ensuring a continuous and efficient data flow.

- Parameter Validation: Sending valid parameters based on the request data source itself, ensuring the integrity and accuracy of the information processed.

- Configuration Management: Use of a configuration module to manage endpoints, retry times and number of attempts, providing flexibility and ease of adjustment.

## How to use it

``` python
## Importing library
from currency_quote import GetData, GetDataTypes

last_quote = GetData("USD-BRL", GetDataTypes.LastCotation)

x = 2024-01-01
y = 2024-02-02
 
quote_by_period = GetData("USD-BRL", GetDataTypes.Period, start_date=x, end_date=y)