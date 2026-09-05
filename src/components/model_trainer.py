import os
import sys
from src.logger import logging
from src.exception import CustomException

from src.utils import evaluate_models
from dataclasses import dataclass

from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier,AdaBoostClassifier
from xgboost import XGBClassifier
# from catboost import CatBoostClassifier

from src.utils import save_object

@dataclass
class ModelTrainerConfig:
    model_tainer_file_path = os.path.join('artifacts','model.pkl')

class ModelTrainer:
    def __init__(self):
        self.model_tainer_config = ModelTrainerConfig()

    def initiate_model_trainer(self,train_array,test_array):
        try:
            X_train,y_train,X_test,y_test = (
                    train_array[:,:-1],
                    train_array[:,-1],
                    test_array[:,:-1],
                    test_array[:,-1]
                )
            models = {
                'LogisticRegression' : LogisticRegression(),
                'SVC' : SVC(),
                'KNeighborsClassifier' : KNeighborsClassifier(),
                'DecisionTreeClassifier' : DecisionTreeClassifier(),
                'RandomForestClassifier' : RandomForestClassifier(),
                'AdaBoostClassifier' : AdaBoostClassifier(),
                'XGBClassifier' : XGBClassifier(),
                # 'CatBoostClassifier' : CatBoostClassifier()
            }

            params = {

                "LogisticRegression": {
                    "C": [0.01, 0.1, 1, 10],
                    "solver": ["liblinear", "lbfgs"],
                    "max_iter": [500, 1000],
                    "class_weight": [None, "balanced"]
                },

                "SVC": {
                    "C": [0.1, 1, 10],
                    "kernel": ["linear", "rbf"],
                    "gamma": ["scale", "auto"],
                    "class_weight": [None, "balanced"]
                },

                "KNeighborsClassifier": {
                    "n_neighbors": [3, 5, 7, 9],
                    "weights": ["uniform", "distance"],
                    "metric": ["euclidean", "manhattan"]
                },

                "DecisionTreeClassifier": {
                    "criterion": ["gini", "entropy"],
                    "max_depth": [3, 5, 10, None],
                    "min_samples_split": [2, 5, 10],
                    "class_weight": [None, "balanced"]
                },

                "RandomForestClassifier": {
                    "n_estimators": [100, 200],
                    "max_depth": [5, 10, None],
                    "min_samples_split": [2, 5],
                    "class_weight": [None, "balanced"]
                },

                "AdaBoostClassifier": {
                    "n_estimators": [50, 100, 200],
                    "learning_rate": [0.01, 0.1, 1.0]
                },

                "XGBClassifier": {
                    "n_estimators": [100, 200],
                    "max_depth": [3, 5, 7],
                    "learning_rate": [0.01, 0.1, 0.2],
                    "scale_pos_weight": [1, 2, 2.77, 3]
                }

                # "CatBoostClassifier": {
                #     "iterations": [100, 200, 300],
                #     "depth": [4, 6, 8],
                #     "learning_rate": [0.01, 0.1, 0.2],
                #     "l2_leaf_reg": [1, 3, 5]
                # }
            }

            model_report = evaluate_models(X_train=X_train,X_test=X_test,y_train=y_train,y_test=y_test,models=models,prams=params)

            ## find the best model score from the dict

            best_model_score = max(list(model_report.values()))

            ## to get the best model name from the dict 

            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]
            best_model = models[best_model_name]

            # print("MODEL REPORT:", model_report)
            # print("BEST MODEL SCORE:", best_model_score)

            if best_model_score<0.6:
                raise CustomException("No best model found")
            logging.info(f"Best found model on both training and testing dataset")

            save_object(
                file_path=self.model_tainer_config.model_tainer_file_path,
                obj=best_model
            )
            
        except Exception as e:
            raise CustomException(e,sys)