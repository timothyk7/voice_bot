import os

def get_api_config_file():
    """
    Gets the api config file
    :return: file path
    :rtype: str
    """
    return get_config_file("priv_api")

def get_config_file(config):
    """
    Gets the config file
    :param config: config name
    :type config: str
    :return: file path
    :rtype: str
    """
    config_file = os.path.join(_get_config_directory(), config + ".ini")
    if not os.path.exists(config_file):
        raise ValueError("Unknown config environment: " + config)
    return config_file

def _get_config_directory():
    """
    Gets the current directory of the config manager
    :return: file path
    :rtype: str
    """
    return os.path.dirname(os.path.realpath(__file__))
