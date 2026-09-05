import os 
import sys
from dataclasses import dataclass
from src.exception import CustomException
from src.logger import logging

import numpy as np
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler
from sklearn.impute import SimpleImputer

from src.utils import save_object

@dataclass
class DataTransformationConfig:
    preprocessor_obj_path = os.path.join('artifacts','preprocessor.pkl')

class DataTransformation:
    def __init__(self):
        self.data_transfomation_config = DataTransformationConfig()

    def data_transformer_object(self):

        '''this methon responsable for the data transformation'''
        try:
        
            # Numerical columns
            numerical_columns = [
                "SeniorCitizen",
                "tenure",
                "MonthlyCharges",
                "TotalCharges"
            ]
            # Binary categorical columns
            # These will be converted manually to 0/1
            binary_columns = [
                "gender",
                "Partner",
                "Dependents",
                "PhoneService",
                "PaperlessBilling"
            ]
            # Remaining categorical columns
            categorical_columns = [
                "MultipleLines",
                "InternetService",
                "OnlineSecurity",
                "OnlineBackup",
                "DeviceProtection",
                "TechSupport",
                "StreamingTV",
                "StreamingMovies",
                "Contract",
                "PaymentMethod"
            ]

            logging.info('Creating numarical pipeline')
            num_pipeline = Pipeline(
                steps=[
                    ('imputer', SimpleImputer(strategy='mean')),
                    ('scaler',StandardScaler())
                ]
            )
            logging.info('Creating categorical pipeline')

            cat_pipeline = Pipeline(
                steps=[
                    ('imputer',SimpleImputer(strategy='most_frequent')),
                    ('OneHotEncoding',OneHotEncoder(handle_unknown="ignore")),
                    # ('scaler',StandardScaler(with_mean='False'))
                ]
            )
            logging.info("Creating Columns Transformer")
            preprocessor = ColumnTransformer(
                [
                ("numaric_pipeline", num_pipeline,numerical_columns),
                ('Categorical_pipeline',cat_pipeline,categorical_columns)
                ]
            )
            logging.info("Pipeline is done")
            return preprocessor
        
        except Exception as e:
            raise CustomException(e,sys)
    def initaite_data_transformation(self,train_path, test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            logging.info('Read train & test data compeleted')

            logging.info("Convert Total_Charges into numeric")
            train_df['TotalCharges'] = pd.to_numeric(train_df['TotalCharges'],errors='coerce')
            test_df['TotalCharges'] = pd.to_numeric(test_df['TotalCharges'],errors='coerce')


            ## conver binary columns 
            binary_maping = {
                'Yes':1,
                'No' : 0,
                'Male':1,
                "Female":0
            }
            binary_columns = [
                            "gender",
                            "Partner",
                            "Dependents",
                            "PhoneService",
                            "PaperlessBilling"
                        ]

            for col in binary_columns:
                train_df[col] = train_df[col].map(binary_maping)
                test_df[col] = test_df[col].map(binary_maping)

            # convert churn Yes/No in 1/0
            train_df['Churn'] = train_df['Churn'].map(
                {
                    'Yes':1,
                    'No' : 0
                }
            )

            test_df['Churn'] = test_df['Churn'].map(
                        {
                            'Yes':1,
                            'No' : 0
                        }
                    )
            preprocessing_obj = self.data_transformer_object()

            target_column_name="Churn"
            

            input_feature_train_df=train_df.drop(columns=[target_column_name],axis=1)
            target_feature_train_df=train_df[target_column_name]

            input_feature_test_df=test_df.drop(columns=[target_column_name],axis=1)
            target_feature_test_df=test_df[target_column_name]

            logging.info(
                f"Applying preprocessing object on training dataframe and testing dataframe."
            )

            input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr=preprocessing_obj.transform(input_feature_test_df)

            train_arr = np.c_[
                input_feature_train_arr, np.array(target_feature_train_df)
            ]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

        

            save_object(
                file_path = self.data_transfomation_config.preprocessor_obj_path,
                obj = preprocessing_obj
            )
            logging.info('Saved preprocessing object')
            return (
                train_arr,
                test_arr,
                self.data_transfomation_config.preprocessor_obj_path
            )
        
        except Exception as e:
            raise CustomException(e,sys)