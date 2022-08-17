import logging

import aiohttp

from pyzehndercloud.auth import AbstractAuth

_LOGGER = logging.getLogger(__name__)

API_ENDPOINT = 'https://zehnder-prod-we-apim.azure-api.net/cloud/api/v2.1'
API_KEY = '23d97a1ba1724a0fb750faf3d8a24f95'


class ZehnderCloud:

    def __init__(self, session: aiohttp.ClientSession, auth: AbstractAuth):
        self.session = session
        self._auth = auth

    async def activate_scene(self, building_id: str, scene_id: str):
        """ Activate a scene. """
        result = await self.make_request('PUT', API_ENDPOINT + '/scenes/{building_id}/activate/{scene_id}'.format(
            building_id=building_id,
            scene_id=scene_id
        ))

        return result

    async def get_device_details(self, device_id: str):
        """ Get details of a device including notifications, orders, properties and errors.
        {
          'id': 1336,
          'buildingId': 1337,
          'roomId': None,
          'sapId': None,
          'connectivity': 0,
          'active': True,
          'siteId': 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx:0',
          'description': None,
          'serialNumber': 'SENR00000000',
          'assistantName': None,
          'warrantyStart': None,
          'warrantyEnd': None,
          'registeredVia': 1,
          'partnerFullAccess': False,
          'cloudEnabled': True,
          'serviceNotifications': [],
          'serviceOrders': [],
          'deviceType': {
            'id': 1,
            'name': 'ComfoAir Q',
            'productFamily': 1,
            'connectivity': True,
            'manufacturer': 'NULL',
            'sapMaterialnumber': None,
            'instructions': [],
            'handledDeviceErrors': [],
            'metadata': [],
            'attachments': []
          },
          'properties': [
            {
              'name': 'assistantName',
              'value': 'ComfoAirQ'
            },
            {
              'name': 'time',
              'value': '1660659795'
            },
            {
              'name': 'deviceSerial',
              'value': 'BEA000000000000'
            },
            {
              'name': 'swVersion',
              'value': 'R1.4.0'
            },
            {
              'name': 'articleNr',
              'value': '471502004'
            },
            {
              'name': 'productSerial',
              'value': 'SENR00000000'
            },
            {
              'name': 'remainingFilterDuration',
              'value': '133'
            },
            {
              'name': 'variant',
              'value': '2'
            },
            {
              'name': 'hwVersion',
              'value': '2'
            },
            {
              'name': 'productId',
              'value': '0'
            },
            {
              'name': 'hasComfoSense',
              'value': 'False'
            },
            {
              'name': 'hasComfoSwitch',
              'value': 'False'
            },
            {
              'name': 'hasOptionBox',
              'value': 'False'
            },
            {
              'name': 'hasComfoConnect',
              'value': 'True'
            },
            {
              'name': 'hasComfoCool',
              'value': 'False'
            },
            {
              'name': 'hasKNXGateway',
              'value': 'False'
            },
            {
              'name': 'hasServiceTool',
              'value': 'False'
            },
            {
              'name': 'hasProductionTestTool',
              'value': 'False'
            },
            {
              'name': 'hasDesignVerificationTestTool',
              'value': 'False'
            },
            {
              'name': 'temperatureProfile',
              'value': '0'
            },
            {
              'name': 'ventilationPreset',
              'value': '1'
            },
            {
              'name': 'manualMode',
              'value': 'True'
            },
            {
              'name': 'exhaustFanOff',
              'value': '0'
            },
            {
              'name': 'supplyFanOff',
              'value': '0'
            },
            {
              'name': 'bypassMode',
              'value': '2'
            },
            {
              'name': 'warmProfileTemp',
              'value': '230'
            },
            {
              'name': 'normalProfileTemp',
              'value': '210'
            },
            {
              'name': 'coolProfileTemp',
              'value': '190'
            },
            {
              'name': 'comfortTemperatureMode',
              'value': '0'
            },
            {
              'name': 'boostTimerEnabled',
              'value': 'False'
            },
            {
              'name': 'awayEnabled',
              'value': 'False'
            },
            {
              'name': 'passiveTemperatureMode',
              'value': '0'
            },
            {
              'name': 'limitRMOTCooling',
              'value': '200'
            },
            {
              'name': 'limitRMOTHeating',
              'value': '130'
            }
          ],
          'errors': [],
          'address': {
            'id': 7,
            'street': 'XXX',
            'streetNumber': '123',
            'addressSuffix': None,
            'postcode': '3000',
            'city': 'Leuven',
            'countryIsoCode': 'BEL',
            'longitude': 0,
            'latitude': 0
          }
        }
         """
        result = await self.make_request('GET', API_ENDPOINT + '/devices/byid/{device_id}/details'.format(
            device_id=device_id
        ))

        return result

    async def get_scenes(self):
        """ Get all supported scenes. """
        result = await self.make_request('GET', API_ENDPOINT + '/scenes')

        return result

    async def get_device_state(self, device_id: int):
        """ Get the current state of a device as a list of name-value pairs.
            Works for all devices like Radiators, Comfosys or non-zehnder (external) devices.

            {
              "device_id": 5665749,
              "timestamp": "2022-08-09T10:59:00+00:00",
              "values": {
                "device_id": "SENR00000000",
                "timeSeriesType": 1,
                "exhaustAirTemp": 264,
                "exhaustSpeed": 889,
                "exhaustDuty": 21,
                "systemSupplySpeed": 907,
                "systemSupplyDuty": 23,
                "currentVentilationPower": 9,
                "avoidedCooling": 28,
                "manualMode": false,
                "exhaustFanOff": 0,
                "supplyFanOff": 0,
                "awayEnabled": false,
                "boostTimerEnabled": false,
                "extractAirHumidity": 53,
                "exhaustAirHumidity": 57,
                "systemSupplyTemp": 260,
                "systemSupplyHumidity": 48,
                "systemOutdoorTemp": 264,
                "systemOutdoorHumidity": 48,
                "exhaustFanAirFlow": 73,
                "supplyFanAirFlow": 72,
                "frostDuty": 0,
                "bypassDuty": 0,
                "runningMeanOutdoorTemparature": 216,
                "coolingSeason": true,
                "heatingSeason": false,
                "requiredTemperature": 224,
                "analogInput1": 0,
                "analogInput2": 0,
                "analogInput3": 0,
                "analogInput4": 0,
                "avoidedHeating": 0,
                "postSupplyAirTempAfterComfoCool": 0,
                "exhaustAirTempAfterComfoCool": 0,
                "postHeaterPresence": false,
                "hoodPresence": false,
                "hoodIsOn": false,
                "remainingFilterDuration": 140,
                "limitRMOTCooling": 200,
                "limitRMOTHeating": 130,
                "extractAirTemp": 259,
                "ventilationPreset": 0,
                "comfoCoolCompressorState": 1,
                "comfortTemperatureMode": 0,
                "passiveTemperatureMode": 0,
                "temperatureProfile": 0,
                "ventilationMode": 0,
                "bypassMode": 2,
                "warmProfileTemp": 230,
                "coolProfileTemp": 190,
                "normalProfileTemp": 210
              }
            }
            """
        result = await self.make_request('GET', API_ENDPOINT + '/devices/{device_id}/state'.format(
            device_id=device_id
        ))

        return result

    async def get_devices(self):
        """ Returns a list of device ids of the current customer. """
        result = await self.make_request('GET', API_ENDPOINT + '/devices/ids')

        return result

    async def get_health(self):
        """ Provides an indication about the health of the API. """
        result = await self.make_request('GET', API_ENDPOINT + '/health')

        return result

    async def get_device_history(self, device_id: str, valuename: str, time_from: str, time_to: str,
                                 time_interval: int):
        """ Returns the history of a value from a device. """
        # result = self.make_request('GET', API_ENDPOINT + '/devices/{device_id}/history[?valuename][&from][&to][&interval]')
        raise NotImplementedError()

    async def get_weather_data(self, device_id: str):
        """ Returns current weather data. """
        result = await self.make_request('GET', API_ENDPOINT + '/devices/{device_id}/weather'.format(
            device_id=device_id
        ))

        return result

    async def get_weather_forecast(self, customer_oid: str, language: str):
        """ Returns weather forecast for a customer. """
        # result = await self.make_request('GET', API_ENDPOINT + '/customers/{customer_oid}/weather/forecast[?language]')
        raise NotImplementedError()

    async def get_weather_history(self, device_id: str, valuename: str, time_from: str, time_to: str,
                                  time_interval: int):
        """ Returns the history of a single weather value. """
        # result = await self.make_request('GET', API_ENDPOINT + '/devices/{device_id}/weather/history[?valuename][&from][&to][&interval]')
        raise NotImplementedError()

    async def set_device_settings(self, device_id: str, settings: dict, device_type: str = 'comfosys'):
        """ Set the settings of a Comfo Air Q device.

            device_type can be comfosys or radiator.

            {
              "setVentilationPreset": {
                "value": "Away"
              },
              "setManualMode": {
                "enabled": true
              },
              "setAway": {
                "enabled": true,
                "until": 0
              },
              "setBoostTimer": {
                "seconds": 0
              },
              "setTemperatureProfileTemperature": {
                "mode": "Cool",
                "temperature": 0
              },
              "setTemperatureProfile": {
                "mode": "Cool"
              },
              "setComfortMode": {
                "mode": "Adaptive"
              },
              "setPassiveTemperatureMode": {
                "mode": "Off"
              },
              "setHumidityComfortMode": {
                "mode": "Off"
              },
              "setHumidityProtectionMode": {
                "mode": "Off"
              },
              "setRMOTCool": {
                "temperature": 0
              },
              "setRMOTHeat": {
                "temperature": 0
              },
              "setExhaustFanOff": {
                "seconds": 0
              },
              "setSupplyFanOff": {
                "seconds": 0
              },
              "forceBypass": {
                "seconds": 0
              }
            }
        """
        result = await self.make_request('PUT', API_ENDPOINT + '/devices/{device_id}/{device_type}/settings'.format(
            device_id=device_id,
            device_type=device_type,
        ), settings)

        return result

    async def make_request(self, method: str, endpoint: str, body=None):
        """ Make a request. """
        if body:
            _LOGGER.debug("Sending %s to %s: %s", method, endpoint, body)
        else:
            _LOGGER.debug("Sending %s to %s", method, endpoint)

        headers = {
            "Authorization": "Bearer " + await self._auth.async_get_access_token(),
            "x-api-key": API_KEY,
        }

        async with self.session.request(method, endpoint, headers=headers, json=body) as response:
            _LOGGER.debug("Response status: %s", response.status)
            _LOGGER.debug("Response body: %s", await response.json())

            if response.status == 401:
                message = await response.json()
                raise Exception(message['message'])

            return await response.json()
