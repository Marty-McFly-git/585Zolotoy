from selenium import webdriver
import time

#тестовые данные
surname=("Филиппова")
name=("Елизавета")
email=("marty_mcfly@list.ru")
mobile=("89523916629")
password=("Ed!nor0g")

#использование созданного профиля
ChromeOptions options = new ChromeOptions();
options.addArgument("--user-data-dir=/путь/к/папке/с/профилями");
options.addArgument("--profile-directory=Название_папки_с_нужным_профилем");

WebDriver driver = new ChromeDriver(options);

#открытие сайта
link = "https://www.585zolotoy.ru/"

browser = webdriver.Chrome()
browser.get(link)

#переход к форме регистрации
Registration=browser.find_element_by_css_selector("#body > div.main > div.global-content.js-global-content > div.m-info-pane > div > div > div:nth-child(2) > div.m-info-pane__subleft > a")
Registration.click()

#заполнение полей
Surname_field=browser.find_element_by_name("REGISTER[LAST_NAME]")
Name_field=browser.find_element_by_name("REGISTER[NAME]")
Mobile_field=browser.find_element_by_name("REGISTER[PERSONAL_MOBILE]")
Email_field=browser.find_element_by_name("REGISTER[EMAIL]")
Password_field=browser.find_element_by_name("REGISTER[PASSWORD]")
SecondPassword_field=browser.find_element_by_name("REGISTER[CONFIRM_PASSWORD]")
Registration_button=browser.find_element_by_css_selector("fancybox-lock > div > div.fancybox-inner.fancybox-skin.fancybox-default-skin.fancybox-default-skin-open > div > form > div:nth-child(11) > a")

Surname_field.send_keys(surname)
Name_field.send_keys(name)
Mobile_field.send_keys(mobile)
Email_field.send_keys(email)
Password_field.send_keys(password)
SecondPassword_field.send_keys(password)
Registration_button.click()

#подтверждение регистрации
Succses_registration=browser.find_element_by_text("Регистрация прошла успешно")
if Succses_registration=True
Print ("Тест успешен")