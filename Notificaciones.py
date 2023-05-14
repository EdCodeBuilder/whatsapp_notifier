import requests
from bs4 import BeautifulSoup
import time
from twilio.rest import Client

# Configura tus credenciales de Twilio
account_sid = 'AC5bebb364e72a0f06956bc17636241f44'
auth_token = 'e5bacc7cf94893d34bf4774121616b52'
client = Client(account_sid, auth_token)

# URL de la página web que deseas monitorear
url = 'https://www.pricesmart.com/site/co/es/pagina-producto/345293'

while True:
    # Realiza una solicitud HTTP GET a la página web
    response = requests.get(url)

    # Analiza el HTML de la página web con BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Encuentra el elemento que contiene la información de disponibilidad del producto
    # i_element = soup.find('i', {'class': 'fa fa-times'})
    span_element = soup.find('span', {'class': 'product-container-inner'})

    # Verifica si el producto está disponible
    #if i_element['style'] == 'color: #7ed321;' and span_element.text == 'Cali Cañasgordas':
    if span_element.text == 'Cali Cañasgordas':
        # Envía un mensaje por WhatsApp usando Twilio
        message = client.messages \
                        .create(
                            body="¡Similac 2 2100g está disponible!",
                            from_='whatsapp:+14155238886',
                            to='whatsapp:+573105450929'
                        )

        print(message.sid)

    # Espera 2 horas antes de realizar la siguiente consulta
    time.sleep(7200)