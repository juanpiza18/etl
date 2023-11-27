import great_expectations as gx

from great_expectations.checkpoint import Checkpoint

context = gx.get_context()

my_connection_string = "sqlite:///./db.sqlite"
datasource_name = "my_datasource"

datasource = context.sources.add_sqlite(
    name=datasource_name, connection_string=my_connection_string
)

datasource.add_table_asset(
    name="unemployment", table_name="unemployment"
)

batch_request = datasource.get_asset("unemployment").build_batch_request()

expectation_suite_name = "unemployment_validation"
context.add_or_update_expectation_suite(expectation_suite_name=expectation_suite_name)
validator = context.get_validator(
    batch_request=batch_request,
    expectation_suite_name=expectation_suite_name,
)

print(validator.head())

# Completeness
validator.expect_column_values_to_not_be_null(column="FIPStxt")
validator.expect_column_values_to_not_be_null(column="State")
validator.expect_column_values_to_not_be_null(column="Area_name")
validator.expect_column_values_to_not_be_null(column="Year")
validator.expect_table_columns_to_match_set([
    "FIPStxt",
    "State",
    "Area_name",
    "Year",
    "unemployment_rate",
], exact_match=True
)

# Consistency
validator.expect_column_values_to_be_of_type(column="FIPStxt", type_="INTEGER")
validator.expect_column_values_to_be_of_type(column="State", type_="TEXT")
validator.expect_column_values_to_be_of_type(column="Area_name", type_="TEXT")
validator.expect_column_values_to_be_of_type(column="Year", type_="INTEGER")
validator.expect_column_values_to_be_of_type(column="unemployment_rate", type_="REAL")

# Uniqueness
validator.expect_column_unique_value_count_to_be_between(column="FIPStxt", min_value=0, max_value=72153)

# Consistency
validator.expect_column_values_to_be_in_set(
    "State",
    {
        "US",
        "AL",
        "AK",
        "AZ",
        "AR",
        "CA",
        "Co",
        "CO",
        "CT",
        "DE",
        "DC",
        "FL",
        "GA",
        "HI",
        "ID",
        "IL",
        "IN",
        "IA",
        "KS",
        "KY",
        "LA",
        "ME",
        "MD",
        "MA",
        "MI",
        "MN",
        "MS",
        "MO",
        "MT",
        "NE",
        "NV",
        "NH",
        "NJ",
        "NM",
        "NY",
        "NC",
        "ND",
        "OH",
        "OK",
        "OR",
        "PA",
        "RI",
        "SC",
        "SD",
        "TN",
        "TX",
        "UT",
        "VT",
        "VA",
        "WA",
        "WV",
        "WI",
        "WY",
        "PR",
        "WN"
    }
)

# Validity / Exactness
validator.expect_column_values_to_be_between(
    column="Year", min_value=2000, max_value=2019
)
validator.expect_column_values_to_be_between(column="FIPStxt", min_value=0, max_value=72153)

validator.expect_table_row_count_to_equal(101525)

# Save expectation Suite
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
