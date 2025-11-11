# Energy Production Planning - FastAPI Project

## Requirements

- Python 3.8 or higher

## Installation

1. **Create and activate a virtual environment**:

    In the terminal, run:

    python -m venv venv

    To activate the virtual environment:

    - **On Windows**:

      .\venv\Scripts\Activate
     

    - **On macOS/Linux**:

      source venv/bin/activate
     

2. **Install dependencies**:

    pip install -r requirements.txt
  

## Usage

### Running the API

To start the API server, use the following command:

uvicorn main:app --host 0.0.0.0 --port 8888



###  Postman

http://127.0.0.1:8888/productionplan

 example :

 {
  "load": 910,
  "fuels":
  {
    "gas(euro/MWh)": 13.4,
    "kerosine(euro/MWh)": 50.8,
    "co2(euro/ton)": 20,
    "wind(%)": 60
  },
  "powerplants": [
    {
      "name": "gasfiredbig1",
      "type": "gasfired",
      "efficiency": 0.53,
      "pmin": 100,
      "pmax": 460
    },
    {
      "name": "gasfiredbig2",
      "type": "gasfired",
      "efficiency": 0.53,
      "pmin": 100,
      "pmax": 460
    },
    {
      "name": "gasfiredsomewhatsmaller",
      "type": "gasfired",
      "efficiency": 0.37,
      "pmin": 40,
      "pmax": 210
    },
    {
      "name": "tj1",
      "type": "turbojet",
      "efficiency": 0.3,
      "pmin": 0,
      "pmax": 16
    },
    {
      "name": "windpark1",
      "type": "windturbine",
      "efficiency": 1,
      "pmin": 0,
      "pmax": 300
    },
    {
      "name": "windpark2",
      "type": "windturbine",
      "efficiency": 1,
      "pmin": 0,
      "pmax": 3600
    }
  ]
}
