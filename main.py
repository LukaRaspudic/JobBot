import requests
from openpyxl import Workbook

def search_indeed_jobs(keywords, location):
    url = "https://api.indeed.com/ads/apisearch"
    params = {
        "q": " OR ".join(keywords),
        "l": location,
        "limit": 50  # Adjust as needed
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch jobs from Indeed: {e}")
        return None

def create_excel_file(jobs, filename):
    wb = Workbook()
    ws = wb.active
    ws.append(["Job Title", "Company", "Job URL"])

    for job in jobs:
        title = job.get('jobtitle', 'N/A')
        company = job.get('company', 'N/A')
        job_url = job.get('url', 'N/A')

        ws.append([title, company, job_url])

    wb.save(filename)
    print(f"Excel file '{filename}' created successfully!")

def main():
    keywords = ["excel", "python"]
    location = "Melbourne, Australia"

    indeed_jobs = search_indeed_jobs(keywords, location)
    if indeed_jobs:
        create_excel_file(indeed_jobs["results"], "indeed_job_listings.xlsx")

if __name__ == "__main__":
    main()
