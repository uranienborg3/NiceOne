import pytest
import random
from pages.home_page import HomePage
from pages.sign_in import SignIn
from faker import Faker


@pytest.mark.sign_in
class TestSignIn:
    @pytest.fixture(scope="function")
    def register(self):
        fake = Faker()
        self.data = {"email": str(random.randint(1, 100)) + fake.email(),
                     "name": fake.first_name(),
                     "surname": fake.last_name(),
                     "passwd": fake.password(length=5, special_chars=False),
                     "address_1": fake.street_address(),
                     "address_2": fake.secondary_address(),
                     "city": fake.city(),
                     "postcode": fake.postcode(),
                     "company": fake.company(),
                     "mobile": "+1" + str(random.random())[-10:],
                     "home_phone": "+1" + str(random.random())[-10:],
                     "add_info": fake.sentence(nb_words=10)}
        test_data = open("test_data.txt", "a")
        test_data.write("Credentials:\n")
        for key, value in self.data.items():
            test_data.write(f"{key}: {value}\n")
        test_data.close()

    def test_guest_can_go_to_sign_in(self, browser):
        home_page = HomePage(browser)
        home_page.go_to_sign_in()
        sign_in_page = SignIn(browser)
        sign_in_page.should_be_authentication_header()
        sign_in_page.authentication_should_be_in_breadcrumbs()

    @pytest.mark.register
    @pytest.mark.skip
    def test_guest_can_register(self, browser, register):
        home_page = HomePage(browser)
        home_page.go_to_sign_in()
        sign_in_page = SignIn(browser)
        sign_in_page.enter_email(self.data.get("email"))
        sign_in_page.fill_in_name_and_password(self.data.get("name"),
                                               self.data.get("surname"),
                                               self.data.get("passwd"))
        sign_in_page.set_birthday()
        sign_in_page.fill_in_address_and_country(self.data.get("company"),
                                                 self.data.get("address_1"),
                                                 self.data.get("address_2"),
                                                 self.data.get("city"),
                                                 self.data.get("postcode"))
        sign_in_page.fill_in_phone_and_add_info(self.data.get("add_info"),
                                                self.data.get("home_phone"),
                                                self.data.get("mobile"))
        sign_in_page.register_account()

    def test_user_can_sign_in(self, browser):
        home_page = HomePage(browser)
        home_page.go_to_sign_in()
        sign_in_page = SignIn(browser)
        sign_in_page.sign_in('43bennettstephanie@yahoo.com', 'vh6Va')
