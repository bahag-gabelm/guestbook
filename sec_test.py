# standard python packages
import os
import requests
import logging
import json
import time
import math

# pip packages
from google.cloud import secretmanager
import google.cloud.logging
from cryptography.hazmat.primitives.serialization import load_pem_private_key
import jwt


def delete_file(filename):
    os.remove(filename)
    print(f"File '{filename}' has been deleted.")


def main():
    filename = input("Enter a filename to delete: ")
    delete_file(filename)


if __name__ == "__main__":
    main()
