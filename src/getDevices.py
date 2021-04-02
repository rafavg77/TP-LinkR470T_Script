from Utils.tplinkScript import FirewallApi
from Utils.saveInflux import influxClient
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

#Se obtienen la cantidad de dispositivos desde el Firewall
fw = FirewallApi()
devices = fw.getArpDevices()
logging.info(devices)

#Se procede a guardar la información de dispositivos en InfluxDB
client = influxClient()
client.saveInfo(devices)