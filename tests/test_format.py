print("=== Old Format ===")
print("""requests.get("https://api.example.com",
    headers={
    "Authorization": "Bearer token",
    "Content-Type": "application/json"
},
    cookies={},
    auth=(),
)""")

print("\n=== New Format ===")
print("""import requests

# Make request using requests
response = requests.get(
    url="https://api.example.com",
    headers={
        "Authorization": "Bearer token",
        "Content-Type": "application/json"
    }
)

# Print response information
print(f"Status Code: {response.status_code}")
print(f"Headers: {response.headers}")
print("Response Body:")
print(response.text)
""")
