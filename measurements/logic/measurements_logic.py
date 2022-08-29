from ..models import Measurement

def get_measurements():
    measurements = Measurement.objects.all()
    return measurements

def get_measurement(meas_pk):
    measurement = Measurement.objects.get(pk=meas_pk)
    return measurement

def update_measurement(meas_pk:int, new_meas)-> Measurement:
    measurement = get_measurement(meas_pk)
    measurement.variable = new_meas["variable"]
    measurement.value = new_meas["value"]
    measurement.place = new_meas["place"]
    measurement.unit = new_meas["unit"]
    measurement.dateTime = new_meas["dateTime"]
    measurement.save()
    return measurement

def create_measurement(meas)-> Measurement:
    measurement = Measurement(
        variable=meas["variable"],
        value=meas["value"],
        place=meas["place"],
        unit=meas["unit"],
        dateTime=meas["dateTime"])
    measurement.save()
    return measurement

def delete_measurement(meas_pk:int):
    measurement = get_measurement(pk=meas_pk)
    measurement.delete()
    
    return measurement
