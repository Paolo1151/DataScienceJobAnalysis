from analytics import AnalyticsObject
from analytics import AnalyticsProcessorFactory
from analytics import AnalyticsAnalyzer
from analytics import AnalyticsGrapher


class UnivariateObject(AnalyticsObject):
    def __init__(self):
        super().__init__("Univariate")

    def fit(self):
        pass 


class UnivariateProcessorFactory(AnalyticsProcessorFactory):
    def __init__(self, bounded_object: UnivariateObject):
        super().__init__("Univariate", bounded_object, UnivariateObject)

    def create_analyzer(self):
        return UnivariateAnalyzer(self.name, self.bounded_object)

    def create_grapher(self):
        return UnivariateGrapher(self.name, self.bounded_object)


class UnivariateAnalyzer(AnalyticsAnalyzer):
    def __init__(self, name, bounded_object: UnivariateObject):
        super().__init__(name, bounded_object, UnivariateObject)

    def describe_numerical(self, df: pd.DataFrame):
        return df.describe(exclude='object')

    def describe_categorical(self, df: pd.DataFrame):
        return df.describe(include='object')


class UnivariateGrapher(AnalyticsAnalyzer):
    def __init__(self, name, bounded_object: UnivariateObject):
        super().__init__(name, bounded_object, UnivariateObject)  

    def graph_distribution(self, df: pd.DataFrame, column: str):
        pass

    def graph_counts(self, df: pd.DataFrame):
        pass


