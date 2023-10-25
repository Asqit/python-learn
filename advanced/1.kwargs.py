# Kwargs (**kwargs)
# Python does allow you to have unlimited number of keyword arguments.
# This behaviour is called kwargs as key-word-arguments
# To add kwargs to your function, you use the: "**" + name_of_your_choice
# The passed kwargs are in 'dict' type !!
# Example:
# > def fn(**cfg):
# >     pass
# But you can combine this with regular *args
# > def fn (*misc, **cfg):
# >     pass


# Example_1
def listen(**cfg) -> None:
    for key, value in cfg.items():
        print(f"{key}: {value}")

    protocol = "https" if cfg["is_encrypted"] == True else "http"
    print(f"Server is listening @ {protocol}://{cfg['host']}:{cfg['port']}")


# You can endlessly keep adding keyword arguments
# it's up to the function to use them.
listen(
    port=8080,
    host="localhost",
    is_encrypted=False,
    default_endpoint="/",
    random_bullshit=("boogie belgique", "Cessna", 10),
)
