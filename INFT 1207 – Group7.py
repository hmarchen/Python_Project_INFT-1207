#  Author: Hlib Marchenko
#  ID: 100901448
#  File: testsuite.py
#  Date: 08.08.2023
#  Description: This Selenium program will open the demo bank web page and check New customer and Edit Customer functions.
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import HtmlTestRunner

class Test_New_Customer_and_Edit_customer(unittest.TestCase):
# setUpClass method initializes the browser
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()

    # Test case: Verify that name cannot be empty
    def test_Name_Cannot_Be_Empty(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/addcustomerpage.php")
        User_Input = driver.find_element(By.XPATH, "//body/table[@class='layout']/tbody/tr/td[@colspan='2']/table[@border='0']/tbody/tr[4]/td[2]/input[1]")
        User_Input.send_keys(Keys.TAB)
        error_message = driver.find_element(By.XPATH, "//label[@id='message']").text
        self.assertEqual("Customer name must not be blank", error_message, "Error message does not match")
        time.sleep(1)
    
    # Test case: Verify that name cannot be numeric
    def test_Name_Cannot_Be_Numeric(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/addcustomerpage.php")
        User_Input = driver.find_element(By.XPATH, "//body/table[@class='layout']/tbody/tr/td[@colspan='2']/table[@border='0']/tbody/tr[4]/td[2]/input[1]")
        User_Input.send_keys("1234")
        error_message = driver.find_element(By.XPATH, "//label[@id='message']").text
        self.assertEqual("Numbers are not allowed", error_message, "Error message does not match")
        time.sleep(1)

        User_Input = driver.find_element(By.XPATH, "//body/table[@class='layout']/tbody/tr/td[@colspan='2']/table[@border='0']/tbody/tr[4]/td[2]/input[1]")
        User_Input.clear()
        User_Input.send_keys("name1234")
        error_message = driver.find_element(By.XPATH, "//label[@id='message']").text
        self.assertEqual("Numbers are not allowed", error_message, "Error message does not match")
        time.sleep(1)
    # Test case: Verify that name cannot have special characters
    def test_Name_Cannot_Have_Special_Characters(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/addcustomerpage.php")
        User_Input = driver.find_element(By.XPATH, "//body/table[@class='layout']/tbody/tr/td[@colspan='2']/table[@border='0']/tbody/tr[4]/td[2]/input[1]")
        User_Input.send_keys("name!@#")
        error_message = driver.find_element(By.XPATH, "//label[@id='message']").text
        self.assertEqual("Special characters are not allowed", error_message, "Error message does not match")
        time.sleep(1)

        User_Input = driver.find_element(By.XPATH, "//body/table[@class='layout']/tbody/tr/td[@colspan='2']/table[@border='0']/tbody/tr[4]/td[2]/input[1]")
        User_Input.clear()
        User_Input.send_keys("!@#")
        error_message = driver.find_element(By.XPATH, "//label[@id='message']").text
        self.assertEqual("Special characters are not allowed", error_message, "Error message does not match")
        time.sleep(1)
    # Test case: Verify that name cannot have first character as blank space
    def test_Name_Cannot_Have_First_Character_As_Blank_Space(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/addcustomerpage.php")
        User_Input = driver.find_element(By.XPATH, "//body/table[@class='layout']/tbody/tr/td[@colspan='2']/table[@border='0']/tbody/tr[4]/td[2]/input[1]")
        User_Input.send_keys(" name")
        error_message = driver.find_element(By.XPATH, "//label[@id='message']").text
        self.assertEqual("First character can not have space", error_message, "Error message does not match")
        time.sleep(1)

    # Test case: Verify that address cannot be empty
    # Broken   
    def test_Address_Cannot_Be_Empty(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/addcustomerpage.php")
        User_Input = driver.find_element(By.XPATH, "//textarea[@rows='5']")
        User_Input.send_keys(Keys.TAB)
        error_message = driver.find_element(By.XPATH, "//label[@id='message3']").text
        self.assertEqual("ADDRESS Field must not be blank", error_message, "Error message does not match")
        time.sleep(1)

    # Test case: Verify that address cannot have first blank space
    def test_Address_Cannot_Have_First_Blank_Space(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/addcustomerpage.php")
        User_Input = driver.find_element(By.XPATH, "//textarea[@rows='5']")
        User_Input.send_keys(" address")
        error_message = driver.find_element(By.XPATH, "//label[@id='message3']").text
        self.assertEqual("First character can not have space", error_message, "Error message does not match")
        time.sleep(1)

    # Test case: Verify that city cannot be empty
    # Broken
    def test_City_Cannot_Be_Empty(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/addcustomerpage.php")
        User_Input = driver.find_element(By.XPATH, "//body/table[@class='layout']/tbody/tr/td[@colspan='2']/table[@border='0']/tbody/tr[8]/td[2]/input[1]")
        User_Input.send_keys(Keys.TAB)
        error_message = driver.find_element(By.XPATH, "//label[@id='message4']").text
        self.assertEqual("City Field must be not blank", error_message, "Error message does not match")
        time.sleep(1)

    # Test case: Verify that city cannot be numeric
    def test_City_cannot_be_numeric(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/addcustomerpage.php")
        User_Input = driver.find_element(By.XPATH, "//body/table[@class='layout']/tbody/tr/td[@colspan='2']/table[@border='0']/tbody/tr[8]/td[2]/input[1]")
        User_Input.send_keys("1234")
        error_message = driver.find_element(By.XPATH, "//label[@id='message4']").text
        self.assertEqual("Numbers are not allowed", error_message, "Error message does not match")
        time.sleep(1)

        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/addcustomerpage.php")
        User_Input = driver.find_element(By.XPATH, "//body/table[@class='layout']/tbody/tr/td[@colspan='2']/table[@border='0']/tbody/tr[8]/td[2]/input[1]")
        User_Input.send_keys("city123")
        error_message = driver.find_element(By.XPATH, "//label[@id='message4']").text
        self.assertEqual("Numbers are not allowed", error_message, "Error message does not match")
        time.sleep(1)

    # Test case: Verify that city cannot have special characters
    def test_City_cannot_have_special_character(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/addcustomerpage.php")
        User_Input = driver.find_element(By.XPATH, "//body/table[@class='layout']/tbody/tr/td[@colspan='2']/table[@border='0']/tbody/tr[8]/td[2]/input[1]")
        User_Input.send_keys("City!@#")
        error_message = driver.find_element(By.XPATH, "//label[@id='message4']").text
        self.assertEqual("Special characters are not allowed", error_message, "Error message does not match")
        time.sleep(1)

        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/addcustomerpage.php")
        User_Input = driver.find_element(By.XPATH, "//body/table[@class='layout']/tbody/tr/td[@colspan='2']/table[@border='0']/tbody/tr[8]/td[2]/input[1]")
        User_Input.send_keys("!@#")
        error_message = driver.find_element(By.XPATH, "//label[@id='message4']").text
        self.assertEqual("Special characters are not allowed", error_message, "Error message does not match")
        time.sleep(1)

    # Test case: Verify that city cannot have first blank space
    def test_City_cannot_have_first_blank_space(self):

        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/addcustomerpage.php")
        User_Input = driver.find_element(By.XPATH, "//body/table[@class='layout']/tbody/tr/td[@colspan='2']/table[@border='0']/tbody/tr[8]/td[2]/input[1]")
        User_Input.send_keys(" city")
        error_message = driver.find_element(By.XPATH, "//label[@id='message4']").text
        self.assertEqual("First character can not have space", error_message, "Error message does not match")
        time.sleep(1)

    # Test case: Verify that state cannot be empty    
    def test_State_cannot_be_empty(self):

        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/addcustomerpage.php")
        User_Input = driver.find_element(By.XPATH, "//body/table[@class='layout']/tbody/tr/td[@colspan='2']/table[@border='0']/tbody/tr[9]/td[2]/input[1]")
        User_Input.send_keys(Keys.TAB)
        error_message = driver.find_element(By.XPATH, "//label[@id='message5']").text
        self.assertEqual("State must not be blank", error_message, "Error message does not match")
        time.sleep(1)

    # Test case: Verify that state cannot be numeric
    def test_State_cannot_be_numeric(self):

        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/addcustomerpage.php")
        User_Input = driver.find_element(By.XPATH, "//body/table[@class='layout']/tbody/tr/td[@colspan='2']/table[@border='0']/tbody/tr[9]/td[2]/input[1]")
        User_Input.send_keys("1234")
        error_message = driver.find_element(By.XPATH, "//label[@id='message5']").text
        self.assertEqual("Numbers are not allowed", error_message, "Error message does not match")
        time.sleep(1)

        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/addcustomerpage.php")
        User_Input = driver.find_element(By.XPATH, "//body/table[@class='layout']/tbody/tr/td[@colspan='2']/table[@border='0']/tbody/tr[9]/td[2]/input[1]")
        User_Input.send_keys("State123")
        error_message = driver.find_element(By.XPATH, "//label[@id='message5']").text
        self.assertEqual("Numbers are not allowed", error_message, "Error message does not match")
        time.sleep(1)

    # Test case: Verify that state cannot have special characters
    def test_State_cannot_have_special_character(self):

        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/addcustomerpage.php")
        User_Input = driver.find_element(By.XPATH, "//body/table[@class='layout']/tbody/tr/td[@colspan='2']/table[@border='0']/tbody/tr[9]/td[2]/input[1]")
        User_Input.send_keys("State!@#")
        error_message = driver.find_element(By.XPATH, "//label[@id='message5']").text
        self.assertEqual("Special characters are not allowed", error_message, "Error message does not match")
        time.sleep(1)

        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/addcustomerpage.php")
        User_Input = driver.find_element(By.XPATH, "//body/table[@class='layout']/tbody/tr/td[@colspan='2']/table[@border='0']/tbody/tr[9]/td[2]/input[1]")
        User_Input.send_keys("!@#")
        error_message = driver.find_element(By.XPATH, "//label[@id='message5']").text
        self.assertEqual("Special characters are not allowed", error_message, "Error message does not match")
        time.sleep(1)

    # Test case: Verify that state cannot have first blank space
    # Broken
    def test_State_cannot_have_first_blank_space(self):

        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/addcustomerpage.php")
        User_Input = driver.find_element(By.XPATH, "//body/table[@class='layout']/tbody/tr/td[@colspan='2']/table[@border='0']/tbody/tr[9]/td[2]/input[1]")
        User_Input.send_keys(" state")
        error_message = driver.find_element(By.XPATH, "//label[@id='message5']").text
        self.assertEqual("First character cannot have space", error_message, "Error message does not match")
        time.sleep(1)

    # Test case: Verify that PIN must be numeric
    # Broken
    def test_PIN_must_be_numeric(self):

        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/addcustomerpage.php")
        User_Input = driver.find_element(By.XPATH, "//body/table[@class='layout']/tbody/tr/td[@colspan='2']/table[@border='0']/tbody/tr[10]/td[2]/input[1]")
        User_Input.send_keys("1234")
        error_message = driver.find_element(By.XPATH, "//label[@id='message6']").text
        self.assertEqual("Characters are not allowed", error_message, "Error message does not match")
        time.sleep(1)

        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/addcustomerpage.php")
        User_Input = driver.find_element(By.XPATH, "//body/table[@class='layout']/tbody/tr/td[@colspan='2']/table[@border='0']/tbody/tr[10]/td[2]/input[1]")
        User_Input.send_keys("1234PIN")
        error_message = driver.find_element(By.XPATH, "//label[@id='message6']").text
        self.assertEqual("Characters are not allowed", error_message, "Error message does not match")
        time.sleep(1)

    # Test case: Verify that PIN cannot be empty
    # Broken
    def test_PIN_cannot_be_empty(self):

        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/addcustomerpage.php")
        User_Input = driver.find_element(By.XPATH, "//body/table[@class='layout']/tbody/tr/td[@colspan='2']/table[@border='0']/tbody/tr[10]/td[2]/input[1]")
        User_Input.send_keys(Keys.TAB)
        error_message = driver.find_element(By.XPATH, "//label[@id='message6']").text
        self.assertEqual("PIN code must not be blank", error_message, "Error message does not match")
        time.sleep(1)

    # Test case: Verify that PIN must have 6 digits
    def test_PIN_must_have_6_digits(self):

        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/addcustomerpage.php")
        User_Input = driver.find_element(By.XPATH, "//body/table[@class='layout']/tbody/tr/td[@colspan='2']/table[@border='0']/tbody/tr[10]/td[2]/input[1]")
        User_Input.send_keys("12")
        error_message = driver.find_element(By.XPATH, "//label[@id='message6']").text
        self.assertEqual("PIN Code must have 6 Digits", error_message, "Error message does not match")
        time.sleep(1)

        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/addcustomerpage.php")
        User_Input = driver.find_element(By.XPATH, "//body/table[@class='layout']/tbody/tr/td[@colspan='2']/table[@border='0']/tbody/tr[10]/td[2]/input[1]")
        User_Input.send_keys("123")
        error_message = driver.find_element(By.XPATH, "//label[@id='message6']").text
        self.assertEqual("PIN Code must have 6 Digits", error_message, "Error message does not match")
        time.sleep(1)

    # Test case: Verify that PIN cannot have special characters
    def test_PIN_cannot_have_special_character(self):

        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/addcustomerpage.php")
        User_Input = driver.find_element(By.XPATH, "//body/table[@class='layout']/tbody/tr/td[@colspan='2']/table[@border='0']/tbody/tr[10]/td[2]/input[1]")
        User_Input.send_keys("!@#")
        error_message = driver.find_element(By.XPATH, "//label[@id='message6']").text
        self.assertEqual("Special characters are not allowed", error_message, "Error message does not match")
        time.sleep(1)

        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/addcustomerpage.php")
        User_Input = driver.find_element(By.XPATH, "//body/table[@class='layout']/tbody/tr/td[@colspan='2']/table[@border='0']/tbody/tr[10]/td[2]/input[1]")
        User_Input.send_keys("123!@#")
        error_message = driver.find_element(By.XPATH, "//label[@id='message6']").text
        self.assertEqual("Special characters are not allowed", error_message, "Error message does not match")
        time.sleep(1)

    # Test case: Verify that PIN cannot have first blank space
    # Broken
    def test_PIN_cannot_have_first_blank_space(self):

        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/addcustomerpage.php")
        User_Input = driver.find_element(By.XPATH, "//body/table[@class='layout']/tbody/tr/td[@colspan='2']/table[@border='0']/tbody/tr[10]/td[2]/input[1]")
        User_Input.send_keys(" pin")
        error_message = driver.find_element(By.XPATH, "//label[@id='message6']").text
        self.assertEqual("First character cannot have space", error_message, "Error message does not match")
        time.sleep(1)

    # Test case: Verify that PIN cannot have blank space
    def test_PIN_cannot_have_blank_space(self):

        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/addcustomerpage.php")
        User_Input = driver.find_element(By.XPATH, "//body/table[@class='layout']/tbody/tr/td[@colspan='2']/table[@border='0']/tbody/tr[10]/td[2]/input[1]")
        User_Input.send_keys("pin ")
        error_message = driver.find_element(By.XPATH, "//label[@id='message6']").text
        self.assertEqual("Characters are not allowed", error_message, "Error message does not match")
        time.sleep(1)
        
    # Test case: Verify that mobile number cannot be empty
    def test_Mobile_number_cannot_be_empty(self):

        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/addcustomerpage.php")
        User_Input = driver.find_element(By.XPATH, "//body/table[@class='layout']/tbody/tr/td[@colspan='2']/table[@border='0']/tbody/tr[11]/td[2]/input[1]")
        User_Input.send_keys(Keys.TAB)
        error_message = driver.find_element(By.XPATH, "//label[@id='message7']").text
        self.assertEqual("Mobile no must not be blank", error_message, "Error message does not match")
        time.sleep(1)

    # Test case: Verify that mobile number cannot have first character as blank space
    def test_Mobile_numberTelephone_cannot_have_first_character_as_blank_space(self):

        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/addcustomerpage.php")
        User_Input = driver.find_element(By.XPATH, "//body/table[@class='layout']/tbody/tr/td[@colspan='2']/table[@border='0']/tbody/tr[11]/td[2]/input[1]")
        User_Input.send_keys(" 289943")
        error_message = driver.find_element(By.XPATH, "//label[@id='message7']").text
        self.assertEqual("First character can not have space", error_message, "Error message does not match")
        time.sleep(1)

    # Test case: Verify that mobile number cannot have spaces
    def test_Mobile_number_cannot_have_spaces(self):

        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/addcustomerpage.php")
        User_Input = driver.find_element(By.XPATH, "//body/table[@class='layout']/tbody/tr/td[@colspan='2']/table[@border='0']/tbody/tr[11]/td[2]/input[1]")
        User_Input.send_keys("123 123")
        error_message = driver.find_element(By.XPATH, "//label[@id='message7']").text
        self.assertEqual("Characters are not allowed", error_message, "Error message does not match")
        time.sleep(1)

    # Test case: Verify that mobile number cannot have special characters
    def test_Mobile_number_cannot_have_special_character(self):

        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/addcustomerpage.php")
        User_Input = driver.find_element(By.XPATH, "//body/table[@class='layout']/tbody/tr/td[@colspan='2']/table[@border='0']/tbody/tr[11]/td[2]/input[1]")
        User_Input.send_keys("886636!@12")
        error_message = driver.find_element(By.XPATH, "//label[@id='message7']").text
        self.assertEqual("Special characters are not allowed", error_message, "Error message does not match")
        time.sleep(1)

        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/addcustomerpage.php")
        User_Input = driver.find_element(By.XPATH, "//body/table[@class='layout']/tbody/tr/td[@colspan='2']/table[@border='0']/tbody/tr[11]/td[2]/input[1]")
        User_Input.send_keys("!@88662682")
        error_message = driver.find_element(By.XPATH, "//label[@id='message7']").text
        self.assertEqual("Special characters are not allowed", error_message, "Error message does not match")
        time.sleep(1)

        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/addcustomerpage.php")
        User_Input = driver.find_element(By.XPATH, "//body/table[@class='layout']/tbody/tr/td[@colspan='2']/table[@border='0']/tbody/tr[11]/td[2]/input[1]")
        User_Input.send_keys("88663682!@")
        error_message = driver.find_element(By.XPATH, "//label[@id='message7']").text
        self.assertEqual("Special characters are not allowed", error_message, "Error message does not match")
        time.sleep(1)

    # Test case: Verify that email cannot be empty
    # Broken
    def test_Email_cannot_be_empty(self):

        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/addcustomerpage.php")
        User_Input = driver.find_element(By.XPATH, "//body/table[@class='layout']/tbody/tr/td[@colspan='2']/table[@border='0']/tbody/tr[12]/td[2]/input[1]")
        User_Input.send_keys(Keys.TAB)
        error_message = driver.find_element(By.XPATH, "//label[@id='message9']").text
        self.assertEqual("Email ID must not be blank", error_message, "Error message does not match")
        time.sleep(1)

    # Test case: Verify that email must be in correct format
    def test_Email_must_be_in_correct_format(self):

        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/addcustomerpage.php")
        User_Input = driver.find_element(By.XPATH, "//body/table[@class='layout']/tbody/tr/td[@colspan='2']/table[@border='0']/tbody/tr[12]/td[2]/input[1]")
        User_Input.send_keys("guru99@gmail")
        error_message = driver.find_element(By.XPATH, "//label[@id='message9']").text
        self.assertEqual("Email-ID is not valid", error_message, "Error message does not match")
        time.sleep(1)

        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/addcustomerpage.php")
        User_Input = driver.find_element(By.XPATH, "//body/table[@class='layout']/tbody/tr/td[@colspan='2']/table[@border='0']/tbody/tr[12]/td[2]/input[1]")
        User_Input.send_keys("guru99")
        error_message = driver.find_element(By.XPATH, "//label[@id='message9']").text
        self.assertEqual("Email-ID is not valid", error_message, "Error message does not match")
        time.sleep(1)

        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/addcustomerpage.php")
        User_Input = driver.find_element(By.XPATH, "//body/table[@class='layout']/tbody/tr/td[@colspan='2']/table[@border='0']/tbody/tr[12]/td[2]/input[1]")
        User_Input.send_keys("Guru99@")
        error_message = driver.find_element(By.XPATH, "//label[@id='message9']").text
        self.assertEqual("Email-ID is not valid", error_message, "Error message does not match")
        time.sleep(1)

        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/addcustomerpage.php")
        User_Input = driver.find_element(By.XPATH, "//body/table[@class='layout']/tbody/tr/td[@colspan='2']/table[@border='0']/tbody/tr[12]/td[2]/input[1]")
        User_Input.send_keys("guru99@gmail.")
        error_message = driver.find_element(By.XPATH, "//label[@id='message9']").text
        self.assertEqual("Email-ID is not valid", error_message, "Error message does not match")
        time.sleep(1)

        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/addcustomerpage.php")
        User_Input = driver.find_element(By.XPATH, "//body/table[@class='layout']/tbody/tr/td[@colspan='2']/table[@border='0']/tbody/tr[12]/td[2]/input[1]")
        User_Input.send_keys("guru99gmail.com")
        error_message = driver.find_element(By.XPATH, "//label[@id='message9']").text
        self.assertEqual("Email-ID is not valid", error_message, "Error message does not match")
        time.sleep(1)

    # Test case: Verify that email cannot have space
    # Broken
    def test_Email_cannot_have_space(self):
        
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/addcustomerpage.php")
        User_Input = driver.find_element(By.XPATH, "//body/table[@class='layout']/tbody/tr/td[@colspan='2']/table[@border='0']/tbody/tr[12]/td[2]/input[1]")
        User_Input.send_keys(" ")
        error_message = driver.find_element(By.XPATH, "//label[@id='message9']").text
        self.assertEqual("Email-ID is not valid", error_message, "Error message does not match")
        time.sleep(1)

    # Test case: Verify that password cannot be empty
    def test_Password_cannot_be_empty(self):
    
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/addcustomerpage.php")
        User_Input = driver.find_element(By.XPATH, "//body/table[@class='layout']/tbody/tr/td[@colspan='2']/table[@border='0']/tbody/tr[12]/td[2]/input[1]")
        User_Input.send_keys(Keys.TAB)
        error_message = driver.find_element(By.XPATH, "//label[@id='message18']").text
        self.assertEqual("Password must not be blank", error_message, "Error message does not match")
        time.sleep(1)

    # Test case: Verify that customer ID cannot be empty        
    def test_Customer_id_cannot_be_empty(self):

        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/EditCustomer.php")
        User_Input = driver.find_element(By.XPATH, "//input[@type='text']")
        User_Input.send_keys(Keys.TAB)
        error_message = driver.find_element(By.XPATH, "//label[@id='message14']").text
        self.assertEqual("Customer ID is required", error_message, "Error message does not match")
        time.sleep(1)

    # Test case: Verify that customer ID must be numeric
    def test_Customer_id_must_be_numeric(self):

        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/EditCustomer.php")
        User_Input = driver.find_element(By.XPATH, "//input[@type='text']")
        User_Input.send_keys("1234Acc")
        error_message = driver.find_element(By.XPATH, "//label[@id='message14']").text
        self.assertEqual("Characters are not allowed", error_message, "Error message does not match")
        time.sleep(1)

        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/EditCustomer.php")
        User_Input = driver.find_element(By.XPATH, "//input[@type='text']")
        User_Input.send_keys("Acc123")
        error_message = driver.find_element(By.XPATH, "//label[@id='message14']").text
        self.assertEqual("Characters are not allowed", error_message, "Error message does not match")
        time.sleep(1)
        
    # tearDownClass method to quit the browser
    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
#  Author: Jianahu Zhang
#  ID: 100900428
#  File: test_finalproject.py
#  Date: 08.08.2023
#  Description: This Selenium program will open the demo bank web page and register account .
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException

class TestBankApplication(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://demo.guru99.com/V4/index.php")

    def tearDown(self):
        self.driver.quit()

    def login(self, username, password):
        user_input = self.driver.find_element(By.NAME, "uid")
        password_input = self.driver.find_element(By.NAME, "password")
        login_button = self.driver.find_element(By.NAME, "btnLogin")

        user_input.send_keys("mngr517723")
        password_input.send_keys("jysEseh")
        login_button.click()

    def navigate_to_edit_customer(self):
        self.driver.find_element(By.LINK_TEXT, "Edit Customer").click()

    # --- Edit Customer Module ---

    def test_edit_customer_special_character_customer_id(self):
        self.login("mngr517723", "jysEseh")
        self.navigate_to_edit_customer()

        customer_id_input = self.driver.find_element(By.NAME, "cusid")
        customer_id_input.send_keys("123!@#")
        submit_button = self.driver.find_element(By.NAME, "AccSubmit")
        submit_button.click()

        try:
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            alert.dismiss()  # Dismiss the alert
            self.assertEqual("Special characters are not allowed", alert_text)
        except NoAlertPresentException:
            self.fail("No alert present")

    def test_edit_customer_valid_customer_id(self):
        self.login("mngr517723", "jysEseh")
        self.navigate_to_edit_customer()

        customer_id_input = self.driver.find_element(By.NAME, "cusid")
        customer_id_input.send_keys("86232")
        submit_button = self.driver.find_element(By.NAME, "AccSubmit")
        submit_button.click()

        success_message = self.driver.find_element(By.CLASS_NAME, "heading3")
        self.assertEqual("Edit Customer", success_message.text)

    def test_edit_customer_empty_address(self):
        self.login("mngr517723", "jysEseh")
        self.navigate_to_edit_customer()

        self.driver.find_element(By.NAME, "cusid").send_keys("86232")
        self.driver.find_element(By.NAME, "AccSubmit").click()

        self.driver.find_element(By.NAME, "addr").send_keys(Keys.TAB)
        error_message = self.driver.find_element(By.ID, "message3")
        self.assertEqual("Address Field must be blank", error_message.text)

    def test_edit_customer_empty_city(self):
        self.login("mngr517723", "jysEseh")
        self.navigate_to_edit_customer()

        self.driver.find_element(By.NAME, "cusid").send_keys("86232")
        self.driver.find_element(By.NAME, "AccSubmit").click()

        self.driver.find_element(By.NAME, "city").send_keys(Keys.TAB)
        error_message = self.driver.find_element(By.ID, "message3")
        self.assertEqual('', error_message.text)

    def test_edit_customer_numeric_city(self):
        self.login("mngr517723", "jysEseh")
        self.navigate_to_edit_customer()

        self.driver.find_element(By.NAME, "cusid").send_keys("86232")
        self.driver.find_element(By.NAME, "AccSubmit").click()

        self.driver.find_element(By.NAME, "city").send_keys("1234")
        error_message = self.driver.find_element(By.ID, "message4")
        self.assertEqual("Numbers are allowed", error_message.text)

    def test_edit_customer_special_character_city(self):
        self.login("mngr517723", "jysEseh")
        self.navigate_to_edit_customer()

        self.driver.find_element(By.NAME, "cusid").send_keys("86232")
        self.driver.find_element(By.NAME, "AccSubmit").click()

        self.driver.find_element(By.NAME, "city").send_keys("City!@#")
        error_message = self.driver.find_element(By.ID, "message4")
        self.assertEqual("Special characters are not allowed", error_message.text)

    def test_edit_customer_empty_state(self):
        self.login("mngr517723", "jysEseh")
        self.navigate_to_edit_customer()

        self.driver.find_element(By.NAME, "cusid").send_keys("86232")
        self.driver.find_element(By.NAME, "AccSubmit").click()

        self.driver.find_element(By.NAME, "state").send_keys(Keys.TAB)
        error_message = self.driver.find_element(By.ID, "message4")
        self.assertEqual('', error_message.text)

    def test_edit_customer_numeric_state(self):
        self.login("mngr517723", "jysEseh")
        self.navigate_to_edit_customer()

        self.driver.find_element(By.NAME, "cusid").send_keys("86232")
        self.driver.find_element(By.NAME, "AccSubmit").click()

        self.driver.find_element(By.NAME, "state").send_keys("1234")
        error_message = self.driver.find_element(By.ID, "message5")
        self.assertEqual("Numbers are not allowed", error_message.text)

    def test_edit_customer_special_character_state(self):
        self.login("mngr517723", "jysEseh")
        self.navigate_to_edit_customer()

        self.driver.find_element(By.NAME, "cusid").send_keys("86232")
        self.driver.find_element(By.NAME, "AccSubmit").click()

        self.driver.find_element(By.NAME, "state").send_keys("State!@#")
        error_message = self.driver.find_element(By.ID, "message5")
        self.assertEqual("Special characters are not allowed", error_message.text)

    def test_edit_customer_non_numeric_pin(self):
        self.login("mngr517723", "jysEseh")
        self.navigate_to_edit_customer()

        customer_id_input = self.driver.find_element(By.NAME, "cusid")
        customer_id_input.send_keys("86232")
        submit_button = self.driver.find_element(By.NAME, "AccSubmit")
        submit_button.click()

        pin_input = self.driver.find_element(By.NAME, "pinno")
        pin_input.send_keys("1234PIN")
        submit_button = self.driver.find_element(By.NAME, "sub")
        submit_button.click()

        error_message = self.driver.find_element(By.ID, "message5")
        self.assertEqual("Characters are not allowed", error_message.text)

    def test_edit_customer_empty_pin(self):
        self.login("mngr517723", "jysEseh")
        self.navigate_to_edit_customer()

        self.driver.find_element(By.NAME, "cusid").send_keys("86232")
        self.driver.find_element(By.NAME, "AccSubmit").click()

        self.driver.find_element(By.NAME, "pinno").send_keys(Keys.TAB)
        error_message = self.driver.find_element(By.ID, "message6")
        print("Actual error message:", error_message.text)
        self.assertEqual("PIN Code must not be blank", error_message.text)
        

    def test_edit_customer_long_short_pin(self):
        self.login("mngr517723", "jysEseh")
        self.navigate_to_edit_customer()

        self.driver.find_element(By.NAME, "cusid").send_keys("86232")
        self.driver.find_element(By.NAME, "AccSubmit").click()

        self.driver.find_element(By.NAME, "pinno").send_keys("1234567")
        submit_button = self.driver.find_element(By.NAME, "sub")
        submit_button.click()

    # Wait for the error message to appear
        error_message = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "message6"))
        )
        self.assertEqual("PIN Code must have 6 Digits", error_message.text)

        self.driver.find_element(By.NAME, "pinno").clear()
        self.driver.find_element(By.NAME, "pinno").send_keys("123")
        submit_button.click()

    # Wait for the error message to appear
        error_message = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "message6"))
        )
        self.assertEqual("PIN Code must have 6 Digits", error_message.text)

    def test_edit_customer_special_character_pin(self):
        self.login("mngr517723", "jysEseh")
        self.navigate_to_edit_customer()

        self.driver.find_element(By.NAME, "cusid").send_keys("86232")
        self.driver.find_element(By.NAME, "AccSubmit").click()

        pin_input = self.driver.find_element(By.NAME, "pinno")
        pin_input.send_keys("!@#")
        submit_button = self.driver.find_element(By.NAME, "sub")
        submit_button.click()

        error_message = self.driver.find_element(By.ID, "message6")
        self.assertEqual("Special characters are not allowed", error_message.text)

    def test_edit_customer_empty_mobile_no(self):
        self.login("mngr517723", "jysEseh")
        self.navigate_to_edit_customer()

        self.driver.find_element(By.NAME, "cusid").send_keys("86232")
        self.driver.find_element(By.NAME, "AccSubmit").click()

        self.driver.find_element(By.NAME, "telephoneno").send_keys(Keys.TAB)
        error_message = self.driver.find_element(By.ID, "message7")
        self.assertEqual("Telephone no must not be blank", error_message.text)

    def test_edit_customer_special_character_mobile_no(self):
        self.login("mngr517723", "jysEseh")
        self.navigate_to_edit_customer()

        self.driver.find_element(By.NAME, "cusid").send_keys("86232")
        self.driver.find_element(By.NAME, "AccSubmit").click()

        mobile_no_input = self.driver.find_element(By.NAME, "telephoneno")
        mobile_no_input.send_keys("886636!@12")
        submit_button = self.driver.find_element(By.NAME, "sub")
        submit_button.click()

        error_message = self.driver.find_element(By.ID, "message7")
        self.assertEqual("Special characters are not allowed", error_message.text)

    def test_edit_customer_empty_email(self):
        self.login("mngr517723", "jysEseh")
        self.navigate_to_edit_customer()

        self.driver.find_element(By.NAME, "cusid").send_keys("86232")
        self.driver.find_element(By.NAME, "AccSubmit").click()

        self.driver.find_element(By.NAME, "emailid").send_keys(Keys.TAB)
        error_message = self.driver.find_element(By.ID, "message9")
        self.assertEqual("Email-ID is not valid", error_message.text)

    def test_edit_customer_invalid_email_format(self):
        self.login("mngr517723", "jysEseh")
        self.navigate_to_edit_customer()

        self.driver.find_element(By.NAME, "cusid").send_keys("86232")
        self.driver.find_element(By.NAME, "AccSubmit").click()

        email_input = self.driver.find_element(By.NAME, "emailid")
        email_input.send_keys("guru99@gmail")
        submit_button = self.driver.find_element(By.NAME, "sub")
        submit_button.click()

        error_message = self.driver.find_element(By.ID, "message9")
        self.assertEqual("Email-ID is not valid", error_message.text)

        email_input.clear()
        email_input.send_keys("guru99")
        submit_button.click()
        error_message = self.driver.find_element(By.ID, "message9")
        self.assertEqual("Email-ID is not valid", error_message.text)

        email_input.clear()
        email_input.send_keys("Guru99@")
        submit_button.click()
        error_message = self.driver.find_element(By.ID, "message9")
        self.assertEqual("Email-ID is not valid", error_message.text)

        email_input.clear()
        email_input.send_keys("gurugmail.com")
        submit_button.click()
        error_message = self.driver.find_element(By.ID, "message9")
        self.assertEqual("Email-ID is not valid", error_message.text)

    # --- Delete Account Module ---

    def navigate_to_delete_account(self):
        self.driver.find_element(By.LINK_TEXT, "Delete Account").click()

    def test_delete_account_empty_account_number(self):
        self.login("mngr517723", "jysEseh")
        self.navigate_to_delete_account()

        self.driver.find_element(By.NAME, "accountno").send_keys(Keys.TAB)
        account_number_error = self.driver.find_element(By.ID, "message2")
        self.assertEqual("Account Number must not be blank", account_number_error.text)

    def test_delete_account_numeric_account_number(self):
        self.login("mngr517723", "jysEseh")
        self.navigate_to_delete_account()

        account_number_input = self.driver.find_element(By.NAME, "accountno")
        account_number_input.send_keys("Acc123")
        submit_button = self.driver.find_element(By.NAME, "AccSubmit")
        submit_button.click()
        account_number_error = self.driver.find_element(By.ID, "message2")
        self.assertEqual("Characters are not allowed", account_number_error.text)

    def test_delete_account_special_character_account_number(self):
        self.login("mngr517723", "jysEseh")
        self.navigate_to_delete_account()

        account_number_input = self.driver.find_element(By.NAME, "accountno")
        account_number_input.send_keys("123!@#")
        submit_button = self.driver.find_element(By.NAME, "AccSubmit")
        submit_button.click()

        error_message = self.driver.find_element(By.ID, "message2")
        self.assertEqual("Special characters are not allowed", error_message.text)

    def test_delete_account_blank_space_account_number(self):
        self.login("mngr517723", "jysEseh")
        self.navigate_to_delete_account()

        account_number_input = self.driver.find_element(By.NAME, "accountno")
        account_number_input.send_keys("123 12")
        submit_button = self.driver.find_element(By.NAME, "AccSubmit")
        submit_button.click()

        error_message = self.driver.find_element(By.ID, "message2")
        self.assertEqual("Characters are not allowed", error_message.text)

    def test_delete_account_first_character_space_account_number(self):
        self.login("mngr517723", "jysEseh")
        self.navigate_to_delete_account()

        account_number_input = self.driver.find_element(By.NAME, "accountno")
        account_number_input.send_keys(" 123456")
        submit_button = self.driver.find_element(By.NAME, "AccSubmit")
        submit_button.click()

        error_message = self.driver.find_element(By.ID, "message2")
        self.assertEqual("First character cannot have space", error_message.text)

    def test_delete_account_valid_account_number(self):
        self.login("mngr517723", "jysEseh")
        self.navigate_to_delete_account()

        account_number_input = self.driver.find_element(By.NAME, "accountno")
        account_number_input.send_keys("125119")
        submit_button = self.driver.find_element(By.NAME, "AccSubmit")
        submit_button.click()

        try:
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            alert.accept()
            self.assertEqual("Do you really want to delete this Account?", alert_text)
        except NoAlertPresentException:
            self.fail("No alert found")

    def test_delete_account_invalid_account_number(self):
        self.login("mngr517723", "jysEseh")
        self.navigate_to_delete_account()

        account_number_input = self.driver.find_element(By.NAME, "accountno")
        account_number_input.send_keys("12345")
        submit_button = self.driver.find_element(By.NAME, "AccSubmit")
        submit_button.click()

        try:
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            alert.accept()
            error_message = self.driver.find_element(By.ID, "message10")
            self.assertEqual("Account does not exist", error_message.text)
        except NoAlertPresentException:
            self.fail("No alert found")

    # --- Balance Enquiry Module ---

    def navigate_to_balance_enquiry(self):
        self.driver.find_element(By.LINK_TEXT, "Balance Enquiry").click()

    def test_balance_enquiry_empty_account_number(self):
        self.login("mngr517723", "jysEseh")
        self.navigate_to_balance_enquiry()

        self.driver.find_element(By.NAME, "accountno").send_keys(Keys.TAB)
        account_number_error = self.driver.find_element(By.ID, "message2")
        self.assertEqual("Account Number must not be blank", account_number_error.text)

    def test_balance_enquiry_numeric_account_number(self):
        self.login("mngr517723", "jysEseh")
        self.navigate_to_balance_enquiry()

        account_number_input = self.driver.find_element(By.NAME, "accountno")
        account_number_input.send_keys("Acc123")
        submit_button = self.driver.find_element(By.NAME, "AccSubmit")
        submit_button.click()

        account_number_error = self.driver.find_element(By.ID, "message2")
        self.assertEqual("Characters are not allowed", account_number_error.text)

    def test_balance_enquiry_special_character_account_number(self):
        self.login("mngr517723", "jysEseh")
        self.navigate_to_balance_enquiry()

        account_number_input = self.driver.find_element(By.NAME, "accountno")
        account_number_input.send_keys("123!@#")
        submit_button = self.driver.find_element(By.NAME, "AccSubmit")
        submit_button.click()

        error_message = self.driver.find_element(By.ID, "message2")
        self.assertEqual("Special characters are not allowed", error_message.text)

    def test_balance_enquiry_first_character_space_account_number(self):
        self.login("mngr517723", "jysEseh")
        self.navigate_to_balance_enquiry()

        account_number_input = self.driver.find_element(By.NAME, "accountno")
        account_number_input.send_keys(" 123456")
        submit_button = self.driver.find_element(By.NAME, "AccSubmit")
        submit_button.click()

        try:
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            alert.accept()
            error_message = self.driver.find_element(By.ID, "message2")
            self.assertEqual("First character cannot have space", error_message.text)
        except NoAlertPresentException:
            self.fail("No alert found")

# if __name__ == "__main__":
#     unittest.main()

# Group7_Ajay_Zanibek_Jianshu_Hlib
# Author: Ajay Singh Ahir
# Date:06-08-2023
# I did test cases [All 8 from "Deleted Customer", All 16 from  "New Account" and 6 from "Edit Account"]
# Total 30 Test Cases.
import time
import unittest

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait


class TestDeleteCustomer(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://demo.guru99.com/V4/")
        self.login()

    def tearDown(self):
        self.driver.quit()

    def login(self):
        user_id_input = self.driver.find_element(By.NAME, "uid")
        password_input = self.driver.find_element(By.NAME, "password")
        login_button = self.driver.find_element(By.NAME, "btnLogin")

        user_id_input.send_keys("mngr517722")
        password_input.send_keys("qunygap")
        login_button.click()
# Test 1
    def test_delete_customer(self):
        # Click on Delete Customer Link
        delete_customer_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Delete Customer']"))
        )
        delete_customer_link.click()

        # Enter Customer ID and move focus away from the field using TAB
        customer_id_input = self.driver.find_element(By.NAME, "cusid")
        customer_id_input.clear()
        customer_id_input.send_keys(Keys.TAB)

        error_message = self.driver.find_element(By.XPATH, "//label[contains(text(),'Customer ID can not be blank')]").text
        self.assertEqual("Customer ID can not be blank", error_message, "Error message does not match")
        print("Test Case DC1: Passed")

# Test 2
    def test_customer_id_not_numeric(self):
        # Click on Delete Customer Link
        delete_customer_link = self.driver.find_element(By.XPATH, "//a[text()='Delete Customer']")
        delete_customer_link.click()

        # Enter Non-numeric character in Customer ID Field
        customer_id_input = self.driver.find_element(By.NAME, "cusid")
        customer_id_input.send_keys("Acc123")



        # Verify Expected Result - Error message "Characters are not allowed" must be shown
        error_message = self.driver.find_element(By.XPATH, "//label[contains(text(),'Characters are not allowed')]").text
        self.assertEqual("Characters are not allowed", error_message, "Error message does not match")
        print("Test Case DA2: Passed")

# Test 3
    def test_delete_customer(self):
        # Click on Delete Customer Link
        delete_customer_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Delete Customer']"))
        )
        delete_customer_link.click()

        # Enter Special Characters in Customer ID Field
        customer_id_input = self.driver.find_element(By.NAME, "cusid")
        customer_id_input.clear()
        customer_id_input.send_keys("123!@#")

        # Verify Expected Result - Error message "Special characters are not allowed" must be shown
        error_message = self.driver.find_element(By.XPATH, "//label[contains(text(),'Special characters are not allowed')]").text
        self.assertEqual("Special characters are not allowed", error_message, "Error message does not match")
        print("Test Case DC2: Passed")

# Test 4
    def test_delete_customer(self):
        # Click on Delete Customer Link
        delete_customer_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Delete Customer']"))
        )
        delete_customer_link.click()

        # Enter Customer ID with Blank Space
        customer_id_input = self.driver.find_element(By.NAME, "cusid")
        customer_id_input.clear()
        customer_id_input.send_keys("123 12")

        # Verify Expected Result - Error message "Characters are not allowed" must be shown
        error_message = self.driver.find_element(By.XPATH, "//label[contains(text(),'Characters are not allowed')]").text
        self.assertEqual("Characters are not allowed", error_message, "Error message does not match")
        print("Test Case DC3: Passed")

# Test 5
    def test_delete_customer(self):
        # Click on Delete Customer Link
        delete_customer_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Delete Customer']"))
        )
        delete_customer_link.click()

        # Enter Customer ID with First Character as Space
        customer_id_input = self.driver.find_element(By.NAME, "cusid")
        customer_id_input.clear()
        customer_id_input.send_keys(" 12345")

        # Verify Expected Result - Error message "First character cannot have space" must be shown
        error_message = self.driver.find_element(By.XPATH, "//label[contains(text(),'First character cannot have space')]").text
        self.assertEqual("First character cannot have space", error_message, "Error message does not match")
        print("Test Case DC5: Passed")

# Test 6
    def test_delete_customer_with_incorrect_id(self):
        # Click on Delete Customer Link
        delete_customer_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Delete Customer']"))
        )
        delete_customer_link.click()

        # Enter Incorrect Customer ID and Click on Submit Button
        customer_id_input = self.driver.find_element(By.NAME, "cusid")
        customer_id_input.clear()
        customer_id_input.send_keys("123456")

        submit_button = self.driver.find_element(By.NAME, "AccSubmit")
        submit_button.click()

        # Verify Expected Result - Error message "Customer does not exist!!" must be shown
        error_message = self.driver.find_element(By.XPATH, "//p[contains(text(),'Customer does not exist!!')]").text
        self.assertEqual("Customer does not exist!!", error_message, "Error message does not match")
        print("Test Case DC6: Passed")

# Test 7
    def test_delete_customer_with_correct_id(self):
        # Click on Delete Customer Link
        delete_customer_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Delete Customer']"))
        )
        delete_customer_link.click()

        # Enter Correct Customer ID and Click on Submit Button
        customer_id_input = self.driver.find_element(By.NAME, "cusid")
        customer_id_input.clear()
        customer_id_input.send_keys("123456")

        submit_button = self.driver.find_element(By.NAME, "AccSubmit")
        submit_button.click()

        time.sleep(2)

        # Handle the Confirmation Dialog
        try:
            alert = self.driver.switch_to.alert
            alert.accept()
            time.sleep(2)
            print("Confirmation dialog accepted.")
        except:
            print("No confirmation dialog found.")

        # Verify Expected Result - Check if the error message "Customer could not be deleted!! First delete all accounts of this customer then delete the customer" is shown after handling the dialog
        error_message = self.driver.find_element(By.XPATH, "//p[contains(text(),'Customer could not be deleted!! First delete all accounts of this customer then delete the customer')]").text
        self.assertEqual("Customer could not be deleted!! First delete all accounts of this customer then delete the customer", error_message, "Error message does not match")
        print("Test Case DC7: Passed")

# Test 8
    def test_reset_button(self):
        # Click on Delete Customer Link
        delete_customer_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Delete Customer']"))
        )
        delete_customer_link.click()

        # Enter any value in the Customer ID field
        customer_id_input = self.driver.find_element(By.NAME, "cusid")
        customer_id_input.send_keys("123456")

        # Click on the Reset button
        reset_button = self.driver.find_element(By.NAME, "res")
        reset_button.click()

        # Verify if the Customer ID field is reset
        customer_id_value = customer_id_input.get_attribute("value")
        self.assertEqual("", customer_id_value, "Customer ID field is not reset")
        print("Test Case DC8: Passed")




# # NEW ACCOUNT TEST CASES 
# Test 9
class BaseTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()  # You can use any other browser driver as needed
        cls.driver.get("http://demo.guru99.com/V4/")
        cls.login()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    @classmethod
    def login(cls):
        user_id_input = cls.driver.find_element(By.NAME, "uid")
        password_input = cls.driver.find_element(By.NAME, "password")
        login_button = cls.driver.find_element(By.NAME, "btnLogin")

        user_id_input.send_keys("mngr517722")
        password_input.send_keys("qunygap")
        login_button.click()

class TestNewAccount(BaseTest):
    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_customer_id_cannot_be_empty(self):
        # Click on New Account Link
        new_account_link = self.driver.find_element(By.XPATH, "//a[text()='New Account']")
        new_account_link.click()

        # Leave Customer ID field empty and Press TAB
        customer_id_input = self.driver.find_element(By.NAME, "cusid")
        customer_id_input.send_keys(Keys.TAB)

        # Verify Expected Result
        error_message = self.driver.find_element(By.XPATH, "//label[contains(text(),'Customer ID is required')]").text
        self.assertEqual("Customer ID is required", error_message, "Error message does not match")
        print("Test Case NA1: Passed")

# Test 10
    def test_customer_id_must_be_numeric(self):
        # Click on New Account Link
        new_account_link = self.driver.find_element(By.XPATH, "//a[text()='New Account']")
        new_account_link.click()

        # Enter character value in Customer ID field and Press TAB
        customer_id_input = self.driver.find_element(By.NAME, "cusid")
        customer_id_input.send_keys("1234Acc")
        customer_id_input.send_keys(Keys.TAB)

        # Verify Expected Result
        error_message = self.driver.find_element(By.XPATH, "//label[contains(text(),'Characters are not allowed')]").text
        self.assertEqual("Characters are not allowed", error_message, "Error message does not match")
        print("Test Case NA2: Passed")

# Test 11
    def test_customer_id_cannot_have_special_character(self):
        # Click on New Account Link
        new_account_link = self.driver.find_element(By.XPATH, "//a[text()='New Account']")
        new_account_link.click()

        # Enter Special Character in Customer ID field and Press TAB
        customer_id_input = self.driver.find_element(By.NAME, "cusid")
        customer_id_input.send_keys("123!@#")
        customer_id_input.send_keys(Keys.TAB)

        # Verify Expected Result
        error_message = self.driver.find_element(By.XPATH, "//label[contains(text(),'Special characters are not allowed')]").text
        self.assertEqual("Special characters are not allowed", error_message, "Error message does not match")
        print("Test Case NA3: Passed")

    # Test 12
    def test_customer_id_cannot_have_blank_space(self):
        # Click on New Account Link
        new_account_link = self.driver.find_element(By.XPATH, "//a[text()='New Account']")
        new_account_link.click()

        # Enter any value in Customer ID field with blank space and Press TAB
        customer_id_input = self.driver.find_element(By.NAME, "cusid")
        customer_id_input.send_keys("123 12")
        customer_id_input.send_keys(Keys.TAB)

        # Verify Expected Result
        error_message = self.driver.find_element(By.XPATH, "//label[contains(text(),'Characters are not allowed')]").text
        self.assertEqual("Characters are not allowed", error_message, "Error message does not match")
        print("Test Case NA4: Passed")

    # Test 13
    def test_first_character_cannot_have_space(self):
        # Click on New Account Link
        new_account_link = self.driver.find_element(By.XPATH, "//a[text()='New Account']")
        new_account_link.click()

        # Enter a space as the first character in Customer ID field and Press TAB
        customer_id_input = self.driver.find_element(By.NAME, "cusid")
        customer_id_input.send_keys(" ")
        customer_id_input.send_keys(Keys.TAB)

        # Verify Expected Result
        error_message = self.driver.find_element(By.XPATH, "//label[contains(text(),'First character cannot have space')]").text
        self.assertEqual("First character cannot have space", error_message, "Error message does not match")
        print("Test Case NA5: Passed")

# Test 14

class TestInitialDeposit(BaseTest):
    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_initial_deposit_cannot_be_empty(self):
        # Click on New Account Link
        new_account_link = self.driver.find_element(By.XPATH, "//a[text()='New Account']")
        new_account_link.click()

        # Enter Customer ID and Click on Submit Button
        customer_id_input = self.driver.find_element(By.NAME, "cusid")
        customer_id_input.send_keys("123456")

        # Enter Account Type
        account_type_input = self.driver.find_element(By.NAME, "selaccount")
        account_type_input.send_keys("Current")

        # Leave Initial Deposit field empty and Press TAB
        initial_deposit_input = self.driver.find_element(By.NAME, "inideposit")
        initial_deposit_input.send_keys(Keys.TAB)

        # Verify Expected Result
        error_message = self.driver.find_element(By.XPATH, "//label[contains(text(),'Initial Deposit must not be blank')]").text
        self.assertEqual("Initial Deposit must not be blank", error_message, "Error message does not match")
        print("Test Case NA6: Passed")

# Test 15
    def test_initial_deposit_must_be_numeric(self):
        # Click on New Account Link
        new_account_link = self.driver.find_element(By.XPATH, "//a[text()='New Account']")
        new_account_link.click()

        # Enter Customer ID and Click on Submit Button
        customer_id_input = self.driver.find_element(By.NAME, "cusid")
        customer_id_input.send_keys("123456")

        # Enter Account Type
        account_type_input = self.driver.find_element(By.NAME, "selaccount")
        account_type_input.send_keys("Current")

        # Enter character value in Initial Deposit Field
        initial_deposit_input = self.driver.find_element(By.NAME, "inideposit")
        initial_deposit_input.send_keys("1234Acc")

        # Verify Expected Result
        error_message = self.driver.find_element(By.XPATH, "//label[contains(text(),'Characters are not allowed')]").text
        self.assertEqual("Characters are not allowed", error_message, "Error message does not match")
        print("Test Case NA2: Passed")

    # Test 16

    def test_initial_deposit_cannot_have_special_character(self):
        # Click on New Account Link
        new_account_link = self.driver.find_element(By.XPATH, "//a[text()='New Account']")
        new_account_link.click()

        # Enter Customer ID and Click on Submit Button
        customer_id_input = self.driver.find_element(By.NAME, "cusid")
        customer_id_input.send_keys("123456")

        # Enter Account Type
        account_type_input = self.driver.find_element(By.NAME, "selaccount")
        account_type_input.send_keys("Current")

        # Enter Special Character In Initial Deposit Field
        initial_deposit_input = self.driver.find_element(By.NAME, "inideposit")
        initial_deposit_input.send_keys("123!@#")

        # Verify Expected Result
        error_message = self.driver.find_element(By.XPATH, "//label[contains(text(),'Special characters are not allowed')]").text
        self.assertEqual("Special characters are not allowed", error_message, "Error message does not match")
        print("Test Case NA3: Passed")


    # Test 17
    def test_initial_deposit_cannot_have_blank_space(self):
        # Click on New Account Link
        new_account_link = self.driver.find_element(By.XPATH, "//a[text()='New Account']")
        new_account_link.click()

        # Enter Customer ID and Click on Submit Button
        customer_id_input = self.driver.find_element(By.NAME, "cusid")
        customer_id_input.send_keys("123456")

        # Enter Account Type
        account_type_input = self.driver.find_element(By.NAME, "selaccount")
        account_type_input.send_keys("Current")

        # Initial Deposit cannot have Blank space
        initial_deposit_input = self.driver.find_element(By.NAME, "inideposit")
        initial_deposit_input.send_keys("123 12")

        # Verify Expected Result
        error_message = self.driver.find_element(By.XPATH, "//label[contains(text(),'Characters are not allowed')]").text
        self.assertEqual("Characters are not allowed", error_message, "Error message does not match")
        print("Test Case NA4: Passed")

    # Test 18
    def test_initial_deposit_first_character_cannot_be_space(self):
        # Click on New Account Link
        new_account_link = self.driver.find_element(By.XPATH, "//a[text()='New Account']")
        new_account_link.click()

        # Enter Customer ID and Click on Submit Button
        customer_id_input = self.driver.find_element(By.NAME, "cusid")
        customer_id_input.send_keys("123456")

        # Enter Account Type
        account_type_input = self.driver.find_element(By.NAME, "selaccount")
        account_type_input.send_keys("Current")

        # First Character cannot be space
        initial_deposit_input = self.driver.find_element(By.NAME, "inideposit")
        initial_deposit_input.send_keys(" 123")

        # Verify Expected Result
        error_message = self.driver.find_element(By.XPATH, "//label[contains(text(),'First character cannot have space')]").text
        self.assertEqual("First character cannot have space", error_message, "Error message does not match")
        print("Test Case NA5: Passed")

    # Test 19

class TestAccountTypeDropdown(BaseTest):
    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_account_type_dropdown_savings(self):
        # Click on New Account Link
        new_account_link = self.driver.find_element(By.XPATH, "//a[text()='New Account']")
        new_account_link.click()

        # Enter Customer ID
        customer_id_input = self.driver.find_element(By.NAME, "cusid")
        customer_id_input.send_keys("123456")

        # Select Account Type as "Savings"
        account_type_dropdown = Select(self.driver.find_element(By.NAME, "selaccount"))
        account_type_dropdown.select_by_visible_text("Savings")

        # Verify that "Savings" option is selected
        selected_option = account_type_dropdown.first_selected_option.text
        self.assertEqual("Savings", selected_option, "Savings option is not selected")
        print("Test Case NA7: Passed")

    # Test 20
    def test_account_type_dropdown_current(self):
        # Click on New Account Link
        new_account_link = self.driver.find_element(By.XPATH, "//a[text()='New Account']")
        new_account_link.click()

        # Enter Customer ID
        customer_id_input = self.driver.find_element(By.NAME, "cusid")
        customer_id_input.send_keys("123456")

        # Select Account Type as "Current"
        account_type_dropdown = Select(self.driver.find_element(By.NAME, "selaccount"))
        account_type_dropdown.select_by_visible_text("Current")

        # Verify that "Current" option is selected
        selected_option = account_type_dropdown.first_selected_option.text
        self.assertEqual("Current", selected_option, "Current option is not selected")
        print("Test Case NA8: Passed")

#  Test 21   

class TestResetButton(BaseTest):

    def test_reset_button(self):
        # Click on New Account Link
        new_account_link = self.driver.find_element(By.XPATH, "//a[text()='New Account']")
        new_account_link.click()

        # Enter Customer ID and Initial Deposit
        customer_id_input = self.driver.find_element(By.NAME, "cusid")
        customer_id_input.send_keys("qwer")

        initial_deposit_input = self.driver.find_element(By.NAME, "inideposit")
        initial_deposit_input.send_keys("123456")

        # Click on Reset button
        reset_button = self.driver.find_element(By.NAME, "reset")
        reset_button.click()

        # Verify that Customer ID and Initial Deposit fields are reset
        self.assertEqual("", customer_id_input.get_attribute("value"), "Customer ID is not reset")
        self.assertEqual("", initial_deposit_input.get_attribute("value"), "Initial Deposit is not reset")
        print("Test Case NA9: Passed")

# Test 22

class TestSubmitButton(BaseTest):

    def test_submit_button_with_incorrect_id(self):
        # Click on New Account Link
        new_account_link = self.driver.find_element(By.XPATH, "//a[text()='New Account']")
        new_account_link.click()

        # Enter Incorrect Customer ID
        customer_id_input = self.driver.find_element(By.NAME, "cusid")
        customer_id_input.send_keys("123456")

        # Click on Submit button
        submit_button = self.driver.find_element(By.NAME, "submit")
        submit_button.click()

        # Verify Expected Result - Check if the error message "Customer does not exist!!" is shown
        error_message = self.driver.find_element(By.XPATH, "//label[contains(text(),'Customer does not exist!!')]").text
        self.assertEqual("Customer does not exist!!", error_message, "Error message does not match")
        print("Test Case NA10: Passed")

    # Test 23

    def test_submit_button_with_correct_id_and_amount(self):
        # Click on New Account Link
        new_account_link = self.driver.find_element(By.XPATH, "//a[text()='New Account']")
        new_account_link.click()

        # Enter Correct Customer ID and amount
        customer_id_input = self.driver.find_element(By.NAME, "cusid")
        customer_id_input.send_keys("100896804")

        initial_deposit_input = self.driver.find_element(By.NAME, "inideposit")
        initial_deposit_input.send_keys("500")

        # Click on Submit button
        submit_button = self.driver.find_element(By.NAME, "submit")
        submit_button.click()

        # Verify Expected Result - Check if the success message "Account generated successfully" is shown
        success_message = self.driver.find_element(By.XPATH, "//p[contains(text(),'Account generated successfully')]").text
        self.assertEqual("Account generated successfully", success_message, "Success message does not match")
        print("Test Case NA11: Passed")


    # Test 24


class TestContinueHyperlink(BaseTest):
    # Other test methods...

    def test_continue_hyperlink_after_account_creation(self):
        # Click on New Account Link
        new_account_link = self.driver.find_element(By.XPATH, "//a[text()='New Account']")
        new_account_link.click()

        # Enter Correct Customer ID and amount
        customer_id_input = self.driver.find_element(By.NAME, "cusid")
        customer_id_input.send_keys("100896804")

        initial_deposit_input = self.driver.find_element(By.NAME, "inideposit")
        initial_deposit_input.send_keys("1000")

        # Click on Submit button
        submit_button = self.driver.find_element(By.NAME, "submit")
        submit_button.click()
        
        # Verify Expected Result - Check if the success message "Account generated successfully" is shown
        success_message = self.driver.find_element(By.XPATH, "//p[contains(text(),'Account generated successfully')]").text
        self.assertEqual("Account generated successfully", success_message, "Success message does not match")

        # Click on the Continue hyperlink
        continue_link = self.driver.find_element(By.XPATH, "//a[text()='Continue']")
        continue_link.click()

        # Verify if the page navigates to the home page
        # Check for a flickering message or manager ID to confirm the home page
        try:
            # Wait for the manager ID element to be visible (you can adjust the timeout as needed)
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//td[text()='Manger Id : mngr517722']")))
            print("Test Case NA12: Passed - Navigated to home page")
        except TimeoutException:
            # If manager ID element is not found, check for flickering message (if any)
            try:
                self.driver.find_element(By.XPATH, "//div[contains(text(),'Welcome')]")
                print("Test Case NA12: Passed - Navigated to home page")
            except NoSuchElementException:
                print("Test Case NA12: Failed - Home page not found")



# EDIT ACCOUNT (6 TESTCASES FROM TOP)
# Test 25

class TestEditAccount(BaseTest):
    # Other test methods...

    def test_account_number_cannot_be_empty(self):
        # Click on Edit Account Link
        edit_account_link = self.driver.find_element(By.XPATH, "//a[text()='Edit Account']")
        edit_account_link.click()

        # Leave Account Number field empty and Press TAB
        account_number_input = self.driver.find_element(By.NAME, "accountno")
        account_number_input.send_keys(Keys.TAB)

        # Verify Expected Result
        error_message = self.driver.find_element(By.XPATH, "//label[contains(text(),'Account Number must not be empty')]").text
        self.assertEqual("Account Number must not be empty", error_message, "Error message does not match")
        print("Test Case EA1: Passed")

    # Test 26
    def test_account_number_must_be_numeric(self):
        # Click on Edit Account Link
        edit_account_link = self.driver.find_element(By.XPATH, "//a[text()='Edit Account']")
        edit_account_link.click()

        # Enter character value in Account Number field
        account_number_input = self.driver.find_element(By.NAME, "accountno")
        account_number_input.clear()
        account_number_input.send_keys("1234Acc")

        # Verify Expected Result
        error_message = self.driver.find_element(By.XPATH, "//label[contains(text(),'Characters are not allowed')]").text
        self.assertEqual("Characters are not allowed", error_message, "Error message does not match")
        print("Test Case EA2: Passed")


    # Test 27
    def test_account_number_cannot_have_special_character(self):
        # Click on Edit Account Link
        edit_account_link = self.driver.find_element(By.XPATH, "//a[text()='Edit Account']")
        edit_account_link.click()

        # Enter Special Character In Account Number field
        account_number_input = self.driver.find_element(By.NAME, "accountno")
        account_number_input.clear()
        account_number_input.send_keys("123!@#")

        # Verify Expected Result
        error_message = self.driver.find_element(By.XPATH, "//label[contains(text(),'Special characters are not allowed')]").text
        self.assertEqual("Special characters are not allowed", error_message, "Error message does not match")
        print("Test Case EA3: Passed")

    # Test 28

    def test_account_number_cannot_have_blank_space(self):
        # Click on Edit Account Link
        edit_account_link = self.driver.find_element(By.XPATH, "//a[text()='Edit Account']")
        edit_account_link.click()

        # Enter Account Number with blank space
        account_number_input = self.driver.find_element(By.NAME, "accountno")
        account_number_input.clear()
        account_number_input.send_keys("123 12")

        # Verify Expected Result
        error_message = self.driver.find_element(By.XPATH, "//label[contains(text(),'Characters are not allowed')]").text
        self.assertEqual("Characters are not allowed", error_message, "Error message does not match")
        print("Test Case EA4: Passed")

    # Test 29

    def test_first_character_cannot_be_space(self):
        # Click on Edit Account Link
        edit_account_link = self.driver.find_element(By.XPATH, "//a[text()='Edit Account']")
        edit_account_link.click()

        # Enter Account Number with first character as space
        account_number_input = self.driver.find_element(By.NAME, "accountno")
        account_number_input.clear()
        account_number_input.send_keys(" 12345")

        # Verify Expected Result
        error_message = self.driver.find_element(By.XPATH, "//label[contains(text(),'First character cannot have space')]").text
        self.assertEqual("First character cannot have space", error_message, "Error message does not match")
        print("Test Case EA5: Passed")

    # Test 30
    def test_submit_button_with_valid_account_number(self):
        # Click on Edit Account Link
        edit_account_link = self.driver.find_element(By.XPATH, "//a[text()='Edit Account']")
        edit_account_link.click()

        # Enter a valid Account Number
        account_number_input = self.driver.find_element(By.NAME, "accountno")
        account_number_input.send_keys("100896804")

        # Click on Submit button
        submit_button = self.driver.find_element(By.NAME, "AccSubmit")
        submit_button.click()

        # Verify if the page redirects to the Edit Account Form
        # Check for any element present on the Edit Account Form to confirm the redirection
        try:
            # Wait for the "Account Type" dropdown to be visible (you can adjust the timeout as needed)
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "selaccount")))
            print("Test Case EA6: Passed - Redirected to Edit Account Form")
        except TimeoutException:
            print("Test Case EA6: Failed - Edit Account Form not found")

# if __name__ == "__main__":
#     unittest.main()

#  Author: Zhanibek Kapen
#  ID: 100861891
#  File: testsuite.py
#  Date: 08.08.2023
#  Description: This Selenium program will open the browser and register account .
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
import HtmlTestRunner
import time

class testSUITE(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()

    def testcase_07_edit_account(self):
        driver = self.driver    
        driver.get("https://demo.guru99.com/V4/")   
        # Edit Account. Test Case 7
        # Login to account

        login = driver.find_element("name", "uid")
        login.clear()
        login.send_keys("mngr519284")
        password= driver.find_element("name", "password")
        password.clear()
        password.send_keys("yzajanU")
        driver.find_element(By.XPATH, "//tbody/tr[3]/td[2]/input[1]").click()
        # Start of the Test Case
        driver.find_element(By.XPATH, "//a[contains(text(),'Edit Account')]").click()
        account_number= driver.find_element(By.XPATH, "//tbody/tr[6]/td[2]/input[1]")
        account_number.send_keys("12345")
        account_number= driver.find_element(By.XPATH, "//tbody/tr[11]/td[2]/input[1]").click()
        alert = driver.switch_to.alert
        error_message = alert.text
        self.assertEqual(error_message, "Account does not exist")


    def testcase_08_edit_account(self):
        driver = self.driver    
        driver.get("https://demo.guru99.com/V4/")   
        # Edit Account. Test Case 8
        # Login to account

        login = driver.find_element("name", "uid")
        login.clear()
        login.send_keys("mngr519284")
        password= driver.find_element("name", "password")
        password.clear()
        password.send_keys("yzajanU")
        driver.find_element(By.XPATH, "//tbody/tr[3]/td[2]/input[1]").click()
        # Start of the Test Case
        driver.find_element(By.XPATH, "//a[contains(text(),'Edit Account')]").click()
        account_number= driver.find_element(By.XPATH, "//tbody/tr[6]/td[2]/input[1]")
        account_number.send_keys("qwer 123456")
        account_number= driver.find_element(By.XPATH, "//tbody/tr[11]/td[2]/input[2]").click()
        error_message = driver.find_element(By.XPATH, "//tbody/tr[6]/td[2]/input[1]").text
        self.assertEqual("", error_message, "Error message does not match")

    def testacase_05_balance_enquiry(self):
        driver = self.driver    
        driver.get("https://demo.guru99.com/V4/")   
        #  Balance Enquiry. Test Case 5
        # Login to account

        login = driver.find_element("name", "uid")
        login.clear()
        login.send_keys("mngr519284")
        password= driver.find_element("name", "password")
        password.clear()
        password.send_keys("yzajanU")
        driver.find_element(By.XPATH, "//tbody/tr[3]/td[2]/input[1]").click()
        # Start of the Test Case
        driver.find_element(By.XPATH, "//a[contains(text(),'Balance Enquiry')]").click()
        account_number= driver.find_element(By.XPATH, "//tbody/tr[6]/td[2]/input[1]")
        account_number.send_keys("125074")
        driver.find_element(By.XPATH, "//tbody/tr[11]/td[2]/input[1]").click()  
        # The test case fails. It suppose to show up page with table, but the page doesn't work. Since we didn't cover this type of errors, I couldn't write the code for this error.


    
    def testacase_06_balance_enquiry(self):
        driver = self.driver    
        driver.get("https://demo.guru99.com/V4/")   
        # Balance Enquiry. Test Case 6
        # Login to account

        login = driver.find_element("name", "uid")
        login.clear()
        login.send_keys("mngr519284")
        password= driver.find_element("name", "password")
        password.clear()
        password.send_keys("yzajanU")
        driver.find_element(By.XPATH, "//tbody/tr[3]/td[2]/input[1]").click()
        # Start of the Test Case
        driver.find_element(By.XPATH, "//a[contains(text(),'Balance Enquiry')]").click()
        account_number= driver.find_element(By.XPATH, "//tbody/tr[6]/td[2]/input[1]")
        account_number.send_keys("12345")
        driver.find_element(By.XPATH, "//tbody/tr[11]/td[2]/input[1]").click()
        alert = driver.switch_to.alert
        error_message = alert.text
        self.assertEqual(error_message, "Account does not exist")
        time.sleep(2)

    def testacase_07_balance_enquiry(self):
        driver = self.driver    
        driver.get("https://demo.guru99.com/V4/")   
        # Balance Enquiry. Test Case 7
        # Login to account

        login = driver.find_element("name", "uid")
        login.clear()
        login.send_keys("mngr519284")
        password= driver.find_element("name", "password")
        password.clear()
        password.send_keys("yzajanU")
        driver.find_element(By.XPATH, "//tbody/tr[3]/td[2]/input[1]").click()
        # Start of the Test Case
        driver.find_element(By.XPATH, "//a[contains(text(),'Balance Enquiry')]").click()
        account_number= driver.find_element(By.XPATH, "//tbody/tr[6]/td[2]/input[1]")
        account_number.send_keys("qwer 123456")
        driver.find_element(By.XPATH, "//tbody/tr[11]/td[2]/input[2]").click()
        error_message = driver.find_element(By.XPATH, "//tbody/tr[6]/td[2]/input[1]").text
        self.assertEqual("", error_message, "Error message does not match")

    def testacase_01_mini_statement(self):
        driver = self.driver    
        driver.get("https://demo.guru99.com/V4/")   

        # Mini Statement. TestCase 1
        # Login to account

        login = driver.find_element("name", "uid")
        login.clear()
        login.send_keys("mngr519284")
        password= driver.find_element("name", "password")
        password.clear()
        password.send_keys("yzajanU")
        driver.find_element(By.XPATH, "//tbody/tr[3]/td[2]/input[1]").click()
        # Start of the Test Case
        driver.find_element(By.XPATH, "//a[contains(text(),'Mini Statement')]").click()
        account_number= driver.find_element(By.XPATH, "//tbody/tr[6]/td[2]/input[1]")
        account_number.send_keys(Keys.TAB)  
        error_message = driver.find_element(By.XPATH, "//label[@id='message2']").text
        self.assertEqual(" Account Number must not be blank", error_message, "Error message does not match")

    def testacase_02_01_mini_statement(self):
        driver = self.driver    
        driver.get("https://demo.guru99.com/V4/")   
        # Mini Statement. TestCase 2.1
        # Login to account

        login = driver.find_element("name", "uid")
        login.clear()
        login.send_keys("mngr519284")
        password= driver.find_element("name", "password")
        password.clear()
        password.send_keys("yzajanU")
        driver.find_element(By.XPATH, "//tbody/tr[3]/td[2]/input[1]").click()
        # Start of the Test Case
        driver.find_element(By.XPATH, "//a[contains(text(),'Mini Statement')]").click()
        account_number= driver.find_element(By.XPATH, "//tbody/tr[6]/td[2]/input[1]")
        account_number.send_keys("Acc123")
        error_message = driver.find_element(By.XPATH, "//label[@id='message2']").text
        self.assertEqual("Characters are not allowed", error_message, "Error message does not match")
    
    def testacase_02_02_mini_statement(self):
        driver = self.driver    
        driver.get("https://demo.guru99.com/V4/")   
        # Mini Statement. TestCase 2.2
        # Login to account

        login = driver.find_element("name", "uid")
        login.clear()
        login.send_keys("mngr519284")
        password= driver.find_element("name", "password")
        password.clear()
        password.send_keys("yzajanU")
        driver.find_element(By.XPATH, "//tbody/tr[3]/td[2]/input[1]").click()
        # Start of the Test Case
        driver.find_element(By.XPATH, "//a[contains(text(),'Mini Statement')]").click()
        account_number= driver.find_element(By.XPATH, "//tbody/tr[6]/td[2]/input[1]")
        account_number.send_keys("1234")
        error_message = driver.find_element(By.XPATH, "//label[@id='message2']").text
        self.assertEqual("Characters are not allowed", error_message, "Error message does not match")

    
    def testacase_03_01_mini_statement(self):
        driver = self.driver    
        driver.get("https://demo.guru99.com/V4/")  
        # Mini Statement. TestCase 3.1
        # Login to account

        login = driver.find_element("name", "uid")
        login.clear()
        login.send_keys("mngr519284")
        password= driver.find_element("name", "password")
        password.clear()
        password.send_keys("yzajanU")
        driver.find_element(By.XPATH, "//tbody/tr[3]/td[2]/input[1]").click()
        # Start of the Test Case
        driver.find_element(By.XPATH, "//a[contains(text(),'Mini Statement')]").click()
        account_number= driver.find_element(By.XPATH, "//tbody/tr[6]/td[2]/input[1]")
        account_number.send_keys("123!@#")
        error_message = driver.find_element(By.XPATH, "//label[@id='message2']").text 
        self.assertEqual("Special characters are not allowed", error_message, "Error message does not match")

    
    def testacase_03_02_mini_statement(self):
        driver = self.driver    
        driver.get("https://demo.guru99.com/V4/")   
        # Mini Statement. TestCase 3.2
        # Login to account

        login = driver.find_element("name", "uid")
        login.clear()
        login.send_keys("mngr519284")
        password= driver.find_element("name", "password")
        password.clear()
        password.send_keys("yzajanU")
        driver.find_element(By.XPATH, "//tbody/tr[3]/td[2]/input[1]").click()
        # Start of the Test Case
        driver.find_element(By.XPATH, "//a[contains(text(),'Mini Statement')]").click()
        account_number= driver.find_element(By.XPATH, "//tbody/tr[6]/td[2]/input[1]")
        account_number.send_keys("!@#")
        error_message = driver.find_element(By.XPATH, "//label[@id='message2']").text 
        self.assertEqual("Special characters are not allowed", error_message, "Error message does not match")
    
    def testacase_04_mini_statement(self):
        driver = self.driver    
        driver.get("https://demo.guru99.com/V4/")   
        # Mini Statement. TestCase 4
        # Login to account  
        login = driver.find_element("name", "uid")
        login.clear()
        login.send_keys("mngr519284")
        password= driver.find_element("name", "password")
        password.clear()
        password.send_keys("yzajanU")
        driver.find_element(By.XPATH, "//tbody/tr[3]/td[2]/input[1]").click()
        # Start of the Test Case
        driver.find_element(By.XPATH, "//a[contains(text(),'Mini Statement')]").click()
        account_number= driver.find_element(By.XPATH, "//tbody/tr[6]/td[2]/input[1]")
        account_number.send_keys("123 12")
        account_number.send_keys(Keys.TAB)
        error_message = driver.find_element(By.XPATH, "//label[@id='message2']").text 
        self.assertEqual("Characters are not allowed", error_message, "Error message does not match")
    
    def testacase_05_mini_statement(self):
        driver = self.driver    
        driver.get("https://demo.guru99.com/V4/")   
        # Mini Statement. TestCase 5
        # Login to account
        login = driver.find_element("name", "uid")
        login.clear()
        login.send_keys("mngr519284")
        password= driver.find_element("name", "password")
        password.clear()
        password.send_keys("yzajanU")
        driver.find_element(By.XPATH, "//tbody/tr[3]/td[2]/input[1]").click()
        # Start of the Test Case
        driver.find_element(By.XPATH, "//a[contains(text(),'Mini Statement')]").click()
        account_number= driver.find_element(By.XPATH, "//tbody/tr[6]/td[2]/input[1]")
        account_number.send_keys(Keys.SPACE)
        account_number.send_keys(Keys.TAB)
        error_message = driver.find_element(By.XPATH, "//label[@id='message2']").text 
        self.assertEqual("First character cannot have space" , error_message, "Error message does not match")
    
    def testacase_06_mini_statement(self):
        driver = self.driver    
        driver.get("https://demo.guru99.com/V4/")   
        # # Mini Statement. TestCase 6
        # # Login to account
        login = driver.find_element("name", "uid")
        login.clear()
        login.send_keys("mngr519284")
        password= driver.find_element("name", "password")
        password.clear()
        password.send_keys("yzajanU")
        driver.find_element(By.XPATH, "//tbody/tr[3]/td[2]/input[1]").click()
        # Start of the Test Case
        driver.find_element(By.XPATH, "//a[contains(text(),'Mini Statement')]").click()
        account_number= driver.find_element(By.XPATH, "//tbody/tr[6]/td[2]/input[1]")
        account_number.send_keys("125074")
        driver.find_element(By.XPATH, "//tbody/tr[11]/td[2]/input[1]").click()
        # The test case fails. It suppose to show up page with table, but the page doesn't work. Since we didn't cover this type of errors, I couldn't write the code for this error.
    
    def testacase_07_mini_statement(self):
        driver = self.driver    
        driver.get("https://demo.guru99.com/V4/")   
        # Mini Statement. TestCase 7
        # Login to account

        login = driver.find_element("name", "uid")
        login.clear()
        login.send_keys("mngr519284")
        password= driver.find_element("name", "password")
        password.clear()
        password.send_keys("yzajanU")
        driver.find_element(By.XPATH, "//tbody/tr[3]/td[2]/input[1]").click()
        # Start of the Test Case
        driver.find_element(By.XPATH, "//a[contains(text(),'Mini Statement')]").click()
        account_number= driver.find_element(By.XPATH, "//tbody/tr[6]/td[2]/input[1]")
        account_number.send_keys("12345")
        driver.find_element(By.XPATH, "//tbody/tr[11]/td[2]/input[1]").click()
        alert = driver.switch_to.alert
        error_message = alert.text
        self.assertEqual(error_message, "Account does not exist")
        alert.accept()  

    def testacase_08_mini_statement(self):
        driver = self.driver    
        driver.get("https://demo.guru99.com/V4/")   
        # Mini Statement. TestCase 8
        # Login to account

        login = driver.find_element("name", "uid")
        login.clear()
        login.send_keys("mngr519284")
        password= driver.find_element("name", "password")
        password.clear()
        password.send_keys("yzajanU")
        driver.find_element(By.XPATH, "//tbody/tr[3]/td[2]/input[1]").click()
        # Start of the Test Case
        driver.find_element(By.XPATH, "//a[contains(text(),'Mini Statement')]").click()
        account_number= driver.find_element(By.XPATH, "//tbody/tr[6]/td[2]/input[1]")
        account_number.send_keys("qwer 123456")
        driver.find_element(By.XPATH, "//tbody/tr[11]/td[2]/input[2]").click()
        error_message = driver.find_element(By.XPATH, "//tbody/tr[6]/td[2]/input[1]").text 
        self.assertEqual("" , error_message, "Error message does not match")

    def testcase_01_customized_statement(self):
        driver = self.driver    
        driver.get("https://demo.guru99.com/V4/")  
        # Customized Statement. TestCase 1
        # Login to account

        login = driver.find_element("name", "uid")
        login.clear()
        login.send_keys("mngr519284")
        password= driver.find_element("name", "password")
        password.clear()
        password.send_keys("yzajanU")
        driver.find_element(By.XPATH, "//tbody/tr[3]/td[2]/input[1]").click()
        # Start of the Test Case
        driver.find_element(By.XPATH, "//a[contains(text(),'Customised Statement')]").click()
        account_number= driver.find_element(By.XPATH, "//tbody/tr[6]/td[2]/input[1]")
        account_number.send_keys(Keys.TAB) 
        error_message = driver.find_element(By.XPATH, "//label[@id='message2']").text 
        self.assertEqual("Account Number must not be blank" , error_message, "Error message does not match")
    def testcase_02_01_customized_statement(self):
        driver = self.driver    
        driver.get("https://demo.guru99.com/V4/")   
        # Customized Statement. TestCase 2.1
        # Login to account

        login = driver.find_element("name", "uid")
        login.clear()
        login.send_keys("mngr519284")
        password= driver.find_element("name", "password")
        password.clear()
        password.send_keys("yzajanU")
        driver.find_element(By.XPATH, "//tbody/tr[3]/td[2]/input[1]").click()
        # Start of the Test Case
        driver.find_element(By.XPATH, "//a[contains(text(),'Customised Statement')]").click()
        account_number= driver.find_element(By.XPATH, "//tbody/tr[6]/td[2]/input[1]")
        account_number.send_keys("1234")
        # For this test case data, the entered data is invalid (doesn't shows up the error message it should)
        error_message = driver.find_element(By.XPATH, "//label[@id='message2']").text 
        self.assertEqual("Characters are not allowed" , error_message, "Error message does not match")
    def testcase_02_02_customized_statement(self):
        driver = self.driver    
        driver.get("https://demo.guru99.com/V4/")   
        # Customized Statement. TestCase 2.2
        # Login to account

        login = driver.find_element("name", "uid")
        login.clear()
        login.send_keys("mngr519284")
        password= driver.find_element("name", "password")
        password.clear()
        password.send_keys("yzajanU")
        driver.find_element(By.XPATH, "//tbody/tr[3]/td[2]/input[1]").click()
        # Start of the Test Case
        driver.find_element(By.XPATH, "//a[contains(text(),'Customised Statement')]").click()
        account_number= driver.find_element(By.XPATH, "//tbody/tr[6]/td[2]/input[1]")
        account_number.send_keys("Acc123")
        error_message = driver.find_element(By.XPATH, "//label[@id='message2']").text 
        self.assertEqual("Characters are not allowed" , error_message, "Error message does not match")
    def testcase_03_01_customized_statement(self):
        driver = self.driver    
        driver.get("https://demo.guru99.com/V4/")   
        # Customized Statement. TestCase 3.1
        # Login to account

        login = driver.find_element("name", "uid")
        login.clear()
        login.send_keys("mngr519284")
        password= driver.find_element("name", "password")
        password.clear()
        password.send_keys("yzajanU")
        driver.find_element(By.XPATH, "//tbody/tr[3]/td[2]/input[1]").click()
        # Start of the Test Case
        driver.find_element(By.XPATH, "//a[contains(text(),'Customised Statement')]").click()
        account_number= driver.find_element(By.XPATH, "//tbody/tr[6]/td[2]/input[1]")
        account_number.send_keys("123!@#")
        error_message = driver.find_element(By.XPATH, "//label[@id='message2']").text 
        self.assertEqual("Special characters are not allowed" , error_message, "Error message does not match")
    def testcase_03_02_customized_statement(self):
        driver = self.driver    
        driver.get("https://demo.guru99.com/V4/")   
        # Customized Statement. TestCase 3.2
        # Login to account

        login = driver.find_element("name", "uid")
        login.clear()
        login.send_keys("mngr519284")
        password= driver.find_element("name", "password")
        password.clear()
        password.send_keys("yzajanU")
        driver.find_element(By.XPATH, "//tbody/tr[3]/td[2]/input[1]").click()
        # Start of the Test Case
        driver.find_element(By.XPATH, "//a[contains(text(),'Customised Statement')]").click()
        account_number= driver.find_element(By.XPATH, "//tbody/tr[6]/td[2]/input[1]")
        account_number.send_keys("!@#")
        error_message = driver.find_element(By.XPATH, "//label[@id='message2']").text 
        self.assertEqual("Special characters are not allowed" , error_message, "Error message does not match")
    def testcase_04_customized_statement(self):
        driver = self.driver    
        driver.get("https://demo.guru99.com/V4/")   
        # Customized Statement. TestCase 4
        # Login to account

        login = driver.find_element("name", "uid")
        login.clear()
        login.send_keys("mngr519284")
        password= driver.find_element("name", "password")
        password.clear()
        password.send_keys("yzajanU")
        driver.find_element(By.XPATH, "//tbody/tr[3]/td[2]/input[1]").click()
        # Start of the Test Case
        driver.find_element(By.XPATH, "//a[contains(text(),'Customised Statement')]").click()
        account_number= driver.find_element(By.XPATH, "//tbody/tr[6]/td[2]/input[1]")
        account_number.send_keys("123 12")
        account_number.send_keys(Keys.TAB)
        error_message = driver.find_element(By.XPATH, "//label[@id='message2']").text 
        self.assertEqual("Characters are not allowed" , error_message, "Error message does not match")
    def testcase_05_customized_statement(self):
        driver = self.driver    
        driver.get("https://demo.guru99.com/V4/")  
        # # Customized Statement. TestCase 5
        # # Login to account

        login = driver.find_element("name", "uid")
        login.clear()
        login.send_keys("mngr519284")
        password= driver.find_element("name", "password")
        password.clear()
        password.send_keys("yzajanU")
        driver.find_element(By.XPATH, "//tbody/tr[3]/td[2]/input[1]").click()
        # Start of the Test Case
        driver.find_element(By.XPATH, "//a[contains(text(),'Customised Statement')]").click()
        account_number= driver.find_element(By.XPATH, "//tbody/tr[6]/td[2]/input[1]")
        account_number.send_keys(Keys.SPACE)
        account_number.send_keys(Keys.TAB)
        error_message = driver.find_element(By.XPATH, "//label[@id='message2']").text 
        self.assertEqual("First character cannot have space", error_message, "Error message does not match")
    def testcase_06_customized_statement(self):
        driver = self.driver    
        driver.get("https://demo.guru99.com/V4/")  
        # Customized Statement. TestCase 6
        # Login to account

        login = driver.find_element("name", "uid")
        login.clear()
        login.send_keys("mngr519284")
        password= driver.find_element("name", "password")
        password.clear()
        password.send_keys("yzajanU")
        driver.find_element(By.XPATH, "//tbody/tr[3]/td[2]/input[1]").click()
        # Start of the Test Case
        driver.find_element(By.XPATH, "//a[contains(text(),'Customised Statement')]").click()
        driver.find_element(By.XPATH, "//tbody/tr[7]/td[2]/input[1]").click()
        error_message = driver.find_element(By.XPATH, "//label[@id='message26']").text 
        self.assertEqual("From Date Field must not be blank", error_message, "Error message does not match")
    def testcase_07_customized_statement(self):
        driver = self.driver    
        driver.get("https://demo.guru99.com/V4/")  
        # Customized Statement. TestCase 7
        # Login to account

        login = driver.find_element("name", "uid")
        login.clear()
        login.send_keys("mngr519284")
        password= driver.find_element("name", "password")
        password.clear()
        password.send_keys("yzajanU")
        driver.find_element(By.XPATH, "//tbody/tr[3]/td[2]/input[1]").click()
        # Start of the Test Case
        driver.find_element(By.XPATH, "//a[contains(text(),'Customised Statement')]").click()
        driver.find_element(By.XPATH, "//tbody/tr[8]/td[2]/input[1]").click()
        error_message = driver.find_element(By.XPATH, "//label[@id='message27']").text 
        self.assertEqual("To Date Field must not be blank", error_message, "Error message does not match")
    def testcase_08_01_customized_statement(self):
        driver = self.driver    
        driver.get("https://demo.guru99.com/V4/")  
        # Customized Statement. TestCase 8.1
        # Login to account
        login = driver.find_element("name", "uid")
        login.clear()
        login.send_keys("mngr519284")
        password= driver.find_element("name", "password")
        password.clear()
        password.send_keys("yzajanU")
        driver.find_element(By.XPATH, "//tbody/tr[3]/td[2]/input[1]").click()
        # Start of the Test Case
        driver.find_element(By.XPATH, "//a[contains(text(),'Customised Statement')]").click()
        transaction = driver.find_element(By.XPATH, "//tbody/tr[9]/td[2]/input[1]")
        transaction.send_keys("1234")
        error_message = driver.find_element(By.XPATH, "//label[@id='message12']").text 
        self.assertEqual("Characters are not allowed", error_message, "Error message does not match")

    def testcase_08_02_customized_statement(self):
        driver = self.driver    
        driver.get("https://demo.guru99.com/V4/")  
        # # Customized Statement. TestCase 8.2
        # # Login to account

        login = driver.find_element("name", "uid")
        login.clear()
        login.send_keys("mngr519284")
        password= driver.find_element("name", "password")
        password.clear()
        password.send_keys("yzajanU")
        driver.find_element(By.XPATH, "//tbody/tr[3]/td[2]/input[1]").click()
        # Start of the Test Case
        driver.find_element(By.XPATH, "//a[contains(text(),'Customised Statement')]").click()
        transaction = driver.find_element(By.XPATH, "//tbody/tr[9]/td[2]/input[1]")
        transaction.send_keys("Acc123")
        error_message = driver.find_element(By.XPATH, "//label[@id='message12']").text 
        self.assertEqual("Characters are not allowed", error_message, "Error message does not match")
 
    def testcase_09_01_customized_statement(self):
        driver = self.driver    
        driver.get("https://demo.guru99.com/V4/")  
        # # Customized Statement. TestCase 9.1
        # # Login to account

        login = driver.find_element("name", "uid")
        login.clear()
        login.send_keys("mngr519284")
        password= driver.find_element("name", "password")
        password.clear()
        password.send_keys("yzajanU")
        driver.find_element(By.XPATH, "//tbody/tr[3]/td[2]/input[1]").click()
        # Start of the Test Case
        driver.find_element(By.XPATH, "//a[contains(text(),'Customised Statement')]").click()
        transaction = driver.find_element(By.XPATH, "//tbody/tr[9]/td[2]/input[1]")
        transaction.send_keys("123!@#")
        error_message = driver.find_element(By.XPATH, "//label[@id='message12']").text 
        self.assertEqual("Special characters are not allowed", error_message, "Error message does not match")
        
    def testcase_09_02_customized_statement(self):
        driver = self.driver    
        driver.get("https://demo.guru99.com/V4/")  
        # # Customized Statement. TestCase 9.1
        # # Login to account

        login = driver.find_element("name", "uid")
        login.clear()
        login.send_keys("mngr519284")
        password= driver.find_element("name", "password")
        password.clear()
        password.send_keys("yzajanU")
        driver.find_element(By.XPATH, "//tbody/tr[3]/td[2]/input[1]").click()
        # Start of the Test Case
        driver.find_element(By.XPATH, "//a[contains(text(),'Customised Statement')]").click()
        transaction = driver.find_element(By.XPATH, "//tbody/tr[9]/td[2]/input[1]")
        transaction.send_keys("!@#")
        error_message = driver.find_element(By.XPATH, "//label[@id='message12']").text 
        self.assertEqual("Special characters are not allowed", error_message, "Error message does not match")
         
    def testcase_10_customized_statement(self):
        driver = self.driver    
        driver.get("https://demo.guru99.com/V4/") 
        # Customized Statement. TestCase 10
        # Login to account
        login = driver.find_element("name", "uid")
        login.clear()
        login.send_keys("mngr519284")
        password= driver.find_element("name", "password")
        password.clear()
        password.send_keys("yzajanU")
        driver.find_element(By.XPATH, "//tbody/tr[3]/td[2]/input[1]").click()
        # Start of the Test Case
        driver.find_element(By.XPATH, "//a[contains(text(),'Customised Statement')]").click()
        transaction = driver.find_element(By.XPATH, "//tbody/tr[9]/td[2]/input[1]")
        transaction.send_keys("123 12")
        error_message = driver.find_element(By.XPATH, "//label[@id='message12']").text 
        self.assertEqual("Characters are not allowed", error_message, "Error message does not match")
         
    def testcase_11_customized_statement(self):
        driver = self.driver    
        driver.get("https://demo.guru99.com/V4/")
        # Customized Statement. TestCase 11
        # Login to account

        login = driver.find_element("name", "uid")
        login.clear()
        login.send_keys("mngr519284")
        password= driver.find_element("name", "password")
        password.clear()
        password.send_keys("yzajanU")
        driver.find_element(By.XPATH, "//tbody/tr[3]/td[2]/input[1]").click()
        # Start of the Test Case
        driver.find_element(By.XPATH, "//a[contains(text(),'Customised Statement')]").click()
        transaction = driver.find_element(By.XPATH, "//tbody/tr[9]/td[2]/input[1]")
        transaction.send_keys(Keys.SPACE)
        transaction.send_keys(Keys.TAB) 
        error_message = driver.find_element(By.XPATH, "//label[@id='message12']").text 
        self.assertEqual("Characters are not allowed", error_message, "Error message does not match")
         
    def testcase_12_01_customized_statement(self):
        driver = self.driver    
        driver.get("https://demo.guru99.com/V4/") 
        # # Customized Statement. TestCase 12.1
        # # Login to account

        login = driver.find_element("name", "uid")
        login.clear()
        login.send_keys("mngr519284")
        password= driver.find_element("name", "password")
        password.clear()
        password.send_keys("yzajanU")
        driver.find_element(By.XPATH, "//tbody/tr[3]/td[2]/input[1]").click()
        # Start of the Test Case
        driver.find_element(By.XPATH, "//a[contains(text(),'Customised Statement')]").click()
        transaction = driver.find_element(By.XPATH, "//tbody/tr[10]/td[2]/input[1]")
        transaction.send_keys("1234")
        error_message = driver.find_element(By.XPATH, "//label[@id='message13']").text 
        self.assertEqual("Characters are not allowed", error_message, "Error message does not match")
         
    def testcase_12_02_customized_statement(self):
        driver = self.driver    
        driver.get("https://demo.guru99.com/V4/") 
        # Customized Statement. TestCase 12.2
        # Login to account

        login = driver.find_element("name", "uid")
        login.clear()
        login.send_keys("mngr519284")
        password= driver.find_element("name", "password")
        password.clear()
        password.send_keys("yzajanU")
        driver.find_element(By.XPATH, "//tbody/tr[3]/td[2]/input[1]").click()
        # Start of the Test Case
        driver.find_element(By.XPATH, "//a[contains(text(),'Customised Statement')]").click()
        transaction = driver.find_element(By.XPATH, "//tbody/tr[10]/td[2]/input[1]")
        transaction.send_keys("Acc123")
        error_message = driver.find_element(By.XPATH, "//label[@id='message13']").text 
        self.assertEqual("Characters are not allowed", error_message, "Error message does not match")
                
    def testcase_13_01_customized_statement(self):
        driver = self.driver    
        driver.get("https://demo.guru99.com/V4/") 
        # Customized Statement. TestCase 13.1
        # Login to account

        login = driver.find_element("name", "uid")
        login.clear()
        login.send_keys("mngr519284")
        password= driver.find_element("name", "password")
        password.clear()
        password.send_keys("yzajanU")
        driver.find_element(By.XPATH, "//tbody/tr[3]/td[2]/input[1]").click()
        # Start of the Test Case
        driver.find_element(By.XPATH, "//a[contains(text(),'Customised Statement')]").click()
        transaction = driver.find_element(By.XPATH, "//tbody/tr[10]/td[2]/input[1]")
        transaction.send_keys("132!@#")
        error_message = driver.find_element(By.XPATH, "//label[@id='message13']").text 
        self.assertEqual("Special characters are not allowed", error_message, "Error message does not match")
         
    def testcase_13_02_customized_statement(self):
        driver = self.driver    
        driver.get("https://demo.guru99.com/V4/") 
        # Customized Statement. TestCase 13.2
        # Login to account

        login = driver.find_element("name", "uid")
        login.clear()
        login.send_keys("mngr519284")
        password= driver.find_element("name", "password")
        password.clear()
        password.send_keys("yzajanU")
        driver.find_element(By.XPATH, "//tbody/tr[3]/td[2]/input[1]").click()
        # Start of the Test Case
        driver.find_element(By.XPATH, "//a[contains(text(),'Customised Statement')]").click()
        transaction = driver.find_element(By.XPATH, "//tbody/tr[10]/td[2]/input[1]")
        transaction.send_keys("!@#")
        error_message = driver.find_element(By.XPATH, "//label[@id='message13']").text  
        self.assertEqual("Special characters are not allowed", error_message, "Error message does not match")
         
    def testcase_14_customized_statement(self):
        driver = self.driver    
        driver.get("https://demo.guru99.com/V4/")
        # Customized Statement. TestCase 14
        # Login to account

        login = driver.find_element("name", "uid")
        login.clear()
        login.send_keys("mngr519284")
        password= driver.find_element("name", "password")
        password.clear()
        password.send_keys("yzajanU")
        driver.find_element(By.XPATH, "//tbody/tr[3]/td[2]/input[1]").click()
        # Start of the Test Case
        driver.find_element(By.XPATH, "//a[contains(text(),'Customised Statement')]").click()
        transaction = driver.find_element(By.XPATH, "//tbody/tr[10]/td[2]/input[1]")
        transaction.send_keys("123 12")
        transaction.send_keys(Keys.TAB) 
        error_message = driver.find_element(By.XPATH, "//label[@id='message13']").text  
        self.assertEqual("Characters are not allowed", error_message, "Error message does not match")
                
    def testcase_15_customized_statement(self):
        driver = self.driver    
        driver.get("https://demo.guru99.com/V4/") 
        # Customized Statement. TestCase 15
        # Login to account

        login = driver.find_element("name", "uid")
        login.clear()
        login.send_keys("mngr519284")
        password= driver.find_element("name", "password")
        password.clear()
        password.send_keys("yzajanU")
        driver.find_element(By.XPATH, "//tbody/tr[3]/td[2]/input[1]").click()
        # Start of the Test Case
        driver.find_element(By.XPATH, "//a[contains(text(),'Customised Statement')]").click()
        transaction = driver.find_element(By.XPATH, "//tbody/tr[10]/td[2]/input[1]")
        transaction.send_keys(Keys.SPACE)
        transaction.send_keys(Keys.TAB)
        # This test case fails, because instead of "First character cannot have space", it shows "Characters are not allowed" error.
        error_message = driver.find_element(By.XPATH, "//label[@id='message13']").text  
        self.assertEqual("First character cannot have space", error_message, "Error message does not match")
         
    def testcase_16_customized_statement(self):
        driver = self.driver    
        driver.get("https://demo.guru99.com/V4/") 
        # Customized Statement. TestCase 16
        # Login to account
        login = driver.find_element("name", "uid")
        login.clear()
        login.send_keys("mngr519284")
        password= driver.find_element("name", "password")
        password.clear()
        password.send_keys("yzajanU")
        driver.find_element(By.XPATH, "//tbody/tr[3]/td[2]/input[1]").click()
        # Start of the Test Case
        driver.find_element(By.XPATH, "//a[contains(text(),'Customised Statement')]").click()
        account_number = driver.find_element(By.XPATH, "//tbody/tr[6]/td[2]/input[1]")
        account_number.send_keys("125074")
        from_date=driver.find_element(By.XPATH, "//tbody/tr[7]/td[2]/input[1]")
        from_date.send_keys("2023")
        from_date.send_keys(Keys.TAB)
        from_date.send_keys("08")
        from_date.send_keys("05")
        to_date=driver.find_element(By.XPATH, "//tbody/tr[8]/td[2]/input[1]")
        to_date.send_keys("2023")
        to_date.send_keys(Keys.TAB)
        to_date.send_keys("08")
        to_date.send_keys("07")
        min_transaction=driver.find_element(By.XPATH, "//tbody/tr[9]/td[2]/input[1]")
        min_transaction.send_keys("1")
        num_transaction=driver.find_element(By.XPATH, "//tbody/tr[10]/td[2]/input[1]")
        num_transaction.send_keys("10000")
        num_transaction=driver.find_element(By.XPATH, "//tbody/tr[13]/td[2]/input[2]").click()
        # Check if reset button works(all entered data are empty).
        error_message = driver.find_element(By.XPATH, "//tbody/tr[6]/td[2]/input[1]").text  
        self.assertEqual("", error_message, "Error message does not match")
        error_message = driver.find_element(By.XPATH, "//tbody/tr[7]/td[2]/input[1]").text  
        self.assertEqual("", error_message, "Error message does not match")
        error_message = driver.find_element(By.XPATH, "//tbody/tr[8]/td[2]/input[1]").text  
        self.assertEqual("", error_message, "Error message does not match")
        error_message = driver.find_element(By.XPATH, "//tbody/tr[9]/td[2]/input[1]").text  
        self.assertEqual("", error_message, "Error message does not match")
        error_message = driver.find_element(By.XPATH, "//tbody/tr[10]/td[2]/input[1]").text  
        self.assertEqual("", error_message, "Error message does not match")

    def testcase_17_customized_statement(self):
        driver = self.driver    
        driver.get("https://demo.guru99.com/V4/") 
        # Customized Statement. TestCase 17
        # Login to account

        login = driver.find_element("name", "uid")
        login.clear()
        login.send_keys("mngr519284")
        password= driver.find_element("name", "password")
        password.clear()
        password.send_keys("yzajanU")
        driver.find_element(By.XPATH, "//tbody/tr[3]/td[2]/input[1]").click()
        # Start of the Test Case
        driver.find_element(By.XPATH, "//a[contains(text(),'Customised Statement')]").click()
        account_number = driver.find_element(By.XPATH, "//tbody/tr[6]/td[2]/input[1]")
        account_number.send_keys("125074")
        from_date=driver.find_element(By.XPATH, "//tbody/tr[7]/td[2]/input[1]")
        from_date.send_keys("2023")
        from_date.send_keys(Keys.TAB)
        from_date.send_keys("08")
        from_date.send_keys("05")
        min_transaction=driver.find_element(By.XPATH, "//tbody/tr[9]/td[2]/input[1]")
        min_transaction.send_keys("100")
        num_transaction=driver.find_element(By.XPATH, "//tbody/tr[10]/td[2]/input[1]")
        num_transaction.send_keys("1")
        time.sleep(2)
        num_transaction=driver.find_element(By.XPATH, "//tbody/tr[13]/td[2]/input[1]").click()
        error_message = driver.find_element(By.XPATH, "//tbody/tr[10]/td[2]/input[1]").text  
        self.assertEqual("Please fill all fields", error_message, "Error message does not match")

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
    

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="test_reports"))