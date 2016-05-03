# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class DeletePollTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.PhantomJS()
        self.driver.implicitly_wait(30)
        self.base_url = "http://qa01-sakai.marist.edu:8080/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_delete_poll(self):
        driver = self.driver
        driver.get(self.base_url + "/portal/site/8b0b7198-0e36-4413-aa3c-ddf098824ee1")
        driver.find_element_by_id("eid").clear()
        driver.find_element_by_id("eid").send_keys("admin")
        driver.find_element_by_id("pw").clear()
        driver.find_element_by_id("pw").send_keys("admin")
        driver.find_element_by_id("submit").click()
        driver.find_element_by_xpath("//nav[@id='toolMenu']/ul/li[23]/a/span[2]").click()
        idValue = driver.find_element_by_css_selector(".checkbox-cell>input").get_attribute("value")
        driver.find_element_by_css_selector(".checkbox-cell>input").click()
        self.assertTrue(self.is_element_present(By.ID, "poll-row:" + idValue + ":poll-select"))
        driver.find_element_by_id("delete-polls").click()
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^Are you sure you want to remove the selected polls[\s\S]$")
        self.assertFalse(self.is_element_present(By.ID, "poll-row:" + idValue + ":poll-select"))
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
