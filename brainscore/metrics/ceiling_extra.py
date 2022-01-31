from brainscore.metrics.ceiling import Ceiling, _SplitHalvesConsistency, SplitHalfConsistency
from brainscore.metrics.xarray_utils import Defaults as XarrayDefaults



class InternalConsistencyLore(Ceiling):
    def __init__(self,
                 split_coord=_SplitHalvesConsistency.Defaults.split_coord, stimulus_coord=XarrayDefaults.stimulus_coord,
                 neuroid_dim=XarrayDefaults.neuroid_dim, neuroid_coord=XarrayDefaults.neuroid_coord, cross_validation_kwargs=None):
        consistency = SplitHalfConsistency(stimulus_coord=stimulus_coord, neuroid_dim=neuroid_dim,
                                           neuroid_coord=neuroid_coord)
        self._consistency = _SplitHalvesConsistency(consistency=consistency, split_coord=split_coord,
                                                    aggregate=consistency.aggregate, cross_validation_kwargs=cross_validation_kwargs)

    def __call__(self, assembly):
        return self._consistency(assembly)