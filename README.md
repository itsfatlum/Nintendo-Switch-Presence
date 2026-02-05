# Nintendo Switch Presence

![HACS Default](https://img.shields.io/badge/HACS-Default-brightgreen) ![Release Version](https://img.shields.io/github/v/release/itsfatlum/Nintendo-Switch-Presence) ![GitHub stars](https://img.shields.io/github/stars/itsfatlum/Nintendo-Switch-Presence?style=flat) ![Downloads](https://img.shields.io/github/downloads/itsfatlum/Nintendo-Switch-Presence/latest?style=flat)

**Brief description**  
Nintendo Switch Presence is a small Home Assistant custom integration that uses an NXAPI presence URL to show your Switch presence and activity (online status, current game, playtime, profile, images, platform, etc.).

---

## Prerequisites ✅
Before getting started, make sure you have the following:

- **Discord Account** - Required to join the nxapi support server and access the registration service
- **Home Assistant** - Ensure it's a supported version for custom integrations
- **HACS** (optional) - Makes installation easier, or you can manually access `config/custom_components`
- **Nintendo Switch Account** - The account you want to track presence for
- **nxapi-auth Account** - Register at https://nxapi-auth.fancy.org.uk (requires Discord server membership)

---

## Quick Start
1. Join the support [Discord](https://discord.com/invite/4D82rFkXRv) and register at https://nxapi-auth.fancy.org.uk.
2. Add your Switch account on the nxapi site and copy your presence URL.
3. In Home Assistant go to **Settings → Devices & Services → Add Integration → Nintendo Switch Presence**, paste the presence URL and finish setup.

---

## Register with nxapi-auth (required)
1. Join the support Discord server: https://discord.com/invite/4D82rFkXRv
   > **Important:** This service is only available to members of this server. If you leave the server you may be removed from the presence server.
2. Register at https://nxapi-auth.fancy.org.uk, add your Nintendo Switch account, then copy the presence URL.
3. Make sure you are **sharing your presence** with the user you added during setup (Friend Settings).
   - If you are not sharing presence with that user, the service cannot see your online state.
4. For playtime to appear, you must also be **sharing play activity** with that user (Play Activity Settings).
   - If you don’t want to share play activity with other Switch friends, set this user as a **Best Friend** and keep sharing only with them.
5. Copy the presence URL from the nxapi website (example): `https://nxapi-presence.fancy.org.uk/api/presence/03e0f77eb2a15cd9`

> Tip: Treat your presence URL as sensitive—only paste it into Home Assistant or other systems you trust. You can manage or revoke registered accounts at https://nxapi-auth.fancy.org.uk.


## Installation (HACS)
[![HACS Repository](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=itsfatlum&repository=Nintendo-Switch-Presence)

Click the badge above to open the HACS repository page for this integration.


## Manual installation (without HACS)
1. Copy the folder `custom_components/nintendo_switch_presence/` into your Home Assistant `config/custom_components/` folder.  
2. Ensure `manifest.json` and `hacs.json` are present.  
3. Restart Home Assistant.  
4. Add integration via **Settings → Devices & Services → Add Integration → Nintendo Switch Presence**, then paste your presence URL.

---

## How to confirm it’s working ✅
- After adding the integration you should see sensors appear under **Settings → Devices & Services** for the added account. If sensors appear, the integration is working.

If no sensors are visible: double-check the presence URL, confirm presence/play activity are shared as required, restart Home Assistant, and consult Home Assistant logs.


## Available Sensors

### Profile Sensor
Shows your Nintendo Switch profile information.
- **State**: Current online status (Online/Offline)
- **Icon**: Nintendo Switch MDI icon (with optional profile picture as entity image)
- **Attributes**:
  - `Account Name` - Your Switch account name
  - `Status` - Online or Offline status
  - `Game Name` - Currently playing game (if any)
  - `Game Image URL` - URL to the game cover image
  - `Total Play Time` - Total playtime in hours for current game
  - `First Played At` - ISO timestamp of when the game was first played
  - `Platform` - Nintendo Switch 1 or Nintendo Switch 2

### Game Sensor
Shows detailed information about your currently playing game.
- **State**: Current game name (or empty if not playing)
- **Icon**: Nintendo Switch MDI icon (with optional game cover as entity image)
- **Attributes**:
  - `Name` - Your Switch account name
  - `Game Name` - Currently playing game title
  - `Game Image URL` - URL to the game cover image
  - `Total Play Time` - Total playtime in hours
  - `First Played At` - ISO timestamp of when first played
  - `Platform` - Nintendo Switch 1 or Nintendo Switch 2
  - `Battle Mode` - Splatoon 3 battle mode (when playing Splatoon 3)
  - `Game Mode` - Splatoon 3 game mode/rule (when playing Splatoon 3)

### Splatoon 3 Sensor (Optional)
Shows Splatoon 3 specific information (only if enabled in setup).
- **State**: Battle mode when playing Splatoon 3, or general online status
- **Icon**: Water droplet MDI icon (shows Splatoon 3 game icon when actively playing)
- **Attributes**:
  - `Nickname` - Your Splatoon 3 player nickname
  - `Player Name` - Your Splatoon 3 player name
  - `Battle Mode` - Current battle mode in Splatoon 3
  - `Game Mode` - Current game mode/rule in Splatoon 3
  - `Platform` - Nintendo Switch 1 or Nintendo Switch 2


## Troubleshooting
- **No sensors after adding:** Ensure the presence URL is correct and reachable from your Home Assistant instance. Check Home Assistant logs for errors.  
- **Playtime missing:** Confirm your Switch play activity is shared with the presence user (Play Activity Settings).  
- **Presence shows OFFLINE when you are online:** Verify friend/presence sharing settings on the Switch and that the presence user is allowed to view your presence.    
- **Errors on setup:** Check HA logs for tracebacks. Common fixes include correcting the presence URL, ensuring HA can reach the API, and fixing missing dependencies in `manifest.json`.


## Data & privacy notes
- This integration reads the presence URL you paste. Treat that URL as sensitive if you want privacy.  
- Only share your presence URL with systems you trust and ensure you are comfortable sharing presence/play activity with the registered presence user.

# Disclaimer
The API used in this integration is not mine and belongs to [Samuel](https://gitlab.fancy.org.uk/samuel/nxapi-auth).
The code in this integration was generated with [AI](https://chatgpt.com).