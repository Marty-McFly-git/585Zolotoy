from selenium import webdriver

#использование созданного профиля
ChromeOptions options = new ChromeOptions();
options.addArgument("--user-data-dir=/путь/к/папке/с/профилями");
options.addArgument("--profile-directory=Название_папки_с_нужным_профилем");

WebDriver driver = new ChromeDriver(options);

#открытие сайта
link = "https://www.585zolotoy.ru/catalog/koltso-obruchalnoe-gl-207817005966943689/"

browser = webdriver.Chrome()
browser.get(link)

#выбор размера кольца. Берем первый дочерний див размеров - выпадет размер в наличи?
size=browser.find_element_by_css_selector("#app > div.is-details-card-main > div.d-card-details > div.dcd-size-parent > div > div.iss-controls.js-select-size:nth-child(1)")
size.click()

#перемещение в корзину
cart=browser.find_element_by_id("buy-to-cart")
cart.click()

#открытие корзины
open_cart=browser.find_element_by_css_selector("#body > div.main > div.global-content.js-global-content > div.n-header.js-global-header.state-header-line > div > div.n-header-top > div.n-header-top__basket > a")
open_cart.click()

#проверка успешности
Succses=browser.find_element_by_link_text("2078270294281")
if success=True print ("Тест успешен")