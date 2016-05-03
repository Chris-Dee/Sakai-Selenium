# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class CalSynopticLogoutFirst(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://qa01-sakai.marist.edu:8080/portal/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_cal_synoptic_logout_first(self):
        driver = self.driver
        driver.get("http://qa01-sakai.marist.edu:8080/portal/")
        driver.find_element_by_css_selector("span.Mrphs-userNav__submenuitem--userid").click()
        driver.find_element_by_css_selector("span.Mrphs-login-Message").click()
        driver.find_element_by_id("eid").clear()
        driver.find_element_by_id("eid").send_keys("admin")
        driver.find_element_by_id("pw").clear()
        driver.find_element_by_id("pw").send_keys("admin")
        driver.find_element_by_id("submit").click()
        driver.find_element_by_xpath("//a[@id='more-sites-menu']/i").click()
        driver.find_element_by_css_selector("#allSites > span").click()
        driver.find_element_by_css_selector("input[type=\"button\"]").click()
        driver.find_element_by_id("search").clear()
        driver.find_element_by_id("search").send_keys("Albin")
        driver.find_element_by_css_selector("input[type=\"button\"]").click()
        driver.find_element_by_link_text("Albin").click()
        driver.find_element_by_css_selector("span.Mrphs-toolsNav__menuitem--icon.icon-sakai-schedule").click()
        driver.find_element_by_link_text("Add Event").click()
        driver.find_element_by_id("activitytitle").clear()
        driver.find_element_by_id("activitytitle").send_keys("Test Event")
        Select(driver.find_element_by_id("startHour")).select_by_visible_text("12")
        Select(driver.find_element_by_id("eventType")).select_by_visible_text("Exam")
        driver.find_element_by_id("location").clear()
        driver.find_element_by_id("location").send_keys("Classroom 1")
        Select(driver.find_element_by_id("day")).select_by_visible_text("16")
        driver.find_element_by_name("eventSubmit_doAdd").click()
        driver.find_element_by_link_text("Test Event").click()
        driver.find_element_by_name("eventSubmit_doDelete").click()
        driver.find_element_by_name("eventSubmit_doConfirm").click()
        driver.get("http://qa01-sakai.marist.edu:8080/portal/site/3922c667-5672-491a-ab06-8a058d85ed95/tool/740cd854-2e71-43c0-a3fa-5c43297212d9")
        driver.find_element_by_link_text("Calendar").click()
        driver.find_element_by_link_text("Merge Internal Calendars").click()
        driver.find_element_by_name("eventSubmit_doUpdate").click()
        driver.find_element_by_link_text("Publish (private)").click()
        driver.find_element_by_name("eventSubmit_doCancel").click()
        driver.find_element_by_link_text("Add Event").click()
        driver.find_element_by_id("activitytitle").clear()
        driver.find_element_by_id("activitytitle").send_keys("Event2")
        Select(driver.find_element_by_id("day")).select_by_visible_text("14")
        driver.find_element_by_name("eventSubmit_doAdd").click()
        Select(driver.find_element_by_id("startHour")).select_by_visible_text("5")
        driver.find_element_by_name("eventSubmit_doAdd").click()
        driver.find_element_by_link_text("Event2").click()
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
        Select(driver.find_element_by_id("startHour")).select_by_visible_text("10")
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
