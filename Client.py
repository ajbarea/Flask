import requests


def fetch_data(url):
    try:
        response = requests.get(url, timeout=10)  # HTTP GET with a timeout
        response.raise_for_status()  # Raise an HTTPError for bad responses
        return response.json()  # Return the response as JSON
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None


url = "http://localhost:8000/hi"  # API 'endpoint'
data = fetch_data(url)

if data:
    print(data)  # Output the response as JSON
else:
    print("Failed to fetch data.")
