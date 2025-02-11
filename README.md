# World-Bank-API-Data-Engineering

---

# Top Countries by Population - Interactive Bar Chart

This Python function fetches population data for countries around the world from the World Bank API, processes it, and displays the top countries by population using Plotly for interactive visualizations.

## Libraries Used

1. **wbgapi**: A Python library for accessing the World Bank's World Development Indicators (WDI) and other data available through the World Bank API.
   - Source: [wbgapi Documentation](https://pypi.org/project/wbgapi/)
   
2. **pandas**: A powerful and flexible Python library used for data manipulation and analysis. It is particularly useful for handling structured data and cleaning, transforming, and analyzing datasets.
   - Source: [Pandas Documentation](https://pandas.pydata.org/pandas-docs/stable/)
   
3. **pycountry**: A Python library that provides access to ISO standard lists of countries, subdivisions, currencies, and languages.
   - Source: [pycountry Documentation](https://pypi.org/project/pycountry/)
   
4. **plotly**: A graphing library that makes interactive, publication-quality graphs online. It supports various types of charts, including bar charts, line charts, scatter plots, etc.
   - Source: [Plotly Documentation](https://plotly.com/python/)
   
5. **plotly.express**: A high-level wrapper for Plotly, which simplifies the creation of various plots.
   - Source: [Plotly Express Documentation](https://plotly.com/python/plotly-express/)

---

## Function Overview

The function `top_countries_by_population(num_countries=10)` does the following:

1. **Fetches population data**: Retrieves population data for all available countries and years using the World Bank API via the `wbgapi` library.
2. **Data Preprocessing**:
   - Cleans up the data by removing invalid entries (non-country rows).
   - Selects the most recent year dynamically.
3. **Sorting & Selection**: Sorts countries by population and selects the top `num_countries` countries (default 10).
4. **Visualization**: Creates an interactive horizontal bar chart using `plotly.express`, displaying the population of the top countries.
5. **Hover Information**: The chart allows hovering to display:
   - Country Name
   - Country Code
   - Population
6. **Layout Customization**: Customizes the chart's appearance, such as axis titles, grid lines, and canvas size, to ensure clarity.

---

## Example of Usage

```python
# Get the top 10 countries by population and display the interactive chart
top_countries_by_population(25)
```
![image](https://github.com/user-attachments/assets/9fab59f8-7c06-41ae-afcc-dcfd16cee2b3)



---

## Requirements

To run this code, you need to install the following Python libraries:

```bash
pip install wbgapi pandas pycountry plotly
```

---

## References

- **World Bank API**: [World Bank Data](https://data.worldbank.org/)
- **Plotly**: [Plotly Python](https://plotly.com/python/)
- **Pandas**: [Pandas Documentation](https://pandas.pydata.org/pandas-docs/stable/)
- **pycountry**: [pycountry Documentation](https://pypi.org/project/pycountry/)

---

This README file provides a brief overview of the libraries and sources used in the function to ensure a smooth setup and understanding of the code.
