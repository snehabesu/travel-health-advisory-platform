def get_country_outbreaks(country: str, dataset: list) -> list:
    """
    Returns a list of outbreaks for a given country,
    including disease name and reported date.
    """
    return [
        {
            "disease": entry["disease"],
            "date": entry["date"]
        }
        for entry in dataset
        if entry["country"] == country
    ]
