def call_me_maybe(client_name):
    # an "expensive" to run network call taking in the range of 50-300ms,
    # like establishing connection to 3rd party API, database, etc.
    print(f"{client_name} - you called?")
