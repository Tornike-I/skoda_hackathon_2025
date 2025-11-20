from srcs.api_exps.app.mock_data import mock_data
def get_top_jobs(employee_id, emp_skills, job_skills):
    # Find employee skills
    employee_data = next((e for e in emp_skills if employee_id in e), None)
    if not employee_data:
        return f"Employee ID {employee_id} not found."

    skills = set(employee_data[employee_id])
    matches = []

    # Compare employee skills to each job
    for job in job_skills:
        job_name = list(job.keys())[0]
        job_skill_list = set(job[job_name])

        have = skills.intersection(job_skill_list)
        dont_have = job_skill_list - skills
        match_count = len(have)
        total_required = len(job_skill_list)
        match_percentage = f"{match_count}/{total_required}"

        matches.append({
            "job": job_name,
            "match": match_percentage,
            "have": list(have),
            "dont have": list(dont_have)
        })

    # Sort by number of matched skills descending, choose top 5
    top_jobs = sorted(matches, key=lambda x: int(x["match"].split("/")[0]), reverse=True)[:5]

    return top_jobs

if __name__ == '__main__':

    # Extract variables
    skills = mock_data.get("skills", [])
    job_positions = mock_data.get("job_positions", [])
    job_skills = mock_data.get("job_skills", [])
    emp_skills = mock_data.get("employee_skills", [])

    print(get_top_jobs("EMP002", emp_skills, job_skills))
