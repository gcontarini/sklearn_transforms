from sklearn.base import BaseEstimator, TransformerMixin


# All sklearn Transforms must have the `transform` and `fit` methods
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        # Retornamos um novo dataframe sem as colunas indesejadas
        return data.drop(labels=self.columns, axis='columns')
class Drop_allzeros_rows(BaseEstimator, TransformerMixin):
    def __init__(self):
        return None

    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        
        data = data.loc[~((data['NOTA_DE'] == 0) & (data['NOTA_EM'] == 0) & (data['NOTA_MF'] == 0) & (data['NOTA_GO'] == 0))]
        
        # Retornamos um novo dataframe sem as colunas indesejadas
        return  data
    
class Total_rep_col(BaseEstimator, TransformerMixin):
    def __init__(self):
        return None

    def fit(self, X, y=None):
        return self
    
    # Cria uma nova coluna com o total de reprovações
    def transform(self, X):
        data = X.copy()
        
        data['TOTAL_REP'] = data['REPROVACOES_DE'] + data['REPROVACOES_EM'] + data['REPROVACOES_MF'] + data['REPROVACOES_GO']
        
        return  data
    
class Rank_col(BaseEstimator, TransformerMixin):
    def __init__(self):
        return None

    def fit(self, X, y=None):
        return self
    
    # Calcula um 'rank' para o aluno baseado no numero de faltas, tarefas online e horas de aula presencial
    def transform(self, X):
        data = X.copy()
        
        temp = new_data.copy()
        
        temp['H_AULA_PRES'] = (data['H_AULA_PRES'] - data['H_AULA_PRES'].min()) / (data['H_AULA_PRES'].max() - data['H_AULA_PRES'].min())
        temp['TAREFAS_ONLINE'] = (data['TAREFAS_ONLINE'] - data['TAREFAS_ONLINE'].min()) / (data['TAREFAS_ONLINE'].max() - data['TAREFAS_ONLINE'].min())
        temp['TX'] = 1 - ((temp['TAREFAS_ONLINE'] + temp['H_AULA_PRES']) / 2)
        
        data['RANK'] = 10 - (data['FALTAS']  * temp['TX']) * (10 / data['FALTAS'].max())
        
        return  data
