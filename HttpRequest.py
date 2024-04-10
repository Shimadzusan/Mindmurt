import requests

class HttpRequest:
    # Constructor to initialize the object with name and age
    def __init__(self):
        print("..created object httpRequest")
        self.makeRequest()

    # Method to display information about the person
    def makeRequest(self):
        # print(f"Name: {self.name}, Age: {self.age}")
        print("makeRequest")
        # Make a GET request to google.com
        response = requests.get("https://www.avito.ru/moskva/kvartiry/prodam-ASgBAgICAUSSA8YQ?localPriority=0")

        # Check if the request was successful
        if response.status_code == 200:
            print("Request to google.com was successful!")
            # Print the content of the response
            print(response.text)
        else:
            print(f"Failed to retrieve data from google.com. Status code: {response.status_code}")
