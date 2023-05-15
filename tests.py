import os
import unittest
from scraper import scrape_product
from notifier import send_whatsapp_message
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class TestScraper(unittest.TestCase):
    def test_scrape_product(self):
        product_url = 'https://www.pricesmart.com/site/co/es/pagina-producto/454448'
        product_price = scrape_product(product_url)
        self.assertIsNotNone(product_price)

class TestNotifier(unittest.TestCase):
    def test_send_whatsapp_message(self):
        account_sid = os.getenv('TWILIO_ACCOUNT_SID')
        auth_token = os.getenv('TWILIO_AUTH_TOKEN')
        from_number = os.getenv('FROM_NUMBER')
        to_numbers = os.getenv('TO_NUMBERS').split(',')
        message = 'Test message'
        send_whatsapp_message(account_sid, auth_token, from_number, to_numbers, message)

if __name__ == '__main__':
    unittest.main()