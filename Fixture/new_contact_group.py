class New_contact_groupHelper:

    def __init__(self, app):
        self.app = app


    def open_created_new_contact(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()


    def created(self, new_contact_group):
        wd = self.app.wd
        self.open_created_new_contact()
        # Created new contact
        # Firstname
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(new_contact_group.firstname)
        # Middlename
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(new_contact_group.middlename)
        # Lastname
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(new_contact_group.lastname)
        # Address
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(new_contact_group.address)
        # Home phone
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(new_contact_group.homephone)
        # Mobile phone
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(new_contact_group.mobile)
        # E-mail
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(new_contact_group.email)
        # Date Birthday
        # Day Birthday
        wd.find_element_by_name("bday").click()
        wd.find_element_by_xpath("//div[@id='content']/form/select/option[13]").click()
        # Month Birthday
        wd.find_element_by_name("bmonth").click()
        wd.find_element_by_xpath("//div[@id='content']/form/select[2]/option[7]").click()
        # Year Birthday
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(new_contact_group.byear)
        # Submint new contact
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()


    def created_2(self, new_contact_group):
        wd = self.app.wd
        self.open_created_new_contact()
        # Created new contact
        # Firstname
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(new_contact_group.firstname)
        # Middlename
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(new_contact_group.middlename)
        # Lastname
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(new_contact_group.lastname)
        # Address
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(new_contact_group.address)
        # Home phone
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(new_contact_group.homephone)
        # Mobile phone
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(new_contact_group.mobile)
        # E-mail
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(new_contact_group.email)
        # Date Birthday
        # Day Birthday
        wd.find_element_by_name("bday").click()
        wd.find_element_by_xpath("//div[@id='content']/form/select/option[15]").click()
        # Month Birthday
        wd.find_element_by_name("bmonth").click()
        wd.find_element_by_xpath("//div[@id='content']/form/select[2]/option[9]").click()
        # Year Birthday
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(new_contact_group.byear)
        # Submint new contact
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()