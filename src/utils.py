import sys
from sklearn.metrics import recall_score,f1_score,precision_score,accuracy_score
from sklearn.model_selection import GridSearchCV

from src.exception import CustomException
from src.logger import logging

import os
import dill



def evaluate_models(X_train,X_test,y_train,y_test,models,prams):

    try:
        report = {}
        for i in range(len(list(models))):
            model = list(models.values())[i]
            param = prams[list(models.keys())[i]]

            gs = GridSearchCV(
                estimator=model,
                param_grid=param,
                cv=3,
                n_jobs=-1,
                scoring='recall'
            )
            gs.fit(X_train,y_train)

            model.set_params(**gs.best_params_)

            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)

            train_model_score = recall_score(y_train, y_train_pred)
            test_model_score = recall_score(y_test, y_test_pred)

            report[list(models.keys())[i]] = test_model_score

        return report
        
    except Exception as e:
        raise CustomException(e,sys)

def save_object(file_path , obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path,exist_ok=True)

        with open(file_path,'wb') as file_obj:
            dill.dump(obj,file_obj)
    except Exception as e:
        raise CustomException(e,sys)