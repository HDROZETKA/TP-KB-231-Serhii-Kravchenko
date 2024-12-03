import requests


def get_exchange_rates():
    """Отримує актуальні курси валют від НБУ."""
    url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        # Вибираємо курси для потрібних валют
        rates = {item["cc"]: item["rate"] for item in data if item["cc"] in ["USD", "EUR", "PLN"]}
        return rates
    except requests.exceptions.RequestException as e:
        print(f"Помилка при отриманні даних: {e}")
        return None


def convert_currency(amount, currency, rates):
    """Конвертує вказану кількість іноземної валюти в гривні."""
    if currency not in rates:
        print("Обрана валюта не підтримується.")
        return None
    return amount * rates[currency]


def main():
    print("Програма конвертації валют (USD, EUR, PLN -> UAH)")
    rates = get_exchange_rates()
    if not rates:
        print("\nНе вдалося отримати курси валют. Спробуйте пізніше.")
        return

    print("Доступні валюти: USD, EUR, PLN")
    currency = input("Введіть код валюти: ").strip().upper()
    if currency not in ['USD', 'EUR', 'PLN']:
        print('\nНеправильно вказано валюту.')
        return
    try:
        amount = float(input("Введіть кількість валюти: "))
    except ValueError:
        print("\nНекоректне значення. Введіть числове значення.")
        return

    result = convert_currency(amount, currency, rates)
    if result is not None:
        print(f"\n{amount} {currency} = {result:.2f} UAH")


main()
