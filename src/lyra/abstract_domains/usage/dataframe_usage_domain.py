from lyra.abstract_domains.stack import Stack
from lyra.abstract_domains.state import State
from lyra.core.expressions import Slicing, Expression, Subscription, VariableIdentifier, BinaryComparisonOperation


class DataFrameColumnUsageState(Stack, State):
    def push(self):
        pass

    def pop(self):
        pass

    def _assign_variable(self, left: VariableIdentifier, right: Expression) -> 'State':
        pass

    def _assign_subscription(self, left: Subscription, right: Expression) -> 'State':
        pass

    def _assign_slicing(self, left: Slicing, right: Expression) -> 'State':
        pass

    def _assume_variable(self, condition: VariableIdentifier, neg: bool = False) -> 'State':
        pass

    def _assume_subscription(self, condition: Subscription, neg: bool = False) -> 'State':
        pass

    def _assume_eq_comparison(self, condition: BinaryComparisonOperation, bwd: bool = False):
        pass

    def _assume_noteq_comparison(self, condition: BinaryComparisonOperation, bwd: bool = False):
        pass

    def _assume_lt_comparison(self, condition: BinaryComparisonOperation, bwd: bool = False):
        pass

    def _assume_lte_comparison(self, condition: BinaryComparisonOperation, bwd: bool = False):
        pass

    def _assume_gt_comparison(self, condition: BinaryComparisonOperation, bwd: bool = False):
        pass

    def _assume_gte_comparison(self, condition: BinaryComparisonOperation, bwd: bool = False):
        pass

    def _assume_is_comparison(self, condition: BinaryComparisonOperation, bwd: bool = False):
        pass

    def _assume_isnot_comparison(self, condition: BinaryComparisonOperation, bwd: bool = False):
        pass

    def _assume_in_comparison(self, condition: BinaryComparisonOperation, bwd: bool = False):
        pass

    def _assume_notin_comparison(self, condition: BinaryComparisonOperation, bwd: bool = False):
        pass

    def enter_if(self) -> 'State':
        pass

    def exit_if(self) -> 'State':
        pass

    def enter_loop(self) -> 'State':
        pass

    def exit_loop(self) -> 'State':
        pass

    def forget_variable(self, variable: VariableIdentifier) -> 'State':
        pass

    def _output(self, output: Expression) -> 'State':
        pass

    def _substitute_variable(self, left: VariableIdentifier, right: Expression) -> 'State':
        pass

    def _substitute_subscription(self, left: Subscription, right: Expression) -> 'State':
        pass

    def _substitute_slicing(self, left: Slicing, right: Expression) -> 'State':
        pass
