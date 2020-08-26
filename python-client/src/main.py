from client import Client


if __name__ == "__main__":
    client = Client("kl13939d.is.klmcorp.net", 9095)

    result = client.scan(
        start_row="2020-02-01|KL",
        stop_row="2020-02-01|KM",
        table_name="flight_leg_departures"
    )

    lst = list(result)
    print(lst[0])
