import pymlconf


settings = pymlconf.DeferredConfigManager()


DEFAULT_ADDRESS = 'localhost:1085'

BUILTIN_CONFIGURATION = f'''
bind: {DEFAULT_ADDRESS}

read_limit: 4096

authentication:
  method: trust

logging:
  level: debug

'''


def configure(init_value=None, files=None):
    """ Load configurations

    .. seealso:: `pymlconf Documentations <https://github.com/pylover/pymlconf#documentation>`_

    :param args: positional arguments pass into ``pymlconf.DeferredConfigManager.load``
    :param kwargs: keyword arguments pass into ``pymlconf.DeferredConfigManager.load``
    """
    settings.load(
        init_value=init_value,
        files=files,
        builtin=BUILTIN_CONFIGURATION,
        missing_file_behavior=pymlconf.IGNORE,
    )
    return settings


