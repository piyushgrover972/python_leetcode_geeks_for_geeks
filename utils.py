#!/usr/bin/env python3

class Test:
    @classmethod
    def assert_equals(cls, func_out, expected_out):
        assert func_out == expected_out, f"The function out '{func_out}' != '{expected_out}'"
