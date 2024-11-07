import os
import requests

# Replace with your GitHub personal access token
ACCESS_TOKEN = os.getenv("GITHUB_ACCESS_TOKEN")

# Source repository URL (where issues are exported from)
SOURCE_URL = "https://api.github.com/repos/Linesmerrill/police-cad/issues"

# Target repository URL (where new issues are created)
TARGET_URL = "https://api.github.com/repos/Lines-Police-CAD/police-cad/issues"

headers = {"Authorization": f"token {ACCESS_TOKEN}"}


def get_issues(url):
    """
    Fetches issues data from the provided GitHub API URL.
    """
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Raise an exception for non-200 status codes
    return response.json()


def create_issue(title, body, labels):
    """
    Creates a new issue in the target repository.
    """
    issue = {'title': title, 'body': body, 'labels': labels}
    response = requests.post(TARGET_URL, json=issue, headers=headers)
    response.raise_for_status()  # Raise an exception for non-200 status codes
    return response.json()

# Example usage
issues = get_issues(SOURCE_URL)
for issue in issues:
    title = issue['title']
    body = issue['body']
    labels = issue.get('labels', [])
    create_issue(title, body, labels)