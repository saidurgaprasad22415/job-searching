import smtplib
import os
import requests
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime

# --- CONFIGURATION ---
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 585
SENDER_EMAIL = "avuladurgasaiprasad1777@gmail.com"
# We read the password from environment variables for security
SENDER_PASSWORD = os.environ.get("GMAIL_APP_PASSWORD") 
RECEIVER_EMAIL = "avuladurgasaiprasad1777@gmail.com"

def fetch_jobs():
    """
    Fetches entry-level jobs. For reliability, you can use a free job API 
    or a scraped RSS feed standard for your target keywords.
    """
    # Sample setup using an open job API (e.g., JSearch or Jooble via RapidAPI, or Github Jobs alternatives)
    # For a simple fallback, we can use open-source job aggregator feeds
    search_queries = [
        "Cloud Computing Entry Level", 
        "Data Analytics Fresher", 
        "Government Technical Jobs India",
        "MNC Software Trainee"
    ]
    
    # Placeholder structured results structure
    job_results = []
    
    # Mocking fetching structure (In production, replace with real API endpoints or requests)
    # Using an API key from SerpAPI (Google Jobs API) is highly recommended for accuracy.
    job_results.append({
        "title": "Cloud Operations Associate (Fresher)",
        "company": "Top MNC / Startup Ecosystem",
        "location": "Remote / India",
        "link": "https://www.linkedin.com/jobs"
    })
    job_results.append({
        "title": "Data Analyst Trainee",
        "company": "Tech Startup",
        "location": "Bangalore",
        "link": "https://www.naukri.com"
    })
    
    return job_results

def build_email_content(jobs):
    date_str = datetime.now().strftime("%Y-%m-%d")
    html = f"""
    <html>
    <body>
        <h2>Daily Job Alerts - {date_str}</h2>
        <p>Here are the latest entry-level openings in Cloud, Data Analytics, MNCs, and Startups:</p>
        <table border="1" cellpadding="5" style="border-collapse: collapse;">
            <tr style="background-color: #f2f2f2;">
                <th>Job Title</th>
                <th>Company</th>
                <th>Location</th>
                <th>Apply Link</th>
            </tr>
    """
    for job in jobs:
        html += f"""
            <tr>
                <td><b>{job['title']}</b></td>
                <td>{job['company']}</td>
                <td>{job['location']}</td>
                <td><a href="{job['link']}">View Job</a></td>
            </tr>
        """
    html += "</table></body></html>"
    return html

def send_email(content):
    msg = MIMEMultipart("alternative")
    msg["Subject"] = f"Daily Job Openings Alert - {datetime.now().strftime('%d %b %Y')}"
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECEIVER_EMAIL
    
    msg.attach(MIMEText(content, "html"))
    
    try:
        server = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())
        server.close()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

if __name__ == "__main__":
    jobs_list = fetch_jobs()
    email_body = build_email_content(jobs_list)
    send_email(email_body)