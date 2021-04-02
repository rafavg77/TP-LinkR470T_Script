from configparser import ConfigParser
from influxdb import InfluxDBClient
import logging
import os

thisfolder = os.path.dirname(os.path.abspath(__file__))
initfile = os.path.join(thisfolder, 'config/config.ini')
config = ConfigParser()
config.read(initfile)

influx_host = config.get('influx',"influx_host")
influx_port = config.get('influx',"influx_port")
influx_user = config.get('influx','influx_user')
influx_passwd = config.get('influx','influx_pass')
influx_db = config.get('influx','influx_db')

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

class influxClient:
    def saveInfo(self,data):
        clients_data = [
            {
                "measurement" : "internet_clients",
                "tags" : {
                    "host": "automation-pi"
                },
                "fields" : {
                    "clients": data
                }
            }
        ]

        client = InfluxDBClient(influx_host, influx_port, influx_user, influx_passwd, influx_db)
        client.write_points(clients_data)
        logging.info("Data saved to InfluxDB")