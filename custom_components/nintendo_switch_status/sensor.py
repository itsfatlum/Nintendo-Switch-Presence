# custom_components/nintendo_switch_status/sensor.py
from homeassistant.components.sensor import SensorEntity
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from homeassistant.helpers.device_registry import DeviceInfo
from .const import DOMAIN
from typing import Any

async def async_setup_entry(hass, entry, async_add_entities):
    coordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_entities(
        [
            NintendoSwitchOnlineSensor(coordinator),
            NintendoSwitchGameSensor(coordinator),
            NintendoSwitchGameImageSensor(coordinator),
            NintendoSwitchProfileNameSensor(coordinator),
            NintendoSwitchProfileImageSensor(coordinator),
            NintendoSwitchAccountIdSensor(coordinator),
            NintendoSwitchTotalPlaytimeSensor(coordinator),
        ],
        True,
    )

class BaseNintendoSwitchSensor(CoordinatorEntity, SensorEntity):
    has_entity_name = True

    def __init__(self, coordinator):
        super().__init__(coordinator)

    @property
    def device_info(self) -> DeviceInfo:
        friend = self.coordinator.data.get("friend", {})
        return DeviceInfo(
            identifiers={(DOMAIN, friend.get("nsaId"))},
            name="Nintendo Switch",
            manufacturer="Nintendo",
            model="Switch",
        )

class NintendoSwitchOnlineSensor(BaseNintendoSwitchSensor):
    _attr_unique_id = "nintendo_switch_status_online"
    _attr_name = "Online Status"

    @property
    def native_value(self) -> Any:
        return self.coordinator.data.get("friend", {}).get("presence", {}).get("state")

class NintendoSwitchGameSensor(BaseNintendoSwitchSensor):
    _attr_unique_id = "nintendo_switch_status_game"
    _attr_name = "Current Game"

    @property
    def native_value(self) -> Any:
        presence = self.coordinator.data.get("friend", {}).get("presence", {})
        game = presence.get("game") if presence else None
        return game.get("name") if game else None

class NintendoSwitchGameImageSensor(BaseNintendoSwitchSensor):
    _attr_unique_id = "nintendo_switch_status_game_image"
    _attr_name = "Game Image URL"

    @property
    def native_value(self) -> Any:
        presence = self.coordinator.data.get("friend", {}).get("presence", {})
        game = presence.get("game") if presence else None
        return game.get("imageUri") if game else None

class NintendoSwitchProfileNameSensor(BaseNintendoSwitchSensor):
    _attr_unique_id = "nintendo_switch_status_profile_name"
    _attr_name = "Profile Name"

    @property
    def native_value(self) -> Any:
        return self.coordinator.data.get("friend", {}).get("name")

class NintendoSwitchProfileImageSensor(BaseNintendoSwitchSensor):
    _attr_unique_id = "nintendo_switch_status_profile_image"
    _attr_name = "Profile Image URL"

    @property
    def native_value(self) -> Any:
        return self.coordinator.data.get("friend", {}).get("imageUri")

class NintendoSwitchAccountIdSensor(BaseNintendoSwitchSensor):
    _attr_unique_id = "nintendo_switch_status_account_id"
    _attr_name = "Account ID"

    @property
    def native_value(self) -> Any:
        return self.coordinator.data.get("friend", {}).get("id")

class NintendoSwitchTotalPlaytimeSensor(BaseNintendoSwitchSensor):
    _attr_unique_id = "nintendo_switch_status_total_playtime"
    _attr_name = "Total Playtime"

    # Assuming API value is in minutes; we expose minutes as the main state
    @property
    def native_value(self) -> Any:
        presence = self.coordinator.data.get("friend", {}).get("presence", {})
        game = presence.get("game") if presence else None
        if not game:
            return None
        return game.get("totalPlayTime")

    @property
    def native_unit_of_measurement(self) -> str:
        return "min"

    @property
    def extra_state_attributes(self) -> dict:
        """Add helper attribute with hours (float, rounded)."""
        minutes = self.native_value
        try:
            if minutes is None:
                return {}
            hours = round(minutes / 60, 2)
            return {"hours": hours}
        except Exception:
            return {}