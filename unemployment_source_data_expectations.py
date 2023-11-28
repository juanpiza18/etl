import great_expectations as gx

context = gx.get_context()
validator = context.sources.pandas_default.read_excel(
    "data/Unemployment.xls",
    skiprows=7
)

# Completeness
validator.expect_column_values_to_not_be_null("FIPStxt")
validator.expect_column_values_to_not_be_null("State")
validator.expect_column_values_to_not_be_null("Area_name")
'''validator.expect_column_values_to_not_be_null("Unemployment_rate_2000")
validator.expect_column_values_to_not_be_null("Unemployment_rate_2001")
validator.expect_column_values_to_not_be_null("Unemployment_rate_2002")
validator.expect_column_values_to_not_be_null("Unemployment_rate_2003")
validator.expect_column_values_to_not_be_null("Unemployment_rate_2004")
validator.expect_column_values_to_not_be_null("Unemployment_rate_2005")
validator.expect_column_values_to_not_be_null("Unemployment_rate_2006")
validator.expect_column_values_to_not_be_null("Unemployment_rate_2007")
validator.expect_column_values_to_not_be_null("Unemployment_rate_2008")
validator.expect_column_values_to_not_be_null("Unemployment_rate_2009")
validator.expect_column_values_to_not_be_null("Unemployment_rate_2010")
validator.expect_column_values_to_not_be_null("Unemployment_rate_2011")
validator.expect_column_values_to_not_be_null("Unemployment_rate_2012")
validator.expect_column_values_to_not_be_null("Unemployment_rate_2013")
validator.expect_column_values_to_not_be_null("Unemployment_rate_2014")
validator.expect_column_values_to_not_be_null("Unemployment_rate_2015")
validator.expect_column_values_to_not_be_null("Unemployment_rate_2016")
validator.expect_column_values_to_not_be_null("Unemployment_rate_2017")
validator.expect_column_values_to_not_be_null("Unemployment_rate_2018")
validator.expect_column_values_to_not_be_null("Unemployment_rate_2019")'''

# Uniqueness
validator.expect_compound_columns_to_be_unique(['FIPStxt', 'State'])

# Consistency
validator.expect_column_values_to_be_in_set(
    "State",
    [
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
    ]
)

# Exactness
validator.expect_table_row_count_to_equal(3275)

# Completeness
validator.expect_table_columns_to_match_set([
"FIPStxt",
"State",
"Area_name",
"Unemployment_rate_2000",
"Unemployment_rate_2001",
"Unemployment_rate_2002",
"Unemployment_rate_2003",
"Unemployment_rate_2004",
"Unemployment_rate_2005",
"Unemployment_rate_2006",
"Unemployment_rate_2007",
"Unemployment_rate_2008",
"Unemployment_rate_2009",
"Unemployment_rate_2010",
"Unemployment_rate_2011",
"Unemployment_rate_2012",
"Unemployment_rate_2013",
"Unemployment_rate_2014",
"Unemployment_rate_2015",
"Unemployment_rate_2016",
"Unemployment_rate_2017",
"Unemployment_rate_2018",
"Unemployment_rate_2019",
], exact_match=False
)

# Consistency
validator.expect_column_values_to_be_of_type("FIPStxt", "int64")
validator.expect_column_values_to_be_of_type("State", "str")
validator.expect_column_values_to_be_of_type("Area_name", "str")
validator.expect_column_values_to_be_of_type("Unemployment_rate_2000", "float64")
validator.expect_column_values_to_be_of_type("Unemployment_rate_2001", "float64")
validator.expect_column_values_to_be_of_type("Unemployment_rate_2002", "float64")
validator.expect_column_values_to_be_of_type("Unemployment_rate_2003", "float64")
validator.expect_column_values_to_be_of_type("Unemployment_rate_2004", "float64")
validator.expect_column_values_to_be_of_type("Unemployment_rate_2005", "float64")
validator.expect_column_values_to_be_of_type("Unemployment_rate_2006", "float64")
validator.expect_column_values_to_be_of_type("Unemployment_rate_2007", "float64")
validator.expect_column_values_to_be_of_type("Unemployment_rate_2008", "float64")
validator.expect_column_values_to_be_of_type("Unemployment_rate_2009", "float64")
validator.expect_column_values_to_be_of_type("Unemployment_rate_2010", "float64")
validator.expect_column_values_to_be_of_type("Unemployment_rate_2011", "float64")
validator.expect_column_values_to_be_of_type("Unemployment_rate_2012", "float64")
validator.expect_column_values_to_be_of_type("Unemployment_rate_2013", "float64")
validator.expect_column_values_to_be_of_type("Unemployment_rate_2014", "float64")
validator.expect_column_values_to_be_of_type("Unemployment_rate_2015", "float64")
validator.expect_column_values_to_be_of_type("Unemployment_rate_2016", "float64")
validator.expect_column_values_to_be_of_type("Unemployment_rate_2017", "float64")
validator.expect_column_values_to_be_of_type("Unemployment_rate_2018", "float64")
validator.expect_column_values_to_be_of_type("Unemployment_rate_2019", "float64")


# Validity
validator.expect_column_values_to_be_between(
    "Unemployment_rate_2019", min_value=0.7, max_value=19.3, mostly=0.95
)
validator.expect_column_median_to_be_between(
    "Unemployment_rate_2019", min_value=3.7, max_value=3.7, result_format="SUMMARY"
)

validator.save_expectation_suite(discard_failed_expectations=False)

checkpoint = context.add_or_update_checkpoint(
    name="unemployment_checkpoint",
    validator=validator,
)

checkpoint_result = checkpoint.run()

context.open_data_docs()

assert checkpoint_result["success"] is True
