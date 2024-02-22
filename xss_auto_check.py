import requests
from bs4 import BeautifulSoup

# Define the URL to test
url = 'http://example.com'

# Define the payloads that will be tested
payloads = ["'", '"', '<', '>', '&', 'javascript:', 'onerror=']

# Define the headers to simulate a real user
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

# Function to test for XSS vulnerabilities
def test_xss(url, payloads):
    # Send a GET request to the URL
    response = requests.get(url, headers=headers)
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    # Find all input fields
    inputs = soup.find_all('input')
    # Find all textarea fields
    textareas = soup.find_all('textarea')
    # Combine all fields
    all_fields = inputs + textareas

    # Loop through all fields and test each payload
    for field in all_fields:
        field_name = field.get('name')
        for payload in payloads:
            # Prepare the data to be sent
            data = {field_name: payload}
            # Send the request with the payload
            response = requests.post(url, data=data, headers=headers)
            # Check the response for signs of XSS vulnerability
            if payload in response.content:
                print(f"Potential XSS vulnerability found with payload: {payload} in field: {field_name}")
                # Optionally, you can print the response content for further analysis
                # print(response.content)

# Run the XSS test
test_xss(url, payloads)
