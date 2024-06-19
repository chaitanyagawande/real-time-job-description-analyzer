from pyspark.sql.types import StringType
from bs4 import BeautifulSoup
from pyspark.sql.functions import udf
from cohere_llm_model import get_job_details_with_rate_limit

def clean_html(html_content):
    if html_content is not None:
        soup = BeautifulSoup(html_content, "html.parser")
        return soup.get_text(separator=" ", strip=True)
    return None
    
def get_cleaned_html():
    clean_html_udf = udf(clean_html, StringType())
    return clean_html_udf

def get_job_details_udf():
    get_job_details_udf = udf(lambda job_desc: get_job_details_with_rate_limit(job_desc), StringType())
    return get_job_details_udf