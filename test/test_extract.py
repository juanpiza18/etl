from ..pipeline import Pipeline
import pandas as pd
import numpy as np

def test_no_duplicated_rows():
  pipeline = Pipeline()
  pipeline.extract()
  pipeline_duplicated = pipeline.population[pipeline.population.duplicated()]
  assert pipeline_duplicated.empty

def test_extracted_population_contains_all_expected_columns(): 
  pipeline = Pipeline()
  pipeline.extract()
  expected_columns = [
    'CBSA',
    'MDIV',
    'STCOU',
    'NAME',
    'LSAD',
    'POPESTIMATE2010',
    'POPESTIMATE2011',
    'POPESTIMATE2012',
    'POPESTIMATE2013',
    'POPESTIMATE2014',
    'POPESTIMATE2015',
    'POPESTIMATE2016',
    'POPESTIMATE2017',
  ]
  
  assert set(expected_columns).issubset(set(pipeline.population.columns.to_list()))

def test_extracted_population_columns():
  pipeline = Pipeline()
  pipeline.extract()
  pipeline.population.dtypes.to_dict()
  print(pipeline.population.dtypes.to_dict())
  column_types = {
    'CBSA': np.dtype('int64'),
    'MDIV': np.dtype('float64'),
    'STCOU': np.dtype('float64'),
    'NAME': np.dtype('O'),
    'LSAD': np.dtype('O'),
    'POPESTIMATE2010': np.dtype('int64'),
    'POPESTIMATE2011': np.dtype('int64'),
    'POPESTIMATE2012': np.dtype('int64'),
    'POPESTIMATE2013': np.dtype('int64'),
    'POPESTIMATE2014': np.dtype('int64'),
    'POPESTIMATE2015': np.dtype('int64'),
    'POPESTIMATE2016': np.dtype('int64'),
    'POPESTIMATE2017': np.dtype('int64'),
  }

  assert set(column_types).issubset(set(pipeline.population.dtypes.to_dict()))

def test_no_null_values_population_cbsa():
  pipeline = Pipeline()
  pipeline.extract()
  pipeline_cbsa_nulls = pipeline.population[pipeline.population['CBSA'].isnull()]
  assert pipeline_cbsa_nulls.empty

def test_population_city_names_unique():
  pipeline = Pipeline()
  pipeline.extract()
  pipeline_duplicated = pipeline.population[pipeline.population[['NAME', 'LSAD']].duplicated()]
  assert pipeline_duplicated.empty