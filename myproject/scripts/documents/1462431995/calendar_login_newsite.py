# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class CalendarLoginNewsite(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://qa01-sakai.marist.edu:8080/portal/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_calendar_login_newsite(self):
        driver = self.driver
        driver.get(self.base_url + "/portal/")
        driver.find_element_by_id("eid").clear()
        driver.find_element_by_id("eid").send_keys("admin")
        driver.find_element_by_id("pw").clear()
        driver.find_element_by_id("pw").send_keys("admin")
        driver.find_element_by_id("submit").click()
        driver.find_element_by_css_selector("span.all-sites-label").click()
        driver.find_element_by_css_selector("#newSite > span").click()
        driver.find_element_by_id("course").click()
        driver.find_element_by_id("submitBuildOwn").click()
        # ERROR: Caught exception [Error: Dom locators are not implemented yet!]
        driver.find_element_by_name("title").clear()
        driver.find_element_by_name("title").send_keys("test1")
        driver.find_element_by_css_selector("div.act > input[name=\"continue\"]").click()
        driver.find_element_by_id("sakai.schedule").click()
        driver.find_element_by_name("Continue").click()
        driver.find_element_by_id("continueButton").click()
        driver.find_element_by_id("addSite").click()
        driver.find_element_by_css_selector("span.flashNotifMessage > a[title=\"test1\"]").click()
        driver.find_element_by_xpath("//nav[@id='toolMenu']/ul/li[3]/a/span[2]").click()
        driver.find_element_by_link_text("Add Event").click()
        driver.find_element_by_id("activitytitle").clear()
        driver.find_element_by_id("activitytitle").send_keys("Test Event")
        Select(driver.find_element_by_id("day")).select_by_visible_text("7")
        Select(driver.find_element_by_id("startHour")).select_by_visible_text("10")
        Select(driver.find_element_by_id("eventType")).select_by_visible_text("Exam")
        driver.find_element_by_css_selector("option[value=\"Exam\"]").click()
        driver.find_element_by_id("location").clear()
        driver.find_element_by_id("location").send_keys("classroom 1")
        driver.find_element_by_name("eventSubmit_doAdd").click()
        driver.find_element_by_link_text("Test Event").click()
        driver.find_element_by_name("eventSubmit_doDelete").click()
        driver.find_element_by_name("eventSubmit_doConfirm").click()
        driver.find_element_by_xpath("//nav[@id='toolMenu']/ul/li[3]/a/span").click()
        driver.find_element_by_link_text("Merge Internal Calendars").click()
        driver.find_element_by_name("eventSubmit_doCancel").click()
        driver.find_element_by_link_text("Publish (private)").click()
        driver.find_element_by_name("eventSubmit_doCancel").click()
        driver.find_element_by_link_text("Add Event").click()
        driver.find_element_by_id("activitytitle").clear()
        driver.find_element_by_id("activitytitle").send_keys("Event 2")
        Select(driver.find_element_by_id("day")).select_by_visible_text("14")
        driver.find_element_by_id("startHour").click()
        Select(driver.find_element_by_id("startHour")).select_by_visible_text("8")
        driver.find_element_by_name("eventSubmit_doAdd").click()
        driver.find_element_by_link_text("Event 2").click()
        driver.find_element_by_name("eventSubmit_doDelete").click()
        driver.find_element_by_name("eventSubmit_doConfirm").click()
        driver.find_element_by_link_text("Fields").click()
        driver.find_element_by_id("textfield").clear()
        driver.find_element_by_id("textfield").send_keys("Field1")
        driver.find_element_by_name("eventSubmit_doAddfield").click()
        driver.find_element_by_id("textfield").clear()
        driver.find_element_by_id("textfield").send_keys("Field2")
        driver.find_element_by_name("eventSubmit_doAddfield").click()
        driver.find_element_by_name("eventSubmit_doUpdate").click()
        driver.find_element_by_link_text("Add Event").click()
        driver.find_element_by_id("activitytitle").clear()
        driver.find_element_by_id("activitytitle").send_keys("Field Check")
        Select(driver.find_element_by_id("day")).select_by_visible_text("15")
        Select(driver.find_element_by_id("startHour")).select_by_visible_text("9")
        driver.find_element_by_name("eventSubmit_doAdd").click()
        driver.find_element_by_link_text("Field Check").click()
        driver.find_element_by_name("eventSubmit_doDelete").click()
        driver.find_element_by_name("eventSubmit_doConfirm").click()
        driver.find_element_by_link_text("Fields").click()
        driver.find_element_by_name("eventSubmit_doCancel").click()
    
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
