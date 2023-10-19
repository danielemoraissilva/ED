
class Hash__table:
  def __init__(self, n):
    self.size = n
    self.nivel_1 = [None]*self.size#vetor com 10 ponteiros para vetores 
  
  def __hash_str(self, key_str):#conversão de chave para número
    num = 0
    for c in key_str:
      num += ord(c)
    return num
  
  def __hash(self, key_str):#retorna posição da chave no primeiro nível
    key = self.__hash_str(key_str)
    return key % self.size 
  
  def __hash_2(self, key_str):#retorna posição da chave no segundo nível
    key = self.__hash_str(key_str)
    return key % self.size // 10 
  
  def insert(self, key, value): #key - nome, value - (nome, matrícula)
    pos = self.__hash(key)
    pos2 = self.__hash_2(key)
    
    if self.nivel_1[pos] is None:#associa vetor[i] do nível 1 a uma lista de n/10 elementos
        self.nivel_1[pos] = [[] for _ in range(self.size // 10)] 
  
    self.nivel_1[pos][pos2].append((key,value))
  
  def get(self, key):
    pos = self.__hash(key)
    pos2 = self.__hash_2(key)
    if self.nivel_1[pos] is not None: 
      for k, value in self.nivel_1[pos][pos2]:
        if k == key:
          return value
    return None
  
  def print(self):
    for i in range(self.size):
        if self.nivel_1[i] is not None:
            print("Nível 1 - índice:  ", i)
            for j in range(self.size // 10):
                print("  Nível 2 - índice: ", j)
                for k, value in self.nivel_1[i][j]:
                    print(f"    Key: {k}, Value: {value}")