import requests
import csv
from bs4 import BeautifulSoup
import sqlite3

# Create SQLite connection and cursor
con = sqlite3.connect('jobs.db')
cursor = con.cursor()

cursor.execute('DROP TABLE IF EXISTS jobs')

# Create Jobs Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS jobs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    company TEXT,
    location TEXT,
    description TEXT,
    application_link TEXT,
    UNIQUE(title, company, location)
)
""")

# Function to scrape the job listings
def scrape_jobs():
    url = 'https://realpython.github.io/fake-jobs/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    jobs = []
    job_elements = soup.find_all('div', class_='card-content')
    for job_element in job_elements:
        title = job_element.find('h2', class_='title').text.strip()
        company = job_element.find('h3', class_='company').text.strip()
        location = job_element.find('p', class_='location').text.strip()
        description = job_element.find('div', class_='content').text.strip()
        application_link = job_element.find('a')['href']
        # Append as a tuple instead of a formatted string
        jobs.append((title, company, location, description, application_link))
    return jobs

# Function to perform incremental loading of job data into the SQLite database
def store_jobs(jobs):
    for job in jobs:
        title, company, location, description, application_link = job
        cursor.execute("""
        INSERT INTO jobs (title, company, location, description, application_link)
        VALUES (?, ?, ?, ?, ?)
        ON CONFLICT(title, company, location)
        DO UPDATE SET description = excluded.description, application_link = excluded.application_link
        """, (title, company, location, description, application_link))
    con.commit()

# Function to filter jobs by location or company and export to CSV (without pandas)
def export_filtered_jobs(location=None, company=None, filename='filtered_jobs.csv'):
    query = "SELECT * FROM jobs WHERE 1=1"
    params = []

    if location:
        query += ' AND location = ?'
        params.append(location)

    if company:
        query += ' AND company = ?'
        params.append(company)

    cursor.execute(query, params)
    jobs = cursor.fetchall()

    with open(filename, mode="w", newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['ID', 'Job Title', 'Company', 'Location', 'Description', 'Application Link'])
        # Write each job row by row
        for job in jobs:
            writer.writerow(job)
    
    print(f"Filtered jobs inserted to {filename}")

if __name__ == '__main__':
    job_listings = scrape_jobs()
    store_jobs(job_listings)
    export_filtered_jobs(location='Remote', filename='remote_jobs.csv')

# Close connection after done
con.close()
