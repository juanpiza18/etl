import great_expectations as gx

from great_expectations.checkpoint import Checkpoint

context = gx.get_context()

my_connection_string = "sqlite:///./db.sqlite"
datasource_name = "my_datasource"

datasource = context.sources.add_sqlite(
    name=datasource_name, connection_string=my_connection_string
)

datasource.add_table_asset(
    name="population", table_name="population"
)

batch_request = datasource.get_asset("population").build_batch_request()

expectation_suite_name = "population_validation"
context.add_or_update_expectation_suite(expectation_suite_name=expectation_suite_name)
validator = context.get_validator(
    batch_request=batch_request,
    expectation_suite_name=expectation_suite_name,
)

print(validator.head())

#Completeness
validator.expect_column_values_to_not_be_null(column="NAME")

#Consistency
validator.expect_column_values_to_be_of_type(column="POPULATION_EST", type_="INTEGER")

# Uniqueness
validator.expect_column_unique_value_count_to_be_between(column="CBSA", max_value=0)

# Validity / Exactness
validator.expect_column_values_to_be_between(
    column="YEAR", min_value=2010, max_value=2017
)


validator.save_expectation_suite(discard_failed_expectations=False)

my_checkpoint_name = "my_sql_checkpoint"

checkpoint = Checkpoint(
    name=my_checkpoint_name,
    run_name_template="%Y%m%d-%H%M%S-my-run-name-template",
    data_context=context,
    batch_request=batch_request,
    expectation_suite_name=expectation_suite_name,
    action_list=[
        {
            "name": "store_validation_result",
            "action": {"class_name": "StoreValidationResultAction"},
        },
        {"name": "update_data_docs", "action": {"class_name": "UpdateDataDocsAction"}},
    ],
)

context.add_or_update_checkpoint(checkpoint=checkpoint)

checkpoint_result = checkpoint.run()

context.open_data_docs()
