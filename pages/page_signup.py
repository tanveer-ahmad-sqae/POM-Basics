from pages.basePage import BasePage


class SignupPage(BasePage):

    def __int__(self, driver):
        super().__init__(driver)
        self.driver = driver

    popupName = "//h3[@xpath=1]"
    name = "//input[@name = 'name']"
    phone = "//input[@name = 'phone']"
    email = "//input[@name = 'email']"
    country = "//select[@name = 'country']"
    city = "//input[@name = 'city']"
    userName = "//input[@name = 'username'] [@style]"
    password = "//*[@id='load_form']/fieldset[7]/input"
    submit = "//*[@id='load_form']/div[1]/div[2]/input"
    sigIn = "//a [@href='#login']"
    websiteLink = "#load_form > div:nth-child(13) > div > p:nth-child(1) > a"
    membership = "#load_form > div:nth-child(13) > div > p:nth-child(2) > a"

    def getPopupName(self):
        return self.driver.find_element_by_xpath(self.popupName)

    def getName(self):
        return self.driver.find_element_by_xpath(self.name)

    def enterName(self, enter_name):
        self.getName().send_keys(enter_name)

    def getPhone(self):
        return self.driver.find_element_by_xpath(self.phone)

    def getEmail(self):
        self.driver.find_element_by_xpath(self.email)

    def getCountry(self):
        self.driver.find_element_by_xpath(self.country)

    def getCity(self):
        self.driver.find_element_by_xpath(self.city)

    def getUserName(self):
        self.driver.find_element_by_xpath(self.userName)

    def getPassword(self):
        self.driver.find_element_by_xpath(self.password)

    def getSubmit(self):
        self.driver.find_element_by_xpath(self.submit)

    def getSignIn(self):
        self.driver.find_element_by_xpath(self.sigIn)

    def getWebsiteLink(self):
        self.driver.find_element_by_css_selector(self.websiteLink)

    def getMembership(self):
        self.driver.find_element_by_css_selector(self.membership)



