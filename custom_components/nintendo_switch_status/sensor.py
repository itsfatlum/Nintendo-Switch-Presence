from homeassistant.components.sensor import SensorEntity
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from homeassistant.helpers.device_registry import DeviceInfo
from .const import DOMAIN

async def async_setup_entry(hass, entry, async_add_entities):
    coordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_entities([
        NintendoSwitchOnlineSensor(coordinator),
        NintendoSwitchGameSensor(coordinator),
        NintendoSwitchGameImageSensor(coordinator),
    ])

class BaseNintendoSwitchSensor(CoordinatorEntity, SensorEntity):
    has_entity_name = True

    def __init__(self, coordinator):
        super().__init__(coordinator)

    @property
    def device_info(self):
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
    def native_value(self):
        return self.coordinator.data["friend"]["presence"]["state"]

class NintendoSwitchGameSensor(BaseNintendoSwitchSensor):
    _attr_unique_id = "nintendo_switch_status_game"
    _attr_name = "Current Game"

    @property
    def native_value(self):
        presence = self.coordinator.data["friend"]["presence"]
        game = presence.get("game")
        return game["name"] if game else "None"

class NintendoSwitchGameImageSensor(BaseNintendoSwitchSensor):
    _attr_unique_id = "nintendo_switch_status_game_image"
    _attr_name = "Game Image URL"

    @property
    def native_value(self):
        presence = self.coordinator.data["friend"]["presence"]
        game = presence.get("game")
        return game["imageUri"] if game else None