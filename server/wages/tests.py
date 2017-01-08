from django.test import TestCase, Client
from django.urls import reverse
from wages.views import DEFAULT_LIMIT, STATS_LIMIT

client = Client()


class WageApiTest(TestCase):
    fixtures = ['sample_data.json']

    def test_data_and_status_in_result(self):
        """
        All api responses should have a data field and a status field
        """
        response = self.client.get(reverse('wages:get_wages'))

        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertIn('data', result)
        self.assertIn('status', result)

    def test_limits_api(self):
        """
        Limits api should respond with valid limits on usage
        """
        response = self.client.get(reverse('wages:get_limits'))

        self.assertEqual(response.status_code, 200)
        result = response.json()
        query_limit = result['data']['query_size_limit']
        self.assertEqual(query_limit, DEFAULT_LIMIT)
        stats_limit = result['data']['stats_limit']
        self.assertEqual(stats_limit, STATS_LIMIT)

    def test_request_less_than_min_page(self):
        """
        If a user requests less than the minimum page it should return page 1
        """
        response = self.client.get(reverse('wages:get_wages'),
                                   {'page': -1})
        self.assertEqual(response.status_code, 200)
        result = response.json()
        data = result['data']
        self.assertEqual(data['cur_page'], 1)

    def test_request_greater_than_max_page(self):
        """
        If a user requests greater than the max page should return the max page
        """
        response = self.client.get(reverse('wages:get_wages'),
                                   {'page': 99999999999})

        self.assertEqual(response.status_code, 200)
        result = response.json()
        data = result['data']
        self.assertEqual(data['cur_page'], data['last_page'])

    def test_request_empty_result_query(self):
        """
        If a user makes a query that will return an empty result, it should
        return an empty list
        """
        response = self.client.get(reverse('wages:get_wages'),
                                   {'first_name': 'no_one_has_this_name'})
        self.assertEqual(response.status_code, 200)
        result = response.json()
        data = result['data']
        self.assertEqual(len(data['wages']), 0)

    def test_request_negative_limit_returns_default(self):
        """
        If a user sets request limit to a negative number it should return
        the default limit
        """
        response = self.client.get(reverse('wages:get_wages'),
                                   {'limit': -1})
        self.assertEqual(response.status_code, 200)
        result = response.json()
        data = result['data']
        self.assertEqual(len(data['wages']), DEFAULT_LIMIT)
