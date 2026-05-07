import requests

def get_exchange_rates(api_url):
    """Fetch exchange rates from an API."""
    try:
        response = requests.get(api_url)
        response.raise_for_status()  
        data = response.json()
        return data["rates"]
    except requests.exceptions.ConnectionError:
        print("Error: Unable to connect to the internet or API server.")
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}")
    except KeyError:
        print("Error: Unexpected response format from the API.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return None


def convert_currency(amount, from_currency, to_currency, rates):
    """Convert the given amount from one currency to another."""
    try:
        if from_currency not in rates or to_currency not in rates:
            print("Error: One of the entered currencies is not supported.")
            return None
        
        
        usd_amount = amount / rates[from_currency]
        converted_amount = usd_amount * rates[to_currency]
        return converted_amount
    except ZeroDivisionError:
        print("Error: Invalid conversion rate encountered.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


def main():
    print(" === Real-Time Currency Converter === \n")

    
    api_url = "https://api.exchangerate-api.com/v4/latest/USD"
    rates = get_exchange_rates(api_url)

    if not rates:
        return  


    print("Available currencies (examples):", ", ".join(list(rates.keys())[:10]), "...")
    
    try:
        amount = float(input("\nEnter the amount to convert: "))
        from_currency = input("Enter the source currency code (e.g., USD, INR, EUR): ").upper()
        to_currency = input("Enter the target currency code (e.g., USD, INR, EUR): ").upper()

        converted = convert_currency(amount, from_currency, to_currency, rates)
        if converted is not None:
            print(f"\n✅ {amount:.2f} {from_currency} = {converted:.2f} {to_currency}")
    except ValueError:
        print("Error: Please enter a valid numeric amount.")


if __name__ == "__main__":
    main()
