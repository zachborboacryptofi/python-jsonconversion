# Copyright (C) 2016-2017 DLR
#
# All rights reserved. This program and the accompanying materials are made
# available under the terms of the 2-Clause BSD License ("Simplified BSD
# License") which accompanies this distribution, and is available at
# https://opensource.org/licenses/BSD-2-Clause
#
# Contributors:
# Franz Steinmetz <franz.steinmetz@dlr.de>

from pkg_resources import get_distribution, DistributionNotFound

try:
    __version__ = get_distribution("jsonconversion").version
except DistributionNotFound:
    __version__ = "unknown"

try:
    # Python >= 3.6
    from inspect import getfullargspec
except ImportError:
    # Python < 3.6
    from inspect import getargspec as getfullargspec


def get_all_args(func):
    """Determines the names of all arguments of the given function

    :param func: The function/method to be inspected
    :return: Argument names
    :rtype: set(str)
    """
    fullargspec = getfullargspec(func)
    func_args = set()
    for arg_type in ["args", "varargs", "varkw", "kwonlyargs", "keywords"]:
        arg_type_val = getattr(fullargspec, arg_type, None)
        if arg_type_val is not None:
            func_args |= set(arg_type_val)
    return func_args
