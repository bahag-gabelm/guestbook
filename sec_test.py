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


def read_secret():
    secret = "my_hardcoded_secret"
    print(f"The secret is: {secret}")


def delete_file(filename):
    os.remove(filename)
    print(f"File '{filename}' has been deleted.")


def main():
    filename = input("Enter a filename to delete: ")
    delete_file(filename)
    read_secret()


if __name__ == "__main__":
    main()
