class Tarefa:
    tarefas = []
    def __init__(self, titulo, descricao):
        self.titulo = titulo
        self.descricao = descricao
        self.concluido = False
        Tarefa.tarefas.append(self)
    def __str__(self):
        return f"Tarefa: {self.titulo} - {self.descricao}"
    
    @classmethod
    def listarTarefas(cls):
        for t in cls.tarefas:
            print(t)

tarefa01 = Tarefa("Atividade 01", "Uso do While")
tarefa02 = Tarefa("Atividade POO", "Criar uma classe")

Tarefa.listarTarefas()