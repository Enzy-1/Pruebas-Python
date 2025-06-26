from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#--------------------------------------------------------------

@app.get("/")
def read_root():
    return {"mensaje": "¡Hola desde FastAPI!"}

#--------------------------------------------------------------

@app.get("/saludo/{nombre}")
def saludar(nombre: str):
    return {"saludo": f"Hola, {nombre}!"}

#--------------------------------------------------------------

@app.post("/enviar/{dato}")
def recibir_dato(dato: str):
    return {"respuesta": f"Me has enviado: {dato}"}

#--------------------------------------------------------------

class Persona(BaseModel):
    nombre: str
    cedula: str

@app.post("/registrar")
def registrar_persona(persona: Persona):
    return {
        "nombre_recibido": persona.nombre,
        "cedula_recibida": persona.cedula
    }
    
#--------------------------------------------------------------
    
class Number(BaseModel):
    numero1: int
    numero2: int
    numero3: int
    numero4: int
    numero5: int

@app.post("/calculo")
def numeros(number: Number):
    lista_numeros = [
        number.numero1,
        number.numero2,
        number.numero3,
        number.numero4,
        number.numero5,
    ]

    mayor = max(lista_numeros)
    menor = min(lista_numeros)
    promedio = sum(lista_numeros) / len(lista_numeros)
    orden_ascendente = sorted(lista_numeros)


    return {
        "Numero Mayor es": mayor,
        "Numero Menor es": menor,
        "Promedio de numeros es": promedio,
        "Numeros ordenados": orden_ascendente

    }