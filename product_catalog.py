from product_data import products
# TODO: Step 1 - Print out the products to see the data that you are working with.

print(products[:3])

# TODO: Step 2 - Create a list called customer_preferences and store the user preference in this list.

customer_preferences = []

response = ""
while response != "N":
    print("Input a preference:")
    preference = input()
    # Add the customer preference to the list

    response = input("Do you want to add another preference? (Y/N): ").upper()
  

# TODO: Step 3 - Convert customer_preferences list to set to eliminate duplicates.

customer_preferences = set(customer_preferences)

# TODO: Step 4 - Convert the product tags to sets in order to allow for faster comparisons.
converted_products = []

converted_products = []

for product in products:
    product_copy = product.copy()
    product_copy["tags"] = set(product["tags"])
    converted_products.append(product_copy)



# TODO: Step 5 - Write a function to calculate the number of matching tags

def count_matches(product_tags, customer_tags):
    '''
    Args:
        product_tags (set): A set of tags associated with a product.
        customer_tags (set): A set of tags associated with the customer.
    Returns:
        int: The number of matching tags between the product and customer.
    '''
    return len(product_tags & customer_tags)




# TODO: Step 6 - Write a function that loops over all products and returns a sorted list of matches

def recommend_products(products, customer_tags):
    '''
    Args:
        products (list): A list of product dictionaries.
        customer_tags (set): A set of tags associated with the customer.
    Returns:
        list: A list of products containing product names and their match counts.
    '''
    recommendations = []
    for product in products:
        score = count_matches(product["tags"], customer_tags)
        if score > 0:
            recommendations.append({"name": product["name"], "score": score})

    recommendations.sort(key=lambda p: p["score"], reverse=True)
    return recommendations



# TODO: Step 7 - Call your function and print the results

recommendations = recommend_products(converted_products, customer_preferences)
for rec in recommendations:
    print(f"{rec['name']} - matches: {rec['score']}")


# DESIGN MEMO (write below in a comment):
# 1. What core operations did you use (e.g., intersections, loops)? Why?
#    I used set intersections (&) in count_matches() to compare product tags against
#    customer preferences, since set lookups/intersections are faster than checking
#    membership across lists. I used loops to convert product tags to sets and to
#    build the recommendation list with each product's score.

# 2. How might this code change if you had 1000+ products?
#    Looping through every product on each call is O(n), which gets slower as the
#    catalog grows. With 1000+ products, I'd build an index mapping each tag to the
#    list of products that have it, so I could look up only the relevant products
#    for a customer's preferences instead of scanning the whole catalog each time.