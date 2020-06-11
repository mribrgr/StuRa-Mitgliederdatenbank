from selenium.webdriver.support.ui import Select


def createReferat(self, referat):
    """
        Erstellen eines Referates über die GUI, benötigt ist ein login als AdminPanel
        Ausgang ist, dass der User Angemeldet ist und sich in der Mitglieder sicht
        befindet.

        :param self:
        :type self:
        :param referat: Name, wie das neue Organisationseinheit heißen soll
        :type referat: string
        :return: No return Value
        :rtype: None
    """

    # Navigieren zum Admin Pannel
    self.browser.find_element_by_xpath("//a[@href='/admin']").click()

    # Navigieren zu Organisationseinheit Hinzufügen
    self.browser.find_element_by_xpath(
        "//a[@href='/admin/aemter/organisationseinheit/add/']").click()

    # fill inputs
    self.browser.find_element_by_xpath(
        "//input[@id='id_bezeichnung']").send_keys(referat)

    # summit form
    self.browser.find_element_by_xpath("//input[@name='_save']").click()

    """
        Überprüfung ob Organisationseinheit hinzugefügt wurde
    """
    self.assertTrue(self.browser.find_element_by_xpath(
        "//a[contains(text(), '%s')]" % referat))
    pass


def createUnterbereich(self, referat, unterbereich):
    """
        Erstellen eines Unterbereiches über die GUI, benötigt ist ein login als AdminPanel
        Ausgang ist, dass der User Angemeldet ist und sich in der Mitglieder sicht
        befindet.

        :param self:
        :type self:
        :param referat: Organisationseinheit, dem der Unterbereich zugeordnet werden soll
        :type referat: string
        :param unterbereich: Name des Unterbereichs
        :type unterbereich: string
        :return: No return Value
        :rtype: None
    """

    # Navigieren zum Admin Pannel
    self.browser.find_element_by_xpath("//a[@href='/admin']").click()

    # Navigieren zu Organisationseinheit Hinzufügen
    self.browser.find_element_by_xpath(
        "//a[@href='/admin/aemter/unterbereich/add/']").click()

    # fill inputs
    self.browser.find_element_by_xpath(
        "//input[@id='id_bezeichnung']").send_keys(unterbereich)

    # fill selects
    select_referat = Select(
        self.browser.find_element_by_xpath("//select[@id='id_referat']"))
    select_referat.select_by_visible_text(referat)

    # summit form
    self.browser.find_element_by_xpath("//input[@name='_save']").click()

    """
        Überprüfung ob Unterbereichs hinzugefügt wurde
    """
    created_unterbereich = unterbereich + " (Organisationseinheit " + referat + ")"
    self.assertTrue(self.browser.find_element_by_xpath(
        "//a[contains(text(), '%s')]" % created_unterbereich))
    pass


def createAmt(self, referat, unterbereich, funktion):
    """
        Erstellen eines Amtes über die GUI, benötigt ist ein login als AdminPanel
        Ausgang ist, dass der User Angemeldet ist und sich in der Mitglieder sicht
        befindet.

        :param self:
        :type self:
        :param referat: Organisationseinheit, dem das Funktion zugeordnet werden soll
        :type referat: string
        :param unterbereich: Unterbereich des Referats
        :type unterbereich: string
        :param funktion: Angabe des Namens, der das neue Funktion erhalten soll
        :type funktion: string
        :return: No return Value
        :rtype: None
    """
    workload = "5"
    unterbereich = unterbereich + " (Organisationseinheit " + referat + ")"

    # Navigieren zum Admin Pannel
    self.browser.find_element_by_xpath("//a[@href='/admin']").click()

    # Navigieren zu Funktion Hinzufügen
    self.browser.find_element_by_xpath(
        "//a[@href='/admin/aemter/funktion/']").click()
    self.browser.find_element_by_xpath(
        "//a[@href='/admin/aemter/funktion/add/']").click()

    # fill inputs
    self.browser.find_element_by_xpath(
        "//input[@id='id_bezeichnung']").send_keys(funktion)
    self.browser.find_element_by_xpath(
        "//input[@id='id_workload']").send_keys(workload)

    # fill selects
    select_referat = Select(
        self.browser.find_element_by_xpath("//select[@id='id_referat']"))
    select_referat.select_by_visible_text(referat)

    select_unterbereich = Select(
        self.browser.find_element_by_xpath("//select[@id='id_unterbereich']"))
    select_unterbereich.select_by_visible_text(unterbereich)

    # summit form
    self.browser.find_element_by_xpath("//input[@name='_save']").click()

    """
        Überprüfung ob Funktion hinzugefügt wurde
    """
    created_amt = funktion + " " + unterbereich
    self.assertTrue(self.browser.find_element_by_xpath(
        "//a[contains(text(), '%s')]" % created_amt))
    pass
