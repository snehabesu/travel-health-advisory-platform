from typing import Any
from risk_calculator import calculate_risk_score, get_country_outbreaks

def generate_travel_advice(country: str, dataset: list[dict[str, Any]]) -> str:
    """
    Generates user-facing travel advice for a country
    based on outbreak activity.
    """
    outbreaks = get_country_outbreaks(country, dataset)
    score = calculate_risk_score(outbreaks)

    if score >= 8:
        return (
            f"Travel to {country} requires a high level of caution. "
            "Review current outbreak information, follow WHO guidance, "
            "and consider whether travel is essential."
        )
    if score >= 5:
        return (
            f"Travel to {country} involves moderate health risk. "
            "Monitor outbreak updates, take recommended precautions, "
            "and remain aware of current public health advice."
        )
    return (
        f"Travel to {country} currently presents a lower level of health risk. "
        "Continue following standard precautions and check for updates before departure."
    )
  
