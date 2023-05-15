import os
import time
import logging
from dotenv import load_dotenv
from scraper import scrape_product
from notifier import send_whatsapp_message

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(filename='scraper.log', level=logging.INFO)

# Configure your Twilio credentials
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
from_number = os.getenv('FROM_NUMBER')

# List of phone numbers to which you want to send the message
to_numbers = os.getenv('TO_NUMBERS').split(',')

# List of products to be monitored
products = eval(os.getenv('PRODUCTS'))

while True:
    for product in products:
        try:
            product_price = scrape_product(product['url'])
            if product_price is not None:
                message = "¡{} está disponible en {} y cuesta {}!".format(product['nombre'], product['url'], product_price)
                send_whatsapp_message(account_sid, auth_token, from_number, to_numbers, message)
                logging.info("Mensaje enviado: {}".format(message))
        except Exception as e:
            logging.error("Error: {}".format(e))

    # Wait 12 hours before making the next request
    hours = 3600*12
    logging.info("Proximo escaneo en {} horas".format(hours/3600))
    time.sleep(hours)