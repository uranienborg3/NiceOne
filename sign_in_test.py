import pytest
import random
import json
import datetime
from pages.home_page import HomePage
from pages.sign_in import SignIn
from faker import Faker


class TestSignIn:
    @pytest.fixture(scope="function")
    def register(self):
        fake = Faker()
        self.data = {"email": str(random.randint(1, 100)) + fake.email(),
                     "name": fake.first_name(),
                     "surname": fake.last_name(),
                     "password": fake.password(length=5, special_chars=False),
                     "address_1": fake.street_address(),
                     "address_2": fake.secondary_address(),
                     "city": fake.city(),
                     "postcode": fake.postcode(),
                     "company": fake.company(),
                     "mobile": "+1" + str(random.random())[-10:],
                     "home_phone": "+1" + str(random.random())[-10:],
                     "add_info": fake.sentence(nb_words=10)}
        with open("test_data_" + datetime.datetime.now().strftime('%Y%m%d_%H%M%S') + ".json", "w") as f:
            json.dump(self.data, f, sort_keys=True, indent=2)

    @pytest.fixture(scope="function")
    def get_credentials(self):
        with open("test_data_20200411_212033.json") as f:
            data = json.load(f)
        self.email = data.get('email')
        self.password = data.get('password')

    def test_guest_can_go_to_sign_in(self, browser):
        home_page = HomePage(browser)
        home_page.go_to_sign_in()
        sign_in_page = SignIn(browser)
        sign_in_page.should_be_authentication_header()
        sign_in_page.authentication_should_be_in_breadcrumbs()

    @pytest.mark.register
    @pytest.mark.skip(reason="It will register a new user and we can not delete from data base")
    def test_guest_can_register(self, browser, register):
        home_page = HomePage(browser)
        home_page.go_to_sign_in()
        sign_in_page = SignIn(browser)
        sign_in_page.enter_email(self.data.get("email"))
        sign_in_page.fill_in_info(self.data.get("name"),
                                  self.data.get("surname"),
                                  self.data.get("password"),
                                  self.data.get("company"),
                                  self.data.get("address_1"),
                                  self.data.get("address_2"),
                                  self.data.get("city"),
                                  self.data.get("postcode"),
                                  self.data.get("add_info"),
                                  self.data.get("home_phone"),
                                  self.data.get("mobile"))
        sign_in_page.register_account()

    @pytest.mark.sign_in
    def test_user_can_sign_in(self, browser, get_credentials):
        home_page = HomePage(browser)
        home_page.go_to_sign_in()
        sign_in_page = SignIn(browser)
        sign_in_page.sign_in(self.email, self.password)
