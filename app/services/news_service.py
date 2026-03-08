
def get_sector_news(sector: str) -> str:
    data = {
        "technology": "AI startups in India are growing rapidly and IT exports remain strong.",
        "pharmaceuticals": "Indian pharma companies expanding generic drug exports globally.",
        "agriculture": "Improved irrigation and export demand boosting crop production."
    }

    return data.get(sector.lower(), "Sector shows moderate growth with emerging opportunities.")
