import os
import os.path
import json

defaulttracepath = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))), "NeuralRacingV1", "data")
tracepath = os.getenv('TRACES_PATH', defaulttracepath)

def clearTraces():
	
	files = os.listdir(tracepath)
	tracefiles = [f for f in files if f.startswith("traces") and f.endswith(".json")]
	for t in tracefiles:
		os.remove(tracepath + "/" + t)

def saveTraces(cars, generation=0):
	traces = []
	for car in cars:
		traces.append(car.traces)
	f = open(tracepath + "/traces"+str(generation)+".json", "w")
	json.dump(traces, f)
	f.close()
