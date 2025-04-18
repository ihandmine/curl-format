import sys
import os

# Add the parent directory to the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

from curlformat.requests.generator import generate_requests_code
from curlformat.common.parser import parse_context

# Test curl command
curl_command = 'curl -X GET "https://api.example.com" -H "Authorization: Bearer token" -H "Content-Type: application/json"'

# Parse the curl command
parsed_context = parse_context(curl_command)

# Generate the code
result = generate_requests_code(parsed_context)

# Print the result
print(result)
