from types import FunctionType
"""

"""


class Claim(object):
    """
    an object representing a claim/contract about another object
    """
    def __init__(self, truth: FunctionType=None):
        """
        initializes the claim with the truth about it.
        the truth should be a function that takes a single argument
        """
        if truth:
            self.truths = {truth}

    def __iand__(self, other):
        """
        adds another claim to this one, for example
        if one claim asserts that
        """
        self.truths = self.truths | other.truths
        return self

    def __and__(self, other):
        """
        """
        new = Claim()
        new.truths = self.truths | other.truths
        return new

    def __call__(self, possibility: object) -> bool:
        """
        checks all contained claims against the object
        """
        if {truth(possibility) for truth in self.truths} == {True}:
            return True
        else:
            return False

    def __iadd__(self, other: FunctionType):
        """
        adds another claim to this one
        """
        self.truths = self.truths | {other}
        return self

    def __str__(self):
        """
        """
        return "\n".join(str(truth) for truth in self.truths)


class typedef(object):
    """
    """

    def __init__(self, typestruct: object):
        """
        """
        pass
