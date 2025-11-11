import requests

# API endpoint
url = "https://jsonplaceholder.typicode.com/users"

try:
    response = requests.get(url)
    response.raise_for_status()  # Raises error for bad responses (like 404 or 500)

    users = response.json()

    if not users:
        print("No users found.")
    else:
        count = 1
        for user in users:
            name = user.get("name")
            username = user.get("username")
            email = user.get("email")
            city = user.get("address", {}).get("city")

            # (Bonus) Only print users whose city starts with 'S'
            if city and city.startswith("S"):
                print(f"User {count}:")
                print(f"Name: {name}")
                print(f"Username: {username}")
                print(f"Email: {email}")
                print(f"City: {city}")
                print("-" * 25)
                count += 1

except requests.exceptions.RequestException as e:
    print("Error fetching data:", e)
