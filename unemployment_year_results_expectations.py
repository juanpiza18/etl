import great_expectations as gx

context = gx.get_context()

validator = context.sources.pandas_default.read_csv(
    "data/unemployment_year_results.csv", encoding='ISO-8859-1'
)


validator.expect_column_to_exist(column='Postal_code')

validator.expect_column_values_to_be_between("Postal_code", 1.0, 72.0)

validator.expect_column_values_to_be_of_type('Postal_code', 'float64')

validator.expect_column_values_to_be_in_set('Postal_code', [1.0, 2.0, 4.0, 5.0, 6.0, 8.0, 9.0,
                                                            12.0, 10.0, 11.0, 13.0, 14.0, 15.0, 16.0,
                                                            17.0, 18.0, 19.0, 20.0, 21.0, 22.0, 23.0, 24.0, 25.0, 26.0,
                                                            27.0, 28.0, 29.0, 30.0, 31.0, 32.0, 33.0, 34.0, 35.0, 36.0,
                                                            37.0, 38.0, 39.0, 40.0, 41.0, 42.0, 43.0, 44.0, 45.0, 46.0,
                                                            47.0, 48.0, 49.0, 50.0, 51.0, 53.0, 54.0, 55.0, 56.0, 72.0])

validator.save_expectation_suite(discard_failed_expectations=False)

checkpoint = context.add_or_update_checkpoint(
    name="unemployment_checkpoint",
    validator=validator,
)

checkpoint_result = checkpoint.run()

context.open_data_docs()

assert checkpoint_result["success"] is True
