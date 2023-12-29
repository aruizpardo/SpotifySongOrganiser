import logging
import sys

# Establecer el formato de los mensajes de registro
handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logging.getLogger().addHandler(handler)

def message(level:str, text:str) -> None:
    logging.log(getattr(logging, level.upper(), 10), text)
