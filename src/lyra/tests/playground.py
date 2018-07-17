from lyra.engine.assumption.assumption_analysis import TypeAnalysis, RangeAnalysis, \
    TypeRangeAssumptionAnalysis
from lyra.engine.data_structures.dict_content_analysis import DictContentAnalysis
from lyra.engine.liveness.liveness_analysis import LivenessAnalysis, StrongLivenessAnalysis
from lyra.engine.numerical.interval_analysis import ForwardIntervalAnalysis
from lyra.engine.numerical.interval_analysis import BackwardIntervalAnalysis
from lyra.engine.usage.usage_analysis import SimpleUsageAnalysis

# LivenessAnalysis().main("liveness/example.py")

# StrongLivenessAnalysis().main("dictionary/dict_descr_example.py")

# SimpleUsageAnalysis().main("dictionary/BRCA_example.py")

# ForwardIntervalAnalysis().main("numerical/forward/example.py")

# BackwardIntervalAnalysis().main("numerical/backward/example.py")

# TypeAnalysis().main("assumption/example.py")
# RangeAnalysis().main("assumption/example.py")
# TypeRangeAssumptionAnalysis().main("assumption/example.py")

DictContentAnalysis().main("numerical/dict_example.py")
