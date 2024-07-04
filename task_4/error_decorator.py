"""Decorator for handling errors that arise during the work of the bot"""
import sys
from typing import Callable


def input_error(func: Callable) -> Callable:
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Not enough arguments"
        except KeyError:
            return "Contact not found"
        except KeyboardInterrupt:
            print("\nInterrupted by user!!!")
            sys.exit()
    return inner
