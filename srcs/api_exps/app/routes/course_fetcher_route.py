from flask import Blueprint, jsonify
from srcs.api_exps.app.scripties.course_fetcher import fetch_courses

courses_bp = Blueprint("courses", __name__)

@courses_bp.route("/courses")
def courses():
    limit = 10  # or get from request.args
    data = fetch_courses(limit)
    return jsonify(data)
