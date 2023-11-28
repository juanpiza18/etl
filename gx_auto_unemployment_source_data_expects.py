import great_expectations as gx
import pandas as pd

context = gx.get_context()
'''archivo_xls = pd.ExcelFile('data/Unemployment.xls')
data = archivo_xls.parse('Unemployment Med HH Income')
data.to_csv('data/Unemployment.csv', index=False, encoding='ISO-8859-1')'''

validator = context.sources.pandas_default.read_excel(
    "data/Unemployment.xls",
    skiprows=7
)

print(validator)

datasource_name = "unemployment"
datasource = context.sources.add_pandas(datasource_name)
asset = datasource.add_excel_asset(
    "unemployment",
    "data/Unemployment.xls",
    skiprows=7
)

batch_request = datasource.get_asset("unemployment").build_batch_request()

expectation_suite_name = "unemployment_validation"
context.add_or_update_expectation_suite(expectation_suite_name=expectation_suite_name)

data_assistant_result = context.assistants.onboarding.run(
    batch_request=batch_request
)

expectation_suite = data_assistant_result.get_expectation_suite(
    expectation_suite_name=expectation_suite_name
)

context.add_or_update_expectation_suite(expectation_suite=expectation_suite)

checkpoint = context.add_or_update_checkpoint(
    name=f"yellow_tripdata_sample_{expectation_suite_name}",
    validations=[
        {
            "batch_request": batch_request,
            "expectation_suite_name": expectation_suite_name,
        }
    ],
)
expectation_suite.show_expectations_by_expectation_type()

context.save_expectation_suite(expectation_suite)

checkpoint_result = checkpoint.run()

context.open_data_docs()
