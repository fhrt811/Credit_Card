import os
import sys
import pandas as pd
import numpy as np
import pickle
from sklearn.metrics import mean_absolute_error, mean_squared_error,r2_score
from src.exception import CustomException
from src.logger import logging

def save_object(file_path,obj):
    try:
        dir_path=os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)

        with open(file_path, 'wb') as file_obj:
            pickle.dump(obj,file_obj)
    except Exception as e:
        logging.info('Error in saving pickle file')
        raise CustomException(e,sys)