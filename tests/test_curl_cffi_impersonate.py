import sys
import os

# Add the parent directory to the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

from curlformat.curl_cffi import parse, parse_async

# Test curl command
curl_command = 'curl -X GET "https://api.example.com" -H "Authorization: Bearer token" -H "Content-Type: application/json"'

# Parse the curl command for synchronous code
sync_result = parse(curl_command)

# Parse the curl command for asynchronous code
async_result = parse_async(curl_command)

# Print the results
print("\nGenerated curl_cffi code with random browser impersonation (Sync):")
print("----------------------------------------------------")
print(sync_result)

print("\n\nGenerated curl_cffi code with random browser impersonation (Async):")
print("----------------------------------------------------")
print(async_result)
