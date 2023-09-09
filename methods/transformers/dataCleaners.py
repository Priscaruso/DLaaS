class DataCleaner:
    def __init__(self, dataframe):
        self.dataframe = dataframe

    def remove_duplicates(self):
        self.dataframe = self.dataframe.drop_duplicates()

    def handle_missing_values(self, method="drop", columns=None):
        """
        Lida com valores nulos no DataFrame.

        Args:
            method (str): Método para lidar com valores nulos. Pode ser 'drop'
                          para remover as linhas com valores nulos,
                          'fill' para preencher os valores nulos com um valor
                          específico ou 'mean' para preencher com a média.
            columns (list): Lista das colunas em que o método deve ser
                            aplicado. Se None, aplica a todas as colunas.
        """
        if method == "drop":
            self.dataframe = self.dataframe.dropna(subset=columns)
        elif method == "fill":
            # Preencha os valores nulos com um valor específico, por exemplo, 0
            self.dataframe.fillna(0, inplace=True)
        elif method == "mean":
            # Preencha os valores nulos com a média das colunas
            # inplace=True removido pois trigava warning
            # 'A value is trying to be set on
            # a copy of a slice from a DataFrame'
            self.dataframe = self.dataframe.fillna(self.dataframe.mean())

    def clean_data(self):
        self.remove_duplicates()
        self.handle_missing_values(method="mean")

    def get_cleaned_dataframe(self):
        return self.dataframe
