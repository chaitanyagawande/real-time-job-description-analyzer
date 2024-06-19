import cohere
import re
import json
import time

co = cohere.Client('CLIENT_API_KEY')

prompt = """
We need your expertise to streamline our job details extraction process! You'll receive job descriptions and your task is to distill essential information into a structured JSON format for database storage. Your output should include crucial details such as required skills, salary range, years of experience, education prerequisites, and other pertinent information commonly found in job postings. Required Output: You're expected to generate a JSON object adhering to the following format: { 'skills': ['Java', 'Python', 'C++'], 'salary': '200k-250k' } Details to Extract: Skills: Extract all technical and soft skills mentioned in the job description. Salary: Identify the salary range specified in the posting. Years of Experience: Provide the number of years of experience required. Education Required: Specify the degree type required (e.g., Bachelor's, Master's). Major Required: Array of any specific majors or disciplines required for the role (e.g. ['Computer Science', 'Computer Engineering']). Note: Please refrain from including any additional commentary or general text in your response. Don't put repeated skills in skills section. Degree type must be either of (Bachelors, Masters, PhD)Focus solely on providing the JSON object according to the specified format. If you don't find any information about a particular field, simply omit it from the JSON object.

Input Description :
"""

def get_job_details(job_description):
    input_prompt = prompt + job_description

    response = co.generate(
        prompt= input_prompt,
    )

    input_text = response[0].text

    pattern = r'\{[^{}]+\}'

    match = re.search(pattern, input_text)

    if match:
        json_object = match.group()
        try:
            parsed_json = json.loads(json_object)
            json_object = json.dumps(parsed_json, indent=2)
            return json_object
        except json.JSONDecodeError as e:
            print("Error decoding JSON:", e)
            return ""
    else:
        print("No JSON object found in the input text.")
        return ""

def get_job_details_with_rate_limit(job_description):
    print("Sleeping for 12 seconds to avoid rate limit...")
    time.sleep(12)
    return get_job_details(job_description)
