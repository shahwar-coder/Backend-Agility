'''
1️⃣ Parsing Products API Response

A backend service calls the products API and receives the response body as a JSON string.

Question:
Write code to convert the JSON string into a Python object and extract the list of products.
'''

import requests
import json
from typing import List, Dict

def fetch_products(url: str)-> List[Dict]:
    """Fetch Products"""
    try:
        # call api
        response = requests.get(url) # gives you response object != json string
        response.raise_for_status() # http error handling

        # response object as python object
        data = response.json() # directly we have option to get python object here,--- # no need for indirect -> "json.loads(response.text)"

        # validate `data`/response structure
        if not isinstance(data, dict):
            raise ValueError("Invalid response format")
        
        # concerned values `products`
        products = data.get("products")

        if not isinstance(products, list):
            raise ValueError("Products key missing or invalid")
        
        return products
        
    except requests.exceptions.RequestException as err:
        raise RuntimeError(f"API request failed: {err}")
    
    except json.JSONDecodeError as err:
        raise ValueError("Invalid JSON response") from err

def main()->None:
    try:
        products = fetch_products("https://dummyjson.com/products")
        print(f"Total products : {len(products)}")
        print(f"A sample product : {products[0]}")
    except Exception as err:
        print(f"Error: {err}")

if __name__=="__main__":
    main()

# Output:
# Total products : 30
# A sample product : {'id': 1, 'title': 'Essence Mascara Lash Princess', 'description': 'The Essence Mascara Lash Princess is a popular mascara known for its volumizing and lengthening effects. Achieve dramatic lashes with this long-lasting and cruelty-free formula.', 'category': 'beauty', 'price': 9.99, 'discountPercentage': 10.48, 'rating': 2.56, 'stock': 99, 'tags': ['beauty', 'mascara'], 'brand': 'Essence', 'sku': 'BEA-ESS-ESS-001', 'weight': 4, 'dimensions': {'width': 15.14, 'height': 13.08, 'depth': 22.99}, 'warrantyInformation': '1 week warranty', 'shippingInformation': 'Ships in 3-5 business days', 'availabilityStatus': 'In Stock', 'reviews': [{'rating': 3, 'comment': 'Would not recommend!', 'date': '2025-04-30T09:41:02.053Z', 'reviewerName': 'Eleanor Collins', 'reviewerEmail': 'eleanor.collins@x.dummyjson.com'}, {'rating': 4, 'comment': 'Very satisfied!', 'date': '2025-04-30T09:41:02.053Z', 'reviewerName': 'Lucas Gordon', 'reviewerEmail': 'lucas.gordon@x.dummyjson.com'}, {'rating': 5, 'comment': 'Highly impressed!', 'date': '2025-04-30T09:41:02.053Z', 'reviewerName': 'Eleanor Collins', 'reviewerEmail': 'eleanor.collins@x.dummyjson.com'}], 'returnPolicy': 'No return policy', 'minimumOrderQuantity': 48, 'meta': {'createdAt': '2025-04-30T09:41:02.053Z', 'updatedAt': '2025-04-30T09:41:02.053Z', 'barcode': '5784719087687', 'qrCode': 'https://cdn.dummyjson.com/public/qr-code.png'}, 'images': ['https://cdn.dummyjson.com/product-images/beauty/essence-mascara-lash-princess/1.webp'], 'thumbnail': 'https://cdn.dummyjson.com/product-images/beauty/essence-mascara-lash-princess/thumbnail.webp'}


'''
# Key Points (Solution)
- Calls an external Products API using requests.get().
- Uses response.raise_for_status() to handle HTTP errors early.
- Converts JSON response directly into a Python object using response.json().
- Avoids unnecessary json.loads(response.text).
- Validates that the API response is a dictionary.
- Safely extracts the "products" key from the response.
- Ensures "products" is a list before returning.
- Separates API logic, validation, and usage cleanly.

# Key Points (Why This Is Backend-Style)
- Uses proper HTTP error handling (raise_for_status).
- Performs defensive validation on API responses.
- Avoids assuming response structure blindly.
- Returns clean Python data structures for further processing.

# Key Points (Output)
- Output is a Python list of product dictionaries.
- Length reflects total products returned by the API.
- Each product is a dict with rich nested data.
- Example:
  Total products : 30
  Sample product : { ... }

# Important Note
- response.json() is preferred over json.loads(response.text).
- Always validate external API responses in production code.
'''
