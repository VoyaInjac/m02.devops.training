import datastore


def process_and_store(key, raw_value):
    value = raw_value.strip().upper()
    datastore.store_value(key, value)
    return value


def retrieve_processed(key):
    value = datastore.get_value(key)
    if value is None:
        return None
    return value.lower()


def update_value(key, raw_value):
    value = raw_value.strip().upper()
    datastore.store_value(key, value)


def delete_value(key):
    return datastore.delete_value(key)


def list_all_keys():
    return datastore.list_keys()
