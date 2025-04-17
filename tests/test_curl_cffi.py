from curlformat.curl_cffi.api import parse, parse_async

# Test curl command
curl_command = 'curl -X GET "https://api.example.com/data" -H "Authorization: Bearer token"'

# Test curl_cffi sync parser
with open('curl_cffi_sync_output.txt', 'w') as f:
    f.write(parse(curl_command))

# Test curl_cffi async parser
with open('curl_cffi_async_output.txt', 'w') as f:
    f.write(parse_async(curl_command))

print("Output written to files.")
