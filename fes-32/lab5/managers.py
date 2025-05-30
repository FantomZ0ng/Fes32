class FigureManager:
    def __init__(self):
        self.figures = {}

    def add_figure(self, name):
        def dec(cls):
            self.figures[name] = cls
            return cls

        return dec

    def get_figure(self, name):
        return self.figures.get(name)
    


class FigureCreator:
    def __init__(self, fm):
        self.fm = fm

    def create_figure(self, figure_type, params):

        fig = self.fm.get_figure(figure_type)

        if fig:
            return fig(*params)

        raise ValueError(f"Unknown figure type: {figure_type}")


class ProcessData:

    def __init__(self, fc: FigureCreator):
        self.fc = fc

    def process_data(self, data):

        result = []
        for fig_type, *params in data:
            result.append(self.fc.create_figure(fig_type, params))

        return result