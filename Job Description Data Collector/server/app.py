from threading import Thread
from flask import Flask, jsonify
from service.linkedin_api_processing import process_linkedin_jobs
from service.remotive_api_processing import process_remotive_jobs
from service.glassdoor_api_processing import process_glassdoor_jobs

app = Flask(__name__)

@app.route('/api/linkedin-jobs', methods=['POST'])
def push_linkedin_jobs_to_kafka():
    thread = Thread(target=process_linkedin_jobs)
    thread.start()
    return jsonify({"status": 201, "message": "LinkedIn Jobs Processing Started!"}), 201

@app.route('/api/remotive-jobs', methods=['POST'])
def push_remotive_jobs_to_kafka():
    thread = Thread(target=process_remotive_jobs)
    thread.start()
    return jsonify({"status": 201, "message": "Remotive Jobs Processing Started!"}), 201

@app.route('/api/glassdoor-jobs', methods=['POST'])
def push_glassdoor_jobs_to_kafka():
    thread = Thread(target=process_glassdoor_jobs)
    thread.start()
    return jsonify({"status": 201, "message": "Glassdoor Jobs Processing Started!"}), 201

if __name__ == '__main__':
    app.run(debug=True)