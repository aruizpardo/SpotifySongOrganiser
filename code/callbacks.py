import logging

def close_callback(route, websockets):
    logging.info("Closing...")
    if not websockets:
        exit()