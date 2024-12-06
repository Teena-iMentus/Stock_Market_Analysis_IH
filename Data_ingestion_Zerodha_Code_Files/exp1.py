from kiteconnect import KiteConnect

# Initialize KiteConnect with your API key
api_key = "47ts5ou0jd3pldey"
api_secret = "8y6axlm6vowrq3ueg5ze52utj1jjlpx5"
kite = KiteConnect(api_key=api_key)

# Step 1: Get the login URL and follow the login process to obtain a new request token
print("Login URL:", kite.login_url())  # Open this URL, log in, and get the request_token from the redirected URL

# Replace with the new request_token obtained after login
request_token = "ZtWEerQ5zXkYYt6mWqae31CYVI4YawSh"

# Step 2: Use the request_token to generate an access token
try:
    data = kite.generate_session(request_token, api_secret=api_secret)
    access_token = data["access_token"]
    print("Access Token:", access_token)

    # Step 3: Initialize KiteConnect with the access token
    kite.set_access_token(access_token)
except Exception as e:
    print("Error:", e)
