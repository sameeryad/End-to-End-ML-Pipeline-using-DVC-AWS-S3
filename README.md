# End-to-End ML Pipeline using DVC and AWS S3

This repository contains an end-to-end Machine Learning pipeline for SMS Spam Detection using DVC (Data Version Control) and AWS S3 integration.

## Project Structure
- `src/data_ingestion.py`: Ingests and splits raw dataset into train and test sets.
- `src/data-preprocessing.py`: Cleans, tokenizes, removes stopwords, and stems text.
- `src/feature_engineering.py`: Applies TF-IDF vectorization.
- `src/model_building.py`: Trains a Random Forest Classifier.
- `src/model_evaluation.py`: Evaluates model performance and tracks metrics with DVCLive.
- `logger.py`: Unified logging configuration for all pipeline stages.
- `params.yaml`: Configuration parameters for pipeline stages.
- `experiments/`: Jupyter notebooks and dataset experiments.
