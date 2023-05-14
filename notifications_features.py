import os
import requests
from bs4 import BeautifulSoup
import time
from twilio.rest import Client
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure your Twilio credentials
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)

# List of phone numbers to which you want to send the message
phone_numbers = ['whatsapp:+573105450929', 'whatsapp:+573106186669']

# List of products to be monitored
products = [
    {'nombre': 'Huggies Toallitas Húmedas Ultra Confort 8 Paquetes / 80 Unidades', 'url': 'https://www.pricesmart.com/site/co/es/pagina-producto/454448'},
    {'nombre': 'Similac 2 Prosensitive Formula Infantil Etapa 2, 6 Unidades / 350 g', 'url': 'https://www.pricesmart.com/site/co/es/pagina-producto/345293'},
    {'nombre': 'Member´s Selection Lavaloza Líquido Biodegradable 3 L / 101.4 oz', 'url': 'https://www.pricesmart.com/site/co/es/pagina-producto/322046'},
]

while True:
    for product in products:
        # Make an HTTP GET request to the web page
        response = requests.get(product['url'])

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
                for numero in phone_numbers:
                    # Send a WhatsApp message using Twilio
                    message = client.messages \
                    .create(
                        body="¡{} está disponible en {} y cuesta {}!".format(product['nombre'], product['url'], product_price),
                        from_='whatsapp:+14155238886',
                        to=numero
                        )

                    print(message.price)
                    print(message.price_unit)
                    print(message.to)
                    print(message.body)
                    print('--------------------------------------------------------')
                    time.sleep(2)

    # Wait 12 hours before making the next request
    hours = 3600*12
    print("Proximo escaneo en {} horas".format(hours/3600))
    time.sleep(hours)
    