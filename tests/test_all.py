from curlformat import parse as parse_requests
try:
    from curlformat import parse_httpx
    httpx_available = True
except ImportError:
    httpx_available = False

try:
    from curlformat import parse_aiohttp
    aiohttp_available = True
except ImportError:
    aiohttp_available = False

try:
    from curlformat import parse_pycurl
    pycurl_available = True
except ImportError:
    pycurl_available = False

try:
    from curlformat import parse_pyhttpx
    pyhttpx_available = True
except ImportError:
    pyhttpx_available = False

try:
    from curlformat import parse_curl_cffi, parse_curl_cffi_async
    curl_cffi_available = True
except ImportError:
    curl_cffi_available = False

# Test curl command
curl_command = 'curl -X GET "https://api.example.com/data" -H "Authorization: Bearer token"'

# Test requests parser
print("=== Requests Output ===")
print(parse_requests(curl_command))
print("\n")

# Test httpx parser if available
if httpx_available:
    print("=== HTTPX Output ===")
    print(parse_httpx(curl_command))
    print("\n")
else:
    print("HTTPX not available")
    print("\n")

# Test aiohttp parser if available
if aiohttp_available:
    print("=== AIOHTTP Output ===")
    print(parse_aiohttp(curl_command))
    print("\n")
else:
    print("AIOHTTP not available")
    print("\n")

# Test pycurl parser if available
if pycurl_available:
    print("=== PycURL Output ===")
    print(parse_pycurl(curl_command))
    print("\n")
else:
    print("PycURL not available")
    print("\n")

# Test pyhttpx parser if available
if pyhttpx_available:
    print("=== PyHTTPX Output ===")
    print(parse_pyhttpx(curl_command))
    print("\n")
else:
    print("PyHTTPX not available")
    print("\n")

# Test curl_cffi parser if available
if curl_cffi_available:
    print("=== curl_cffi Sync Output ===")
    print(parse_curl_cffi(curl_command))
    print("\n")
    print("=== curl_cffi Async Output ===")
    print(parse_curl_cffi_async(curl_command))
    print("\n")
else:
    print("curl_cffi not available")
    print("\n")
