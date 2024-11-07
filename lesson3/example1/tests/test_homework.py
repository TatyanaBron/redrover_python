from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def test_registration(driver, wait):
    # Перейти по URL: Открыть в браузере указанный URL сайта <https://victoretc.github.io/selenium_waits/>
    # * Проверить заголовок: Убедиться, что текст в теге <h1> на странице соответствует "Практика с ожиданиями в Selenium".
    driver.get('https://victoretc.github.io/selenium_waits/')
    element = driver.find_element(By.XPATH, "/html/body/h1")
    assert element.text == "Практика с ожиданиями в Selenium"
    # Дождаться появления кнопки "Начать тестирование"
    # * Найти кнопку: Найти на странице кнопку с текстом "Начать тестирование".
    #* Начать тестирование: Кликнуть по кнопке "Начать тестирование".
    button = wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/button")))
    assert button.is_displayed()
    button.click()
    #* Ввод логина: Ввести "login" в поле для логина.
    login = driver.find_element(By.XPATH, "/html/body/div[1]/label[1]")
    assert login.text == "Логин:"
    login_input = driver.find_element(By.XPATH,"/html/body/div[1]/input[1]")
    login_input.send_keys("login")
    #* Ввод пароля: Ввести "password" в поле для пароля.
    password_input = driver.find_element(By.XPATH,"/html/body/div[1]/input[2]")
    password_input.send_keys("password")
    #* Согласие с правилами: Установить флажок в чекбокс "Согласен со всеми правилами".
    check_box = driver.find_element(By.XPATH, "/html/body/div[1]/label[3]/input")
    check_box.click()
    #* Подтвердить регистрацию: Нажать кнопку "Зарегистрироваться".
    registr = driver.find_element(By.XPATH,"/html/body/div[1]/button")
    registr.click()
    #* Проверка загрузки: Удостовериться, что появился индикатор загрузки.
    #* Проверка сообщения: Убедиться, что после завершения загрузки появилось сообщение "Вы успешно зарегистрированы".
    loading = wait.until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[2]")))
    message = wait.until(EC.visibility_of_element_located((By.ID,"successMessage")))
    assert message.text == "Вы успешно зарегистрированы!"
