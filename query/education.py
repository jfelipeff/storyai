from fastapi import FastAPI
import os
from google.cloud import bigquery
app = FastAPI() 

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '../bigquery-service-account.json'

@app.get("/query/education")
def get_data():
    

# Construct a BigQuery client object.
    client = bigquery.Client()
    
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
    query_job = client.query(query)  # Make an API request.

    print("The query data:")
    for row in query_job:
        # Row values can be accessed by field name or index.
        print("name={}, count={}".format(row[0], row[1]))

