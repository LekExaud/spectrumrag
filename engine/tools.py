import json

def lookup_spectrum_band(band_name: str, frequency_start_mhz: float, frequency_end_mhz: float, region: str) -> str:
    """Simulated database or regulatory document lookup for spectrum bands."""
    database = {
        "C-band": {"allocation": "Mobile (IMT) Primary", "status": "Active for 5G deployment in TCRA jurisdiction", "notes": "Subject to earth station coordination."},
        "mmWave": {"allocation": "Fixed Wireless Access / Mobile Primary", "status": "Emerging licensing framework", "notes": "High attenuation, short range."}
    }
    
    result = database.get(band_name, {
        "allocation": "Unknown / Unassigned", 
        "status": "Requires manual ITU/TCRA frequency clearance check", 
        "notes": "No local record found."
    })
    
    return json.dumps({
        "band_name": band_name,
        "range_mhz": f"{frequency_start_mhz}-{frequency_end_mhz}",
        "region": region,
        **result
    }, indent=2)

# Registry mapping tool names to functions
AVAILABLE_TOOLS = {
    "lookup_spectrum_band": lookup_spectrum_band
}