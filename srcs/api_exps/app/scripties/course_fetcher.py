import requests

CATALOG_URL = "https://learn.microsoft.com/api/catalog/"

def fetch_courses(limit: int = 10):
    """
    Fetch courses from Microsoft Learn catalog and extract skills.
    Returns a dict similar to the FastAPI response.
    """
    try:
        resp = requests.get(CATALOG_URL, timeout=10)
        resp.raise_for_status()
        data = resp.json()
    except requests.RequestException as e:
        # Handle network errors gracefully
        return {"count": 0, "courses": [], "error": str(e)}

    modules = data.get("modules", [])
    results = []

    for m in modules[:limit]:
        skills = []

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
            "summary": m.get("summary")
        })

    return {
        "count": len(results),
        "courses": results
    }
