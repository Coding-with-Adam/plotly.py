import _plotly_utils.basevalidators


class StepValidator(_plotly_utils.basevalidators.CompoundValidator):

    def __init__(
        self,
        plotly_name='stepdefaults',
        parent_name='layout.slider',
        **kwargs
    ):
        super(StepValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop('data_class_str', 'Step'),
            data_docs=kwargs.pop('data_docs', """
"""),
            **kwargs
        )