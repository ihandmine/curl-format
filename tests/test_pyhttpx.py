from curlformat.pyhttpx.api import parse

# Test curl command
curl_command = 'curl -X GET "https://api.example.com/data" -H "Authorization: Bearer token"'

# Test pyhttpx parser
with open('pyhttpx_output.txt', 'w') as f:
    f.write(parse(curl_command))

print("Output written to file.")
