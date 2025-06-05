# Databricks notebook source
import requests
import pandas as pd

url = " https://run.mocky.io/v3/0ff9b004-fb7a-4d8a-9c95-43f96080d0e6"
response = requests.get(url)
data = response.json()
df = pd.DataFrame(data)
df.to_csv("data.csv")