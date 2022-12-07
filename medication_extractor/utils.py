# standard libaries
from typing import Dict, List

# custom libraries
from medication_extractor.extractor import MedicationExtractor
from medication_extractor.rxnorm_api import RXNormAPI


def map_medications(medications: List[str]) -> Dict[str, str]:
    """Map a list of medication extracted by `MedicationExtractor`
    to their RXNorm CUI codes

    Args:
        medications (List[str]): List of medications

    Returns:
        Dict[str, str]: Mapping {Medication: RXCUI}
    """
    mapping_dict = {}

    for medication in medications:
        results = RXNormAPI().get_approximate_match(medication)
        if results and "candidate" in results["approximateGroup"]:
            candiates = results["approximateGroup"]["candidate"]
            rxnorm_val = next((item for item in candiates if item["source"] == "RXNORM"), None)
            mapping_dict[rxnorm_val["name"]] = rxnorm_val["rxcui"]

    return mapping_dict


def get_medications(text: str) -> List[str]:
    """Get medications from text

    Args:
        text (str): Raw text

    Returns:
        List[str]: Medication mentions
    """
    extractor = MedicationExtractor()
    return extractor.extract(text)


def get_medication_mapping(text: str) -> Dict[str, str]:
    """Helper function to extract medications and map
    to RXNorm CUI codes

    Args:
        text (str): Raw text

    Returns:
        Dict[str, str]: Mapping {Medication: RXCUI}
    """
    medications = get_medications(text)
    return map_medications(medications)
