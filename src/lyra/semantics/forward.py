from lyra.semantics.semantics import Semantics, DefaultSemantics

from lyra.abstract_domains.state import State
from lyra.core.statements import VariableAccess, Assignment, Call


class ForwardSemantics(Semantics):
    """Forward semantics of statements."""
    pass


class UserDefinedCallSemantics(ForwardSemantics):
    """Forward semantics of user-defined function/method calls."""

    def user_defined_call_semantics(self, stmt: Call, state: State) -> State:
        """Forward semantics of a user-defined function/method call.

        :param stmt: call statement to be executed
        :param state: state before executing the call statement
        :return: state modified by the call statement
        """
        error = f"Forward semantics for call statement {stmt} not yet implemented!"
        raise NotImplementedError(error)


class AssignmentSemantics(ForwardSemantics):
    """Forward semantics of assignments."""

    def assignment_semantics(self, stmt: Assignment, state: State) -> State:
        """Forward semantics of an assignment. 
        
        :param stmt: assignment statement to be executed
        :param state: state before executing the assignment
        :return: state modified by the assignment
        """
        lhs = self.semantics(stmt.left, state).result    # lhs evaluation
        rhs = self.semantics(stmt.right, state).result   # rhs evaluation
        if isinstance(stmt.left, VariableAccess):
            return state.assign_variable(lhs, rhs)
        error = "Forward semantics for assignment {stmt} not yet implemented!"
        raise NotImplementedError(error)


# noinspection PyAbstractClass
class DefaultForwardSemantics(DefaultSemantics, UserDefinedCallSemantics, AssignmentSemantics):
    """Default forward semantics of statements."""
    pass