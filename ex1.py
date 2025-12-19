from dataclasses import dataclass, asdict, replace
import json
from typing import Self

@dataclass(frozen=True, slots=True)
class Livre:
    titre: str
    auteur: str
    annee: int
    prix: float

    # --- Extension 1 : Immutabilité et Modification ---
    def promo(self, prix_reduit: float) -> Self:
        """Retourne une nouvelle instance avec le prix modifié."""
        return replace(self, prix=prix_reduit)

    # --- Extension 2 : Désérialisation ---
    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Reconstitue un objet Livre à partir d'une chaîne JSON."""
        donnees = json.loads(json_str)
        return cls(**donnees)

    def to_json(self) -> str:
        """Sérialise l'objet en JSON."""
        return json.dumps(asdict(self), ensure_ascii=False)

    # --- Extension 3 : Comparaison par prix ---
    def __lt__(self, other: Self) -> bool:
        """Permet le tri par prix (ordre croissant)."""
        if not isinstance(other, Livre):
            return NotImplemented
        return self.prix < other.prix

    def __eq__(self, other: object) -> bool:
        """Vérifie l'égalité basée sur le contenu."""
        if not isinstance(other, Livre):
            return False
        return (self.titre, self.auteur, self.annee, self.prix) == \
               (other.titre, other.auteur, other.annee, other.prix)
l1 = Livre("1984", "George Orwell", 1949, 9.90)
l2 = Livre("Le Meilleur des Mondes", "Aldous Huxley", 1932, 8.50)

catalog = [l1, l2]
catalog.sort()  # Tri automatique par prix grâce à __lt__
print(f"Livre le moins cher : {catalog[0].titre} ({catalog[0].prix}€)")

# 2. Application d'une promotion
l1_promo = l1.promo(7.50)
print(f"Ancien prix de 1984 : {l1.prix}€ | Nouveau prix : {l1_promo.prix}€")

# 3. Chargement depuis JSON
json_data = '{"titre": "Fahrenheit 451", "auteur": "Ray Bradbury", "annee": 1953, "prix": 10.2}'
l3 = Livre.from_json(json_data)
print(f"Chargé : {l3.titre} de {l3.auteur}")