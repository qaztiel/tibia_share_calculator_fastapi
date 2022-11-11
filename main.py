from fastapi import FastAPI
from tibiasharecalculator import TibiaShareCalculator

app = FastAPI()
calc = TibiaShareCalculator()

@app.get("/")
async def root():
    return {"message": "Hello"}


@app.get("/level/{level}")
async def calc_level(level):
    
    results = calc.calc_range(int(level))
    
    return {
        "min": results['min_level'],
        "max": results['max_level']
    }
