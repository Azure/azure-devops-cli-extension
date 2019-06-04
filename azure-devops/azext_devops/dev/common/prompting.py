# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import sys

from knack.log import get_logger
from knack.prompting import NoTTYException, verify_is_a_tty, prompt

logger = get_logger(__name__)


def delete_last_line():
    "Use this function to delete the last line in the STDOUT"
    from colorama import init, deinit
    init()
    # cursor up one line
    sys.stdout.write('\x1b[1A')
    # delete last line
    sys.stdout.write('\x1b[2K')
    deinit()


def prompt_user_friendly_choice_list(msg, a_list, default=1, help_string=None, error_msg=None):
    """Prompt user to select from a list of possible choices.
    :param msg: A message displayed to the user before the choice list
    :type msg: str
    :param a_list: The list of choices (list of strings or list of dicts with 'name' & 'desc')
    "type a_list: list
    :param default: The default option that should be chosen if user doesn't enter a choice
    :type default: int
    :param help_string: Help message to be displayed on the input terminal
    :type help_string: str
    :param error_msg: Error message to display if the terminal is non interactive
    :type error_msg: str
    :returns: The list index of the item chosen.
    """
    verify_is_a_tty_or_raise_error(error_msg=error_msg)
    options = '\n'.join([' [{}] {}{}'
                         .format(i + 1,
                                 x['name'] if isinstance(x, dict) and 'name' in x else x,
                                 ' - ' + x['desc'] if isinstance(x, dict) and 'desc' in x else '')
                         for i, x in enumerate(a_list)])
    allowed_vals = list(range(1, len(a_list) + 1))
    linesToDelete = len(a_list) + 1
    while True:
        val = prompt('{}\n{}\nPlease enter a choice [Default choice({})]: '.format(msg, options, default))
        if val == '?' and help_string is not None:
            for x in range(0, linesToDelete):
                delete_last_line()
            print('Please enter a choice [Default choice({})]: {}'.format(default, '?'))
            print(help_string)
            continue
        if not val:
            val = '{}'.format(default)
        try:
            ans = int(val)
            if ans in allowed_vals:
                for x in range(0, linesToDelete):
                    delete_last_line()
                print('Please enter a choice [Default choice({})]: {}'.format(default, a_list[ans - 1]))
                print('')
                # array index is 0-based, user input is 1-based
                return ans - 1
            raise ValueError
        except ValueError:
            for x in range(0, linesToDelete):
                delete_last_line()
            print('Please enter a choice [Default choice({})]: {}'.format(default, val))
            logger.warning('Valid values are %s', allowed_vals)


def prompt_not_empty(msg, help_string=None):
    """
    Wrapper on knacks prompt function which does not return until non none value is recieved from user input.
    """
    if not help_string:
        help_string = 'This field cannot be left blank.'
    user_input = None
    while not user_input:
        user_input = prompt(msg=msg, help_string=help_string)
    return user_input


def verify_is_a_tty_or_raise_error(error_msg=None):
    """
    Verifies interactive environment raises NoTTYException with the error_msg string
    if the environment is non-interative
    """
    try:
        verify_is_a_tty()
    except NoTTYException:
        raise NoTTYException(error_msg)


def try_verify_is_a_tty():
    """
    Return True for TTY and False for non-TTY terminals
    """
    try:
        verify_is_a_tty()
        return True
    except NoTTYException:
        return False
