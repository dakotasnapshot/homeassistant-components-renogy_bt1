"""Config flow for Renogy BT-1 integration."""
from __future__ import annotations

from homeassistant import config_entries
from homeassistant.const import CONF_NAME
import voluptuous as vol

from .const import DOMAIN

class RenogyBt1ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Renogy BT-1."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        if user_input is not None:
            # Handle user input and create/configure the integration
            return self.async_create_entry(title=user_input[CONF_NAME], data={})

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required(CONF_NAME): str,
            }),
        )
