import json
import unittest
from unittest.mock import Mock, patch
from pact_python.dsl import Pact, SomethingLike, term
from pact_python.provider import Provider
from pact_python.matchers import integer_type, url_path

class TestDashboardContract(unittest.TestCase):

    def setUp(self):
        self.pact = Pact()
        self.provider = Provider(
            consumer="dashboard",
            provider="employee_service",
            host="localhost",
            port=80,
            pact_file=self.pact.write_pact(),
        )

    def tearDown(self):
        self.pact.finalize()

    @patch("requests.get")
    def test_get_all_employees_contract(self, mock_get):
        # Setup the expected response for the Employee service
        employee_response = {
            "employees": [
                {
                    "id": 1,
                    "name": "John Doe",
                    "age": 30,
                },
                {
                    "id": 2,
                    "name": "Jane Doe",
                    "age": 25,
                },
            ]
        }
        expected = json.dumps(employee_response)

        # Setup the mocked response from the Employee service
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = employee_response

        # Define the expected interaction between Dashboard and Employee services
        interaction = self.pact.given("There are some employees").upon_receiving("a request to get all employees").with_request(
            method="GET",
            path=url_path("/employees"),
            headers={
                "Content-Type": "application/json"
            }
        ).will_respond_with(
            200,
            headers={
                "Content-Type": "application/json"
            },
            body=SomethingLike(employee_response),
        )

        # Call the Dashboard service endpoint
        from your_dashboard_module import get_all_employees
        actual = get_all_employees()

        # Assert the returned result
        self.assertEqual(actual, employee_response["employees"])

        # Add the interaction to the Pact
        self.pact.add_interaction(interaction)

    @patch("requests.post")
    def test_create_employee_contract(self, mock_post):
        # Setup the expected response for the Employee service
        employee_response = {
            "id": 3,
            "name": "New Employee",
            "age": 22,
        }
        expected = json.dumps(employee_response)

        # Setup the mocked response from the Employee service
        mock_post.return_value.status_code = 201
        mock_post.return_value.json.return_value = employee_response

        # Define the expected interaction between Dashboard and Employee services
        interaction = self.pact.given("There are some employees").upon_receiving("a request to create a new employee").with_request(
            method="POST",
            path=url_path("/employees"),
            headers={
                "Content-Type": "application/json"
            },
            body={
                "name": "New Employee",
                "age": 22,
            }
        ).will_respond_with(
            201,
            headers={
                "Content-Type": "application/json"
            },
            body=SomethingLike(employee_response),
        )

        # Call the Dashboard service endpoint
        from your_dashboard_module import create_employee
        actual = create_employee("New Employee", 22)

        # Assert the returned result
        self.assertEqual(actual, employee_response)

        # Add the interaction to the Pact
        self.pact.add_interaction(interaction)

    @patch("requests.put")
    def test_update_employee_contract(self, mock_put):
        # Setup the expected response for the Employee service
        employee_response = {
            "id": 1,
            "name": "Updated Employee",
            "age": 31,
        }
        expected = json.dumps(employee_response)

        # Setup the mocked response from the Employee service
        mock_put.return_value.status_code = 200
        mock_put.return_value.json.return_value = employee_response

        # Define the expected interaction between Dashboard and Employee services
        interaction = self.pact.given("There is an employee").upon_receiving("a request to update an employee").with_request(
            method="PUT",
            path=url_path("/employees/1"),
            headers={
                "Content-Type": "application/json"
            },
            body={
                "name": "Updated Employee",
                "age": 31,
            }
        ).will_respond_with(
            200,
            headers={
                "Content-Type": "application/json"
            },
            body=SomethingLike(employee_response),
        )

        # Call the Dashboard service endpoint
        from your_dashboard_module import update_employee
        actual = update_employee(1, "Updated Employee", 31)

        # Assert the returned result
        self.assertEqual(actual, employee_response)

        # Add the interaction to the Pact
        self.pact.add_interaction(interaction)

    @patch("requests.get")
    def test_get_employee_by_id_contract(self, mock_get):
    # Setup the expected response for the Employee service
        employee_response = {
            "id": 1,
            "name": "John Doe",
            "age": 30,
        }
        expected = json.dumps(employee_response)

    # Setup the mocked response from the Employee service
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = employee_response

    # Define the expected interaction between Dashboard and Employee services
        interaction = self.pact.given("There is an employee").upon_receiving("a request to get employee by id").with_request(
            method="GET",
            path=url_path("/employees/1"),
            headers={
                "Content-Type": "application/json"
            }
        ).will_respond_with(
            200,
            headers={
                "Content-Type": "application/json"
            },
            body=SomethingLike(employee_response),
        )

    # Call the Dashboard service endpoint
        from your_dashboard_module import get_employee_by_id
        actual = get_employee_by_id(1)

    # Assert the returned result
        self.assertEqual(actual, employee_response)

    # Add the interaction to the Pact
        self.pact.add_interaction(interaction)

    @patch("requests.put")
    def test_update_employee_contract(self, mock_put):
        # Setup the expected response for the Employee service
        employee_response = {
            "id": 1,
            "name": "Updated Employee",
            "age": 31,
        }
        expected = json.dumps(employee_response)

        # Setup the mocked response from the Employee service
        mock_put.return_value.status_code = 200
        mock_put.return_value.json.return_value = employee_response

        # Define the expected interaction between Dashboard and Employee services
        interaction = self.pact.given("There is an employee").upon_receiving("a request to update an employee").with_request(
            method="PUT",
            path=url_path("/employees/1"),
            headers={
                "Content-Type": "application/json"
            },
            body={
                "name": "Updated Employee",
                "age": 31,
            }
        ).will_respond_with(
            200,
            headers={
                "Content-Type": "application/json"
            },
            body=SomethingLike(employee_response),
        )

        # Call the Dashboard service endpoint
        from your_dashboard_module import update_employee
        actual = update_employee(1, "Updated Employee", 31)

        # Assert the returned result
        self.assertEqual(actual, employee_response)

        # Add the interaction to the Pact
        self.pact.add_interaction(interaction)