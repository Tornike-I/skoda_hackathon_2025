import json
from srcs.api_exps.app.scripties.suggestor import get_top_jobs
# Load JSON file
with open("mock_database.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Extract variables
skills = data.get("skills", [])
job_positions = data.get("job_positions", [])
job_skills = data.get("job_skills", [])
emp_skills = data.get("employee_skills", [])



print(get_top_jobs("EMP006", emp_skills, job_skills))