import logging

from configfile import ConfigWrapper


class SecondaryEndstop:
    def __init__(self, config: ConfigWrapper):
        self.name = name = config.get_name().partition(' ')[2]
        self.pin = pin = config.get("pin")
        logging.info("secondary_endstop: %s, %s", name, pin)

        printer = config.get_printer()
        ppins = printer.lookup_object('pins')
        mcu_endstop = ppins.setup_pin('endstop', pin)
        query_endstops = printer.load_object(config, 'query_endstops')
        query_endstops.register_endstop(mcu_endstop, name)


def load_config_prefix(config: ConfigWrapper):
    return SecondaryEndstop(config)
