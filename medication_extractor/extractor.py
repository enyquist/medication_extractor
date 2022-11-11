# standard libaries
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import ClassVar, List

# third party libraries
import spacy


@dataclass
class Extractor(ABC):
    """Base Extractor"""

    nlp: ClassVar[spacy.language.Language]

    @abstractmethod
    def extract(self, text: str) -> List[str]:
        """Abstract Method for extraction"""
        pass


@dataclass
class MedicationExtractor(Extractor):
    """Extract medication names from text"""

    nlp = ClassVar[spacy.language.Language] = spacy.load("en_core_med7_lg")

    def extract(self, text: str) -> List[str]:
        """Extract medications from text

        Args:
            text (str): Raw text

        Returns:
            List[str]: List of medication names identified in text
        """
        doc = self.nlp(text)
        return [ent.text for ent in doc.ents if ent.label_ == "DRUG"]
