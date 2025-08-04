class BalanceViewModel:
    def __init__(self, ganancias_values=None, perdidas_values=None, labels=None, y_formatter=None):
        self.ganancias_values = ganancias_values or []
        self.perdidas_values = perdidas_values or []
        self.labels = labels or []
        self.y_formatter = y_formatter or (lambda value: f"${value:,.2f}")

    def update_chart_data(self, ganancias, perdidas, labels):
        self.ganancias_values = list(ganancias)
        self.perdidas_values = list(perdidas)
        self.labels = list(labels)
