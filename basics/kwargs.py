# **kwargs
# in python, functions can have a parameter preceded by two stars (**config)
# the "**kwargs" is called keyword parameter
# Basically, when a function has kwargs it can accept any number of keyword arguments as dictionary


def server_listen(**cfg) -> None:
    # looping over all kwargs
    for key, value in cfg.items():
        print(f"{key}: {value}")

    protocol = "https" if cfg["is_encrypted"] == True else "http"
    print(f"{protocol}://{cfg['host']}:{cfg['port']}")


# basically we can keep expanding these parameters as much as we want
server_listen(
    port=8080, host="localhost", is_encrypted=True, default_endpoint="/index.html"
)
