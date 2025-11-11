# main.py
from fastapi import FastAPI, HTTPException # fast api: to create a web app framework, httpexception: to control errors
from pydantic import BaseModel #convert JSON data
import logging # save information



app = FastAPI() #create the work environment first 
logging.basicConfig(level=logging.INFO) # show message from information level

# Fuel data
class Fuels(BaseModel):
    gas: float
    kerosine: float
    co2: float
    wind: float
# Energy data
class PowerPlant(BaseModel):
    name: str
    type: str
    efficiency: float
    pmin: float
    pmax: float
# The “Payload” class defines the structure of the data we receive in the body of the request.
# It is a model that includes the “load”, “fuels” and “powerplants”
class Payload(BaseModel):
    load: float
    fuels: dict
    powerplants: list

#path for the post
@app.post("/productionplan")
def production_plan(payload: Payload):
    #extract the input data
    try:
        load = payload.load
        fuels = payload.fuels
        plants = payload.powerplants
# list to store the results
        results = []

        # Calculate cost and actual available power
        enriched = []
        for p in plants:
            plant = dict(p)
            if p["type"] == "windturbine":
                plant["cost"] = 0 # no fuel cost
                plant["pmax"] = p["pmax"] * fuels["wind(%)"] / 100 #pmax depending on the wind
            elif p["type"] == "gasfired":
                plant["cost"] = fuels["gas(euro/MWh)"] / p["efficiency"] # fuel cost based on efficiency
            elif p["type"] == "turbojet":
                plant["cost"] = fuels["kerosine(euro/MWh)"] / p["efficiency"]
            enriched.append(plant)

       # Sort by cheapest to most expensive
        enriched.sort(key=lambda x: x["cost"])

        remaining = load  # initial variable with the total load to be covered
        for p in enriched: # use every plant on the list we have
            produce = min(p["pmax"], remaining) # we collect the value that each plant can cover (the minimum between the maximum and remaining) so that the plant does not generate more than it can
            if produce < p["pmin"]: # if min is greater than produce, p = 0 
                produce = 0
            results.append({"name": p["name"], "p": round(produce, 1)}) # save results
            remaining -= produce # reduce the load used until it reaches 0
            if remaining <= 0:
                break

       # Fill in with zeros if there are extra plants.
        for p in enriched[len(results):]:
            results.append({"name": p["name"], "p": 0.0})

        return results

    except Exception as e:
        logging.error(f"Error procesando plan: {e}")
        raise HTTPException(status_code=500, detail=str(e))
