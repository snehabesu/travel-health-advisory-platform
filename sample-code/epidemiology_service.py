from typing import Any
from risk_calculator import get_country_outbreaks

def generate_epidemiology_summary(country: str, dataset: list[dict[str, Any]]) -> str:
    """
    Returns a short epidemiology summary for a country
    using outbreak data from a JSON-based dataset.
    """
    outbreaks = get_country_outbreaks(country, dataset)

    if not outbreaks:
        return f"No active outbreak records were found for {country} in the current dataset."

    latest_outbreak = outbreaks[-1]
    disease = latest_outbreak.get("disease", "an unknown disease")
    date = latest_outbreak.get("date", "an unknown date")

    return (
        f"{country} has {len(outbreaks)} recorded outbreak(s) in the dataset. "
        f"The most recent recorded outbreak is {disease}, reported on {date}."
    )
  
