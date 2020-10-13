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
```

# Docker Setup for AMR Prediction Project

This repository contains Python code for predicting antimicrobial resistance using python scikit-learn. This guide explains how to dockerize the project and interact with the Docker container to run the code.`

## Prerequisites

Docker installed on your machine. You can download it from [here](https://www.docker.com/get-started).

## Building the Docker Image

- `Navigate to the root directory of your project and build the Docker image by running the following command:

```bash
docker build -t amr_prediction:latest .
```

## Running the Docker Container

- After building the Docker image, you can run the Docker container using Docker Compose:

```bash
docker-compose up
```

- `This command will start the Jupyter Notebook server, and you will be able to access it at http://localhost:8888 in your web browser. Use the token provided in the terminal to log in.
Interacting with the Docker Container

- Once the container is running, you can interact with it in several ways:

## Running Jupyter Notebooks

    Open your web browser and go to http://localhost:8888.
    Use the token provided in the terminal to log in.
    Open the notebooks in the notebooks/ directory to run the data preprocessing, model training, and model evaluation steps.

## Running Python Scripts

- You can also run the Python scripts directly within the container. To do this, first, open a terminal session inside the running container:

```bash
docker-compose exec amr_prediction /bin/bash
```
Once you are inside the container, you can run any of the Python scripts. For example, to preprocess the data, run:

```bash
python src/data_preprocessing.py
```
- `To train the models, run:

```bash
python src/model_training.py
```
- `To evaluate the models, run:

```bash
python src/model_evaluation.py
```
## Testing

You can run the tests inside the container as well. First, open a terminal session inside the running container:

```bash
docker-compose exec amr_prediction /bin/bash
```

- Then, run the tests using pytest:

```bash
pytest tests/
```

## Stopping the Docker Container

- To stop the Docker container, press Ctrl+C in the terminal where you ran docker-compose up. Alternatively, you can stop the container using the following command:

```bash
docker-compose down
```

## Cleaning Up

- If you want to remove the Docker images and containers, you can use the following commands:

```bash
docker-compose down --rmi all
docker system prune -f
```

- This guide should help you set up Docker for the AMR Prediction project and interact with the code effectively. If you have any questions or encounter any issues, please open an issue on the GitHub repository.


- Feel free to adjust any parts of this script to fit your specific project needs! If you have any questions or need further assistance, just let me know.