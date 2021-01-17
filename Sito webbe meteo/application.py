import os
import csv
from flask import Flask, flash, jsonify, redirect, render_template, request, session, send_from_directory


# Configure application
app = Flask(__name__)



@app.route("/")
def index():
    #Recupera dati da file e inviali allla pagina
    with open('DATA.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                temp=row[0]
                umidità=row[1]
                dir_vento=row[2]
                
    return render_template("RT_Meteo.html",tmp=temp,hum=umidità,vento_dir=dir_vento)
   
