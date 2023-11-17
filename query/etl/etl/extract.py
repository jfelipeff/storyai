import pandas_gbq
from google.oauth2 import service_account


# This module is in charge of making the request to the BigQuery dataset 
# and retrieving the data to be used in the different endpoints.


# Here we get the credentials of the bigquery throug a service account. For more information
# about service accounts: https://cloud.google.com/iam/docs/service-account-overview
credentials = service_account.Credentials.from_service_account_file('../bigquery-service-account.json')

# Get data from BigQuery
def get_data(query: str) -> object:
    # Construct a BigQuery client object.

    query = """
    SELECT
    country_name,
    AVG(value) AS average
    FROM
    `bigquery-public-data.world_bank_intl_education.international_education`
    WHERE
    indicator_code = "SE.XPD.TOTL.GB.ZS"
    AND year > 2000
    GROUP BY
    country_name
    ORDER BY
    average DESC
    """

    df = pandas_gbq.read_gbq(query, credentials=credentials) 

    return df

