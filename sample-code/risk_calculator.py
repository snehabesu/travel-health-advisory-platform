from typing import Any

def get_country_outbreaks(country: str, dataset: list[dict[str, Any]]) -> list[dict[str, str]]:
    """
    Returns a list of outbreaks for a given country,
    including disease name and reported date.
    """
    return [
        {
            "disease": entry.get("disease", "Unknown"),
            "date": entry.get("date", "Unknown"),
        }
        for entry in dataset
        if entry.get("country", "").strip().lower() == country.strip().lower()
    ]

def calculate_risk_score(outbreaks: list[dict[str, str]]) -> float:
    """
    Calculates a simple travel risk score out of 10
    based on the number of outbreaks recorded.
    """
    outbreak_count = len(outbreaks)

    if outbreak_count >= 9:
        return 9.0
    if outbreak_count >= 7:
        return 8.0
    if outbreak_count >= 5:
        return 7.0
    if outbreak_count >= 3:
        return 5.0
    if outbreak_count >= 1:
        return 3.0
    return 1.0
