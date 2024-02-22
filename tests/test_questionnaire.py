from selene import browser, have, command, by
import os

def test_element_tests():
    browser.open('/automation-practice-form')
    browser.element('#firstName').perform(command.js.scroll_into_view).type('Name')
    browser.element('#lastName').type('Surname')
    browser.element('#userEmail').type('aaaa@aa.com')
    browser.element('[value="Female"]').perform(command.js.click)
    browser.element('#userNumber').type('1010101010')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click().element(by.text('June')).click()
    browser.element('.react-datepicker__year-select').click().element(by.text('1999')).click()
    browser.element('.react-datepicker__day--014').click()
    browser.element('#subjectsInput').type('Maths').press_enter()
    browser.element('[value="3"]').perform(command.js.click)
    browser.element('#uploadPicture').send_keys(os.path.abspath('pic1.jpeg'))
    browser.element('#currentAddress').type('MNE, Budva')
    browser.element('#react-select-3-input').type('Haryana').press_enter()
    browser.element('#react-select-4-input').type('Panipat').press_enter()
    browser.element('#submit').perform(command.js.click)
    browser.element('#example-modal-sizes-title-lg').should(have.text("Thanks for submitting the form")) #pop-up
    browser.element('.table').should(have.text("Name Surname"))
    browser.element('.table').should(have.text("aaaa@aa.com"))
    browser.element('.table').should(have.text("Female"))
    browser.element('.table').should(have.text("1010101010"))
    browser.element('.table').should(have.text("14 June,1999"))
    browser.element('.table').should(have.text("Maths"))
    browser.element('.table').should(have.text("Music"))
    browser.element('.table').should(have.text("pic1.jpeg"))
    browser.element('.table').should(have.text("MNE, Budva"))
    browser.element('.table').should(have.text("Haryana Panipat"))
    browser.element('#closeLargeModal').perform(command.js.click)


