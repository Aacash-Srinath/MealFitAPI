from langchain_ollama import OllamaLLM
from flask import Flask, request, jsonify
import json
import re


ollama = OllamaLLM(model="llama3.2")




app = Flask(__name__)




@app.route('/mealplan', methods=['POST'])
def weekly_meal_plan():

    json_content = request.json
    query = json_content['query']
    print(f"Query: {query}")

    response = ollama.invoke(query)
    parsed_json = {"weekly_meal_plan": response}

    return parsed_json

@app.route('/fitnessplan', methods=['POST'])
def weekly_fitness_plan():

    json_content = request.json
    query = json_content['query']
    print(f"Query: {query}")

    response = ollama.invoke(query)
    parsed_json = {"weekly_fitness_plan": response}

    return parsed_json

