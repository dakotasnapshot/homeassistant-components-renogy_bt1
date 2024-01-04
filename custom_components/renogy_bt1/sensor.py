"""Support for Renogy BT-1 sensors."""
from __future__ import annotations

from homeassistant.components.sensor import SensorEntity, PLATFORM_SCHEMA
from homeassistant.const import DEVICE_CLASS_VOLTAGE, DEVICE_CLASS_SIGNAL_STRENGTH, PERCENTAGE, VOLT, DECIBELS_MILLIWATT
from homeassistant.core import callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers import config_validation as cv

from .const import DOMAIN

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({})

SENSOR_DESCRIPTIONS = {
    "total_energy": {"device_class": None, "unit_of_measurement": "kWh"},
    "battery_charging_power": {"device_class": None, "unit_of_measurement": "W"},
    "battery_charging_voltage": {"device_class": DEVICE_CLASS_VOLTAGE, "unit_of_measurement": VOLT},
    
}

async def async_setup_platform(hass, config, async_add_entities: AddEntitiesCallback, discovery_info=None):
    """Set up the Renogy BT-1 sensors."""
    entities = []
    # Create sensors based on SENSOR_DESCRIPTIONS
    for sensor_key, sensor_info in SENSOR_DESCRIPTIONS.items():
        entities.append(RenogyBt1Sensor(sensor_key, sensor_info))
    async_add_entities(entities)

class RenogyBt1Sensor(SensorEntity):
    """Representation of a Renogy BT-1 sensor."""

    def __init__(self, sensor_key, sensor_info):
        """Initialize the sensor."""
        self._sensor_key = sensor_key
        self._sensor_info = sensor_info
        self._state = None

    @property
    def unique_id(self):
        """Return a unique ID."""
        return f"{DOMAIN}_{self._sensor_key}"

    @property
    def name(self):
        """Return the name of the sensor."""
        return f"Renogy BT-1 {self._sensor_key.replace('_', ' ').title()}"

    @property
    def device_class(self):
        """Return the device class."""
        return self._sensor_info["device_class"]

    @property
    def unit_of_measurement(self):
        """Return the unit of measurement."""
        return self._sensor_info["unit_of_measurement"]

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @callback
    def update_data(self, data):
        """Update sensor data."""
        self._state = data.get(self._sensor_key)
        self.async_write_ha_state()
