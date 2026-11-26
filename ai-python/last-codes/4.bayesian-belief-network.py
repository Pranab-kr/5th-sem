import numpy as np
import pandas as pd
from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.inference import VariableElimination

heartDisease = pd.read_csv('HEART.csv')
heartDisease = heartDisease.replace('?', np.nan)

print('Few examples from the dataset are given below:')
print(heartDisease.head())

print('\nChecking for missing values:')
print(heartDisease.isnull().sum())

heartDisease.dropna(inplace=True)

categorical_cols = ['sex', 'fbs', 'restecg', 'exang', 'slope', 'ca', 'thal', 'target']
for col in categorical_cols:
    heartDisease[col] = heartDisease[col].astype('category')

heartDisease['age'] = pd.to_numeric(heartDisease['age'], errors='coerce')
print('\nUnique values of age:')
print(heartDisease['age'].unique())

model = DiscreteBayesianNetwork([
    ('age', 'trestbps'),
    ('age', 'fbs'),
    ('sex', 'trestbps'),
    ('exang', 'trestbps'),
    ('trestbps', 'target'),
    ('fbs', 'target'),
    ('target', 'restecg'),
    ('target', 'thalach'),
    ('target', 'chol')
])

print('\nLearning CPD using Maximum Likelihood Estimators...')
model.fit(heartDisease, estimator=MaximumLikelihoodEstimator)

print('\nInference with Bayesian Network:')
HeartDisease_infer = VariableElimination(model)

age_value = 58
print(f'\n1. Probability of HeartDisease given Age={age_value}:')
q1 = HeartDisease_infer.query(variables=['target'], evidence={'age': age_value})
print("Probabilities of Heart Disease based on age:")
for state, probability in zip(q1.state_names['target'], q1.values):
    print(f'Probability of target={state}: {probability:.4f}')

chol_value = 212
print('\n 2. Probability of heartDisease given cholesterol=212')
q2 = HeartDisease_infer.query(variables=['target'], evidence={'chol': chol_value})
print("Probabilities of Heart Disease based on cholesterol:")
for state, probability in zip(q1.state_names['target'], q2.values):
    print(f'Probability of target={state}: {probability:.4f}')