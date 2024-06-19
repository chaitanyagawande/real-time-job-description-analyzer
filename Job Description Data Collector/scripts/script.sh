#!/bin/bash

# Kill all processes running on port 3000, 3001, 3002
kill $(lsof -ti:3002) ; kill $(lsof -ti:3001) ; kill $(lsof -ti:3000); kill $(lsof -ti:5000);

# Starting JSON Server for Glassdoor jobs on port 3000
json-server ../data/glassdoor_jobs.json -p 3000 > ../logs/glassdoor.log 2>&1 &

# Starting JSON Server for Remotive jobs on port 3001
json-server ../data/remotive_jobs.json -p 3001 > ../logs/remotive.log 2>&1 &

# Starting JSON Server for LinkedIn job postings on port 3002
json-server ../data/linkedin_job_postings.json -p 3002 > ../logs/linkedin.log 2>&1 &



