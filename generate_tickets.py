import requests
import json
import time

# Jira credentials and API endpoint
JIRA_BASE_URL = "https://your-jira-instance.atlassian.net"
JIRA_BULK_CREATE_ENDPOINT = f"{JIRA_BASE_URL}/rest/api/2/issue/bulk"
JIRA_AUTH = ("your-email@example.com", "your-api-token")  # Use API token authentication

# Headers for API requests
HEADERS = {
    "Content-Type": "application/json"
}

# List of Jira issues to create
jira_issues = [
    {
        "fields": {
            "project": { "key": "FRONT" },
            "summary": "Login Page UI Test",
            "description": "Verify UI elements on the login page...",
            "issuetype": { "name": "Bug" },
            "priority": { "name": "High" },
            "assignee": { "name": "qa_engineer" },
            "labels": ["frontend", "login", "ui-test"]
        }
    },
    {
        "fields": {
            "project": { "key": "FRONT" },
            "summary": "Add to Cart Functionality",
            "description": "Ensure users can add products to the cart...",
            "issuetype": { "name": "Bug" },
            "priority": { "name": "Critical" },
            "assignee": { "name": "qa_engineer" },
            "labels": ["frontend", "cart", "ui-test"]
        }
    },
    {
        "fields": {
            "project": { "key": "FRONT" },
            "summary": "Search Bar Testing",
            "description": "Validate the search functionality...",
            "issuetype": { "name": "Bug" },
            "priority": { "name": "Medium" },
            "assignee": { "name": "qa_engineer" },
            "labels": ["frontend", "search", "ui-test"]
        }
    },
    {
        "fields": {
            "project": { "key": "FRONT" },
            "summary": "Checkout Process Validation",
            "description": "Ensure checkout process flows smoothly...",
            "issuetype": { "name": "Bug" },
            "priority": { "name": "High" },
            "assignee": { "name": "qa_engineer" },
            "labels": ["frontend", "checkout", "ui-test"]
        }
    },
    {
        "fields": {
            "project": { "key": "FRONT" },
            "summary": "Product Image Gallery",
            "description": "Test the image carousel on product pages...",
            "issuetype": { "name": "Bug" },
            "priority": { "name": "Medium" },
            "assignee": { "name": "qa_engineer" },
            "labels": ["frontend", "product", "ui-test"]
        }
    },
    {
        "fields": {
            "project": { "key": "FRONT" },
            "summary": "Promo Code Application",
            "description": "Ensure promo codes apply correctly...",
            "issuetype": { "name": "Bug" },
            "priority": { "name": "High" },
            "assignee": { "name": "qa_engineer" },
            "labels": ["frontend", "checkout", "promo"]
        }
    },
    {
        "fields": {
            "project": { "key": "FRONT" },
            "summary": "Payment Gateway Testing",
            "description": "Ensure payment transactions process correctly...",
            "issuetype": { "name": "Bug" },
            "priority": { "name": "Critical" },
            "assignee": { "name": "qa_lead" },
            "labels": ["frontend", "payment", "gateway"]
        }
    },
    {
        "fields": {
            "project": { "key": "FRONT" },
            "summary": "Mobile Responsiveness Test",
            "description": "Ensure website layout adapts properly on mobile...",
            "issuetype": { "name": "Bug" },
            "priority": { "name": "High" },
            "assignee": { "name": "qa_engineer" },
            "labels": ["frontend", "mobile", "ui-test"]
        }
    },
    {
        "fields": {
            "project": { "key": "FRONT" },
            "summary": "Wishlist Functionality",
            "description": "Ensure users can add and remove items from the wishlist...",
            "issuetype": { "name": "Bug" },
            "priority": { "name": "Medium" },
            "assignee": { "name": "qa_engineer" },
            "labels": ["frontend", "wishlist", "ui-test"]
        }
    },
    {
        "fields": {
            "project": { "key": "FRONT" },
            "summary": "Logout Feature",
            "description": "Ensure users can log out and clear session properly...",
            "issuetype": { "name": "Bug" },
            "priority": { "name": "Low" },
            "assignee": { "name": "qa_engineer" },
            "labels": ["frontend", "logout", "ui-test"]
        }
    }
]

# Send request to Jira API to create tickets
response = requests.post(JIRA_BULK_CREATE_ENDPOINT, auth=JIRA_AUTH, headers=HEADERS, data=json.dumps({"issueUpdates": jira_issues}))

if response.status_code == 201:
    issues = response.json().get("issues", [])
    print("Jira tickets created successfully!")
    
    # Extract issue keys
    issue_keys = [issue["key"] for issue in issues]
    
    # Comments for each issue
    issue_comments = {
        "FRONT-101": ["Let's double-check the login button on mobile screens.", "Test on Safari and Edge."],
        "FRONT-102": ["Check if cart persists in incognito mode.", "What happens with out-of-stock items?"],
        "FRONT-103": ["Does 'lap' return 'laptop' in search?", "Test handling of special characters."],
        "FRONT-104": ["Check lag between cart and checkout.", "Empty cart error message should be clear."],
        "FRONT-105": ["Ensure swipe functionality works on mobile.", "Check zoom feature on all images."],
        "FRONT-106": ["What happens if users try multiple promo codes?", "Check discount application delay."],
        "FRONT-107": ["Payment failures reported with test cards—verify Stripe logs.", "Add test case for expired cards."],
        "FRONT-108": ["Navbar overlaps on Android—verify fix.", "Test in both portrait and landscape modes."],
        "FRONT-109": ["Does wishlist persist after logout?", "Check notification when adding an item."],
        "FRONT-110": ["Ensure session cookies are cleared on logout.", "Check behavior when back button is pressed."]
    }

    # Add comments to each ticket
    for issue_key in issue_keys:
        for comment in issue_comments.get(issue_key, []):
            comment_payload = {"body": comment}
            comment_url = f"{JIRA_BASE_URL}/rest/api/2/issue/{issue_key}/comment"
            requests.post(comment_url, auth=JIRA_AUTH, headers=HEADERS, data=json.dumps(comment_payload))
            time.sleep(1)  # Avoid hitting Jira rate limits
    
    print("Comments added successfully!")
else:
    print(f"Error creating Jira tickets: {response.status_code} - {response.text}")
