import requests
from bs4 import BeautifulSoup

def scrape_product(product_url):
    # Make an HTTP GET request to the web page
    response = requests.get(product_url)

    # Analyze web page HTML with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the element containing the product availability information
    product_price = soup.find('strong', {'id': 'product-price'}).text.replace(" ", "")
    i_elements = soup.find_all('i', {'class': "fa fa-check", 'style': "color:#7ED321"})

    # additional function
    """ with open('element.txt', 'w', encoding='utf-8') as file:
            file.write(i_element.prettify()) """
    available_store = []

    # Check if the product is available
    if i_elements is not None:
        for i in i_elements:
            span_element =  i.find_next_sibling('span', {'class': "product-container-inner"})
            if span_element is not None:
                available_store.append(span_element.text)
        if 'Cali Cañasgordas' in available_store:
            return product_price
    return None