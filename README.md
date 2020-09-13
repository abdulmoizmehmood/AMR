# AMR Prediction

This repository contains Python code for predicting antimicrobial resistance (AMR) using sci-kit learn.

## Folder Structure

- `data/`: Contains raw and processed data files.
- `notebooks/`: Jupyter notebooks for data preprocessing, model training, and evaluation.
- `src/`: Source code for data preprocessing, model training, and evaluation.
- `tests/`: Unit tests for the source code.
- `.gitignore`: Git ignore file.
- `README.md`: Project documentation.
- `requirements.txt`: List of dependencies.
- `setup.py`: Setup file for the project.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/abdulmoizmehmood/AMR.git
    cd AMR
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

### Usage

1. **Data Preprocessing**:
    - Run the `data_preprocessing.ipynb` notebook to clean and preprocess the raw data.

2. **Model Training**:
    - Use the `model_training.ipynb` notebook to train machine learning models on the preprocessed data.

3. **Model Evaluation**:
    - Evaluate the performance of the trained models using the `model_evaluation.ipynb` notebook.

### Project Overview

The project involves the following steps:

1. **Data Preprocessing**: Cleaning and preparing the data for machine learning.
2. **Model Training**: Training various machine learning models to predict AMR.
3. **Model Evaluation**: Evaluating the performance of the models.

### Code Structure

- `data_preprocessing.py`: Functions for data cleaning and preprocessing.
- `model_training.py`: Functions for training machine learning models.
- `model_evaluation.py`: Functions for evaluating model performance.
- `utils.py`: Utility functions.

### Testing

Run the tests using `pytest`:
```bash
pytest tests/
