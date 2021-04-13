import unittest
import main


class TaskTest(unittest.TestCase):
    @classmethod
    def setUp(cls):

        cls.posts = \
            [
                {
                    "userId": 1,
                    "id": 1,
                    "title": "powtarza sie",
                    "body": "1"
                },
                {
                    "userId": 1,
                    "id": 2,
                    "title": "powtarza sie",
                    "body": "1"
                },
                {
                    "userId": 1,
                    "id": 3,
                    "title": "random",
                    "body": "1"
                },
                {
                    "userId": 2,
                    "id": 4,
                    "title": "powtarza sie",
                    "body": "1"
                },
            ]
        cls.users = \
            [
                {
                    "id": 1,
                    "name": "Leanne Graham",
                    "username": "Bret",
                    "email": "Sincere@april.biz",
                    "address": {
                        "geo": {
                            "lat": "-37.3159",
                            "lng": "81.1496"
                        }
                    },
                },
                {
                    "id": 2,
                    "name": "Leanne Graham",
                    "username": "John",
                    "email": "Sincere@april.biz",
                    "address": {
                        "geo": {
                            "lat": "-40.3159",
                            "lng": "-80.1496"
                        }
                    },
                },
                {
                    "id": 3,
                    "name": "Leanne Graham",
                    "username": "Erika",
                    "email": "Sincere@april.biz",
                    "address": {
                        "geo": {
                            "lat": "50.3214",
                            "lng": "20.1496"
                        }
                    },
                }
            ]

        cls.connected_posts_with_users = [
            {
                "id": 1,
                "name": "Leanne Graham",
                "username": "Bret",
                "email": "Sincere@april.biz",
                "address": {
                    "geo": {
                        "lat": "-37.3159",
                        "lng": "81.1496"
                    }
                },
                "posts": [
                    {
                        "userId": 1,
                        "id": 1,
                        "title": "powtarza sie",
                        "body": "1"
                    },
                    {
                        "userId": 1,
                        "id": 2,
                        "title": "powtarza sie",
                        "body": "1"
                    },
                    {
                        "userId": 1,
                        "id": 3,
                        "title": "random",
                        "body": "1"
                    },
                ]
            },
            {
                "id": 2,
                "name": "Leanne Graham",
                "username": "John",
                "email": "Sincere@april.biz",
                "address": {
                    "geo": {
                        "lat": "-40.3159",
                        "lng": "-80.1496"
                    }
                },
                "posts": [
                    {
                        "userId": 2,
                        "id": 4,
                        "title": "powtarza sie",
                        "body": "1"
                    },
                ]
            },
            {
                "id": 3,
                "name": "Leanne Graham",
                "username": "Erika",
                "email": "Sincere@april.biz",
                "address": {
                    "geo": {
                        "lat": "50.3214",
                        "lng": "20.1496"
                    }
                },
                "posts": [
                ]
            }
        ]

    def test_get_users_with_posts(self):
        connected_data = main.get_users_with_posts(self.users, self.posts)
        self.assertDictEqual(self.connected_posts_with_users, connected_data, "Failed on connecting users with posts")

    def test_get_not_unique_titles(self):
        data = main.get_not_unique_titles(self.posts)
        is_repeating = False
        for post in data:
            if post["title"] == "powtarza sie":
                is_repeating = True
        self.assertTrue(is_repeating)

    def test_distance_between_geolocations(self):
        geo1 = {
            "lat": "28.426846",
            "lng": "77.088834"
        }

        geo2 = {
            "lat": "28.394231",
            "lng": "77.050308"
        }
        result = main.calculate_distance_between_geolocations(geo1, geo2)
        self.assertEqual(5.229712941541709, result, "Testing calculating distance failed")

    def test_get_distance_between_users(self):
        distances = main.get_distance_between_users(self.users)
        self.assertEqual(['The closest user to Bret lives John', 'The closest user to John lives Bret'], distances)


if __name__ == "__main__":
    unittest.main()
