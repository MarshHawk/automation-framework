from _pytest.runner import CallInfo

class Verifier(object):
    """Verifier class for implementing soft asserts, like Java TestNG: https://github.com/Gadigeppa-J/testng"""

    def __init__(self):
        self.assertion_errors = []

    def get_assertion_buffer(self):
        return self.assertion_errors

    def verify(self, expected, actual):
        try:
            assert expected == actual
        except AssertionError as e:
            ve = VerificationError()
            ve.args = e.args
            self.assertion_errors.append(ve)

class VerificationError(Exception):
    pass
    #def __init__(self, message, error_arg=None):

        # Call the base class constructor with the parameters it needs
    #    super().__init__(message)

        # Now for your custom code...
        #self.errors = errors

#class VerifyingCallInfo(CallInfo):
    #pass
    #def __init__(self, message, error_arg=None):
        #super().__init__(message)

        # Now for your custom code...
        #self.errors = errors