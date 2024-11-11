import logging
import os

def do_env(all:bool) -> None:
    logging.info(f"Env Command all: {all}")
    logging.info(f"Environment Variables: {os.environ}")