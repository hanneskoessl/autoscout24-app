# AutoScout24 Analysis and Price Prediction App

This application allows you to analyze AutoScout24 data from Germany and make predictions about car prices based on custom inputs.

## Contents

- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
  - [Analysis Page](#analysis-page)
  - [Price Prediction Page](#price-prediction-page)
- [Data Source](#data-source)
- [License](#license)

## Overview

This Streamlit app consists of two main pages:

1. **Analysis Page**: View, filter, and visualize AutoScout24 data to discover trends and patterns in car prices.
2. **Price Prediction Page**: Enter specific vehicle data to get an instant price prediction.



## Installation

To run the app locally, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/autoscout24-app.git
    cd autoscout24-app

2. **Download the dataset**:
    Download the dataset from Kaggle [here](https://www.kaggle.com/datasets/ander289386/cars-germany). Place the downloaded CSV-file in the root directory of the cloned repository.

2. **Install dependencies**:
    Make sure you have Python 3.7+ installed. Then, install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the app**:
    ```bash
    streamlit run app.py
    ```

## Usage

### Analysis Page

- **Data Display**: View the complete AutoScout24 dataset, browse, and filter the data by make, model, price, mileage, and more.
- **Charts**: Select different charts to visualize price distribution, average prices by make, mileage, and more.

### Price Prediction Page

- **Input**: Enter specific vehicle details such as make, model, year, mileage, and fuel type.
- **Result**: The app calculates a price prediction for the car based on your input.

## Data Source

The data used in this app is sourced from Kaggle and can be downloaded [here](https://www.kaggle.com/datasets/ander289386/cars-germany). The dataset includes detailed information on cars sold in Germany.

## License

This app is released under the MIT License. For more details, please refer to the [LICENSE](LICENSE) file.

---

Enjoy using the AutoScout24 Analysis and Price Prediction App! If you have any questions or encounter any issues, please open an issue in this repository.
