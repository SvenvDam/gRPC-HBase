from client import Client


def main():
    client = Client("0.0.0.0", 8080)

    result = client.scan(
        prefix="2020-02-08|KL|90",
        columns={"basic_info": []},
        max_versions=1,
        table_name="flight_leg_departures"
    )

    print(result.get_row_df())


if __name__ == "__main__":
    main()
