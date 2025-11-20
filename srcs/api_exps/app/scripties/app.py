from fastapi import FastAPI
import requests

app = FastAPI()

CATALOG_URL = "https://learn.microsoft.com/api/catalog/"


@app.get("/")
def root():
    return {"message": "Hello from FastAPI"}


@app.get("/courses")
def get_courses(limit: int = 10):
    """
    Return a list of courses (modules) with extracted 'skills'.
    'skills' here = roles + products for that module.
    """
    resp = requests.get(CATALOG_URL, timeout=10)
    resp.raise_for_status()
    data = resp.json()

    # The catalog returns top-level "modules", not "items"
    modules = data.get("modules", [])

    results = []
    for m in modules[:limit]:
        skills = []

        # roles / products may be missing or null, so be safe
        roles = m.get("roles") or []
        products = m.get("products") or []

        if isinstance(roles, list):
            skills.extend(roles)
        if isinstance(products, list):
            skills.extend(products)

        skills = list(set(skills))  # remove duplicates

        results.append({
            "course_title": m.get("title"),
            "course_url": m.get("url"),
            "skills": skills,
            "all": m
        })

    return {
        "count": len(results),
        "courses":results
}