from curlformat import parse

# Test curl command
curl_command = 'curl -X GET "https://api.example.com" -H "Authorization: Bearer token" -H "Content-Type: application/json"'

# Test requests parser
print("=== Requests Output ===")
print(parse(curl_command))
