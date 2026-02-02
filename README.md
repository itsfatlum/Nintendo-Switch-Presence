# Nintendo Switch Status

**Introduction**  
Nintendo Switch Status is a simple Home Assistant custom integration that polls an NXAPI presence URL and exposes your Switch presence and activity inside Home Assistant (online status, current game, playtime, profile, images, platform, etc.). This README explains how to register with the nxapi-auth service, install via HACS, configure the integration, and troubleshoot common issues. Please not that this was made with AI because I don't know how to code.

---

## Quick start — nxapi-auth steps (required)
1. Join the support Discord server (https://discord.com/invite/4D82rFkXRv).
   > **Important:** *This service is only available to members of this server. If you leave this server you may be removed from the presence server user.*  
2. Register on `https://nxapi-auth.fancy.org.uk/` and add a Nintendo Switch account and copy the **presence URL** for that account.  
3. Make sure you are **sharing your presence** with the user you registered (Friend Settings).  
   - *If you are not sharing presence with that user, the service cannot see your online state.*  
4. For playtime to appear, you must also be **sharing play activity** with that user (Play Activity Settings).  
   - If you don’t want to share play activity with other Switch friends, you can set this user as a **Best Friend** and keep sharing only with them.  
5. Copy the presence URL (example): https://nxapi-presence.fancy.org.uk/api/presence/03e0f77eb2a15cd9



## Installation (HACS)
[![HACS Repository](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=itsfatlum&repository=Nintendo-Switch-Status)

Click the badge above to open the HACS repository page for this integration.

## Manual Installation (HACS)
1. Copy the link to the repo: `https://github.com/itsfatlum/Nintendo-Switch-Status`.  
2. In Home Assistant go to **HACS → Integrations → ⋮ (top-right) → Custom repositories**.  
3. Paste the GitHub repo URL: https://github.com/itsfatlum/Nintendo-Switch-Status

- Select **Category: Integration** and click **Add**.  
4. Install **Nintendo Switch Status** from HACS.  
5. Restart Home Assistant.


## Manual installation (if you do NOT use HACS)
1. Copy the folder `custom_components/nintendo_switch_status/` into your Home Assistant `config/custom_components/` folder.  
2. Ensure `manifest.json` and `hacs.json` are correct.  
3. Restart Home Assistant.  
4. Add integration via **Settings → Devices & Services → Add Integration → Nintendo Switch Status**, then paste your presence URL.


## Add the integration (UI)
1. After restart go to **Settings → Devices & Services → Add Integration**.  
2. Search for **Nintendo Switch Status** and click it.  
3. The integration will ask for your **presence API URL** — paste the URL you copied from the website server and submit.  
4. After setup a device named **Nintendo Switch** will be created and the following sensors/entities will appear:
- **Online Status** (ONLINE / OFFLINE)  
- **Current Game**  
- **Game Image URL** (entity picture available)  
- **Profile Name**  
- **Profile Image URL** (entity picture available)  
- **Nintendo Switch Account ID**  
- **Total Playtime** (minutes) — extra attribute `hours` included  
- **Platform** (shows `Nintendo Switch 1` or `Nintendo Switch 2`)


## Troubleshooting
- **No sensors after adding:** Ensure the presence URL is correct and reachable from your Home Assistant instance (try `curl` from the HA host). Check Home Assistant logs for errors.  
- **Playtime missing:** Confirm your Switch play activity is shared with the presence user (Play Activity Settings).  
- **Presence shows OFFLINE when you are online:** Verify friend/presence sharing settings on the Switch and that the presence user is allowed to view your presence.  
- **Icon not showing in HACS:** Make sure `icon.png` is in `custom_components/nintendo_switch_status/` and the repo is public. Browser/CDN caching can delay updates (clear cache or wait up to 24 hours for CDN).  
- **Errors on setup:** Check HA logs for tracebacks. Common fixes include correcting the presence URL, ensuring HA can reach the API, and fixing missing dependencies in `manifest.json`.


## Data & privacy notes
- This integration reads the presence URL you paste. Treat that URL as sensitive if you want privacy.  
- Only paste URLs you trust and ensure you are comfortable sharing presence/play activity with the registered presence user.
- You can find the source code of nxapi on https://github.com/samuelthomas2774/nxapi.