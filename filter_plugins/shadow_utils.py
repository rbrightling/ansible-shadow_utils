""" Shadow Utils Ansible Jinja Filters """
__metaclass__ = type


def option(value, join=";"):
    if value is True:
        return "yes"
    elif value is False:
        return "no"
    elif type(value) is list:
        return join.join(value)
    else:
        return value


class FilterModule(object):

    def filters(self):
        return {
            'login_defs_option': option,
        }
