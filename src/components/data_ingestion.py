# Data ingestion requires input where to save the data and where to save the train and test data


from sklearn.model_selection import train_test_split    
from dataclasses import dataclass
import pandas as pd
from src.logger import logging

import sys
import os

# Get the absolute path of the directory containing the current file
current_dir = os.path.dirname(os.path.abspath(__file__))
# Go up two levels to reach the project root (ML_Project_Deployment)
project_root = os.path.abspath(os.path.join(current_dir, '..', '..'))

# Add the project root to sys.path
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# Now your imports should work
from src.exception import CustomException



@dataclass
class DataIngestionConfig:
    raw_data_path = os.path.join('artifacts', 'raw_data.csv')
    train_data_path = os.path.join('artifacts', 'train_data.csv')
    test_data_path = os.path.join('artifacts', 'test_data.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info('Data Ingestion method started')
        try:
            df = pd.read_csv('notebook/data/stud.csv')
            logging.info('Dataset read as pandas DataFrame')

            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            logging.info('Train test split initiated')
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
        except Exception as e:
            logging.error(f"Error occurred during data ingestion: {e}")
            raise CustomException(e)

if __name__ == "__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()  # This will run the data ingestion process

