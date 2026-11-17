from pathlib import Path
import json
def read_json_booking()->list:
    path = Path(__file__).parent /"bookings.json"
    with open (path,"r") as json_file:
        all_booking = json.load(json_file)
        return all_booking

def write_to_json_booking(all_booking):
    path = Path(__file__).parent /"bookings.json"
    with open(path,"w") as json_file:
        json.dump(all_booking,json_file,indent=2)
        return