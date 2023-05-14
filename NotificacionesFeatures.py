import requests
from bs4 import BeautifulSoup
import time
from twilio.rest import Client

# Configura tus credenciales de Twilio
account_sid = 'AC5bebb364e72a0f06956bc17636241f44'
auth_token = 'e5bacc7cf94893d34bf4774121616b52'
client = Client(account_sid, auth_token)

# Lista de números de teléfono a los que deseas enviar el mensaje
numeros = ['whatsapp:+573105450929', 'whatsapp:+573106186669']

# Lista de productos que deseas monitorear
productos = [
    {'nombre': 'Huggies Toallitas Húmedas Ultra Confort 8 Paquetes / 80 Unidades', 'url': 'https://www.pricesmart.com/site/co/es/pagina-producto/454448'},
    {'nombre': 'Similac 2 Prosensitive Formula Infantil Etapa 2, 6 Unidades / 350 g', 'url': 'https://www.pricesmart.com/site/co/es/pagina-producto/345293'},
    {'nombre': 'Member´s Selection Lavaloza Líquido Biodegradable 3 L / 101.4 oz', 'url': 'https://www.pricesmart.com/site/co/es/pagina-producto/322046'},
]

while True:
    for producto in productos:
        # Realiza una solicitud HTTP GET a la página web
        response = requests.get(producto['url'])

        # Analiza el HTML de la página web con BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Encuentra el elemento que contiene la información de disponibilidad del producto
        product_price = soup.find('strong', {'id': 'product-price'})
        i_elements = soup.find('i', {'class': 'fa fa-check','style': 'color:#7ED321'}).find('span', {'class': 'product-container-inner'})
        span_elements = i_elements.find('span', {'class': 'product-container-inner'})
        # span_elements = i_elements.find_all('span').text
        # for i_element in i_elements:
            # span_elements.append(i_elements.find_all('span').text)

        # Verifica si el producto está disponible
        if i_elements is not None and span_elements.text == 'Cali Cañasgordas':
        # if i_elements is not None and i_elements['style'] == 'color: #7ED321;' and span_elements.text == 'Cali Cañasgordas':
        # if span_elements.text == producto['nombre']:
            for numero in numeros:
                # Envía un mensaje por WhatsApp usando Twilio
                message = client.messages \
                                .create(
                                    body="¡{} está disponible en {} y cuesta {}!".format(producto['nombre'], producto['url'], product_price.text.replace(" ", "")),
                                    from_='whatsapp:+14155238886',
                                    to=numero
                                )

                print(message.sid)
                print(message.body)
                print('--------------------------------------------------------')
        time.sleep(2)

    # Espera 2 horas antes de realizar la siguiente consulta
    time.sleep(7200)
    