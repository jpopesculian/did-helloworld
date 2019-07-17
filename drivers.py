from bdb_driver import BdbDriver

drivers = {
    'bdb': BdbDriver()
}

def get_driver(did):
    parts = did.split(":", 2)
    if parts[0] != "did":
        return None, None
    driver = drivers[parts[1]]
    id = parts[2]
    return driver, id
