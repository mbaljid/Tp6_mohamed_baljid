import unittest
import json
from dataclasses import FrozenInstanceError
from ex2 import Film, favoris_to_json

class TestFilm(unittest.TestCase):

    def setUp(self):
        self.film_data = {
            "titre": "Inception",
            "realisateur": "Christopher Nolan",
            "annee": 2010,
            "note": 8.8
        }
        self.movie = Film(**self.film_data)

    def test_immutability(self):
        """Verify that attributes cannot be modified after creation."""
        with self.assertRaises(FrozenInstanceError):
            self.movie.note = 9.0

    def test_is_classic(self):
        """Verify the 2000 threshold logic."""
        old_movie = Film("Pulp Fiction", "Tarantino", 1994, 8.9)
        new_movie = Film("Interstellar", "Nolan", 2014, 8.6)
        boundary_movie = Film("Gladiator", "Scott", 2000, 8.5)
        
        self.assertTrue(old_movie.est_classique())
        self.assertFalse(new_movie.est_classique())
        self.assertFalse(boundary_movie.est_classique())

    def test_json_roundtrip(self):
        """Verify that to_json and from_json are consistent."""
        json_str = self.movie.to_json()
        new_movie = Film.from_json(json_str)
        self.assertEqual(self.movie, new_movie)

    def test_sorting_by_rating(self):
        """Verify that films are sorted by note (ascending)."""
        f1 = Film("Low Score", "Dir A", 2020, 2.0)
        f2 = Film("High Score", "Dir B", 2020, 9.5)
        f3 = Film("Mid Score", "Dir C", 2020, 5.0)
        
        sorted_films = sorted([f2, f1, f3])
        self.assertEqual(sorted_films[0].note, 2.0)
        self.assertEqual(sorted_films[-1].note, 9.5)

    def test_list_serialization(self):
        """Verify the favorites list serialization."""
        catalog = [self.movie, Film("Vertigo", "Hitchcock", 1958, 8.3)]
        json_output = favoris_to_json(catalog)
        parsed_data = json.loads(json_output)
        self.assertEqual(len(parsed_data), 2)
        self.assertEqual(parsed_data[1]["titre"], "Vertigo")

if __name__ == "__main__":
    unittest.main()