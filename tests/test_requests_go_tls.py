import sys
import os

# Add the parent directory to the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

from curlformat.requests_go import parse

# Test curl command
curl_command = 'curl -X GET "https://api.example.com" -H "Authorization: Bearer token" -H "Content-Type: application/json"'

# Parse the curl command
result = parse(curl_command)

# Print the result
print("\nGenerated requests-go code with TLS configuration:")
print("----------------------------------------------------")
print(result)
