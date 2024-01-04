"""Support for Renogy BT-1 devices."""
from __future__ import annotations

from homeassistant.components.bluetooth import BluetoothEntity

def device_key_to_bluetooth_entity_key(device_key):
    """Convert a device key to an entity key."""
    return BluetoothEntity.device_key_to_entity_key(device_key)
