import configparser


def get(option: str, section='general'):
    """Возвращает значение опции

        :param option: имя опции
        :param section: имя секции

        | Если опция задана в config вернёт её значение
        | Если нет задана, вернёт None
        """
    config = configparser.ConfigParser()
    config.read('config.ini')
    try:
        value = config.get(section, option)
    except Exception:
        return None
    return value


