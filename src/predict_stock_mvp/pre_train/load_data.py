import pandas as pd

class conect_data():
    """
    Classe feita para carregar, salvar e deletar tabelas.
    
    Estou classe trabalha com csv nesse primeiro momento no desenvolvimento do MVP, porém será refatorada quando houver conexão com bancos do cliente.
    """
    def load_table(location_table, name_table, type_table, encoding='ISO-8859-1', sep=';'):
        """
        Carregando tabelas
        """
        data = pd.read_csv(f'{location_table}/{name_table}.{type_table}', encoding=encoding, sep=sep)
        return data
    
    def save_table(data_save, location_table, name_table, type_table):
        """
        Salvando tabelas
        """
        data_save.to_csv(f'{location_table}/{name_table}.{type_table}')
        return 'save_sucess'
    
    def del_table():
        pass