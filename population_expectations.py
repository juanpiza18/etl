import great_expectations as gx

context = gx.get_context()
validator = context.sources.pandas_default.read_csv(
  "data/cbsa-est2017-alldata.csv", encoding='ISO-8859-1'
)

# Completeness
validator.expect_column_values_to_not_be_null("CBSA")

#Uniqueness
validator.expect_compound_columns_to_be_unique(['NAME', 'LSAD'])

#Consistency
validator.expect_column_values_to_be_in_set(
  "LSAD",
  [
    "Metropolitan Statistical Area",
    "County or equivalent",
    "Metropolitan Division",
    "Micropolitan Statistical Area"
  ]
)

# Exactness
validator.expect_table_row_count_to_equal(2789)

# Completeness
validator.expect_table_columns_to_match_set([
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
    'POPESTIMATE2017'
  ], exact_match=False
)

#Consistency
validator.expect_column_values_to_be_of_type("CBSA", "int64")
validator.expect_column_values_to_be_of_type("MDIV", "float64")
validator.expect_column_values_to_be_of_type("STCOU", "float64")
validator.expect_column_values_to_be_of_type("NAME", "O")
validator.expect_column_values_to_be_of_type("LSAD", "O")
validator.expect_column_values_to_be_of_type("POPESTIMATE2010", "int64")
validator.expect_column_values_to_be_of_type("POPESTIMATE2011", "int64")
validator.expect_column_values_to_be_of_type("POPESTIMATE2012", "int64")
validator.expect_column_values_to_be_of_type("POPESTIMATE2013", "int64")
validator.expect_column_values_to_be_of_type("POPESTIMATE2014", "int64")
validator.expect_column_values_to_be_of_type("POPESTIMATE2015", "int64")
validator.expect_column_values_to_be_of_type("POPESTIMATE2016", "int64")
validator.expect_column_values_to_be_of_type("POPESTIMATE2017", "int64")

# Validity
validator.expect_column_values_to_be_between("POPESTIMATE2010", 50, 20000000)
validator.save_expectation_suite(discard_failed_expectations=False)

checkpoint = context.add_or_update_checkpoint(
    name="population_checkpoint",
    validator=validator,
)

checkpoint_result = checkpoint.run()

context.open_data_docs()

assert checkpoint_result["success"] is True
