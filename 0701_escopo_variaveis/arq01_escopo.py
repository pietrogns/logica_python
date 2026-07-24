# Nem toda variável é acessivel em qulauqer parte do programa. O escopo define onde uma variável pode ser usada e por quanto tempo ela existe - Seu tempo de vida.
# - Onde existe? Depende de como e onde a variável foi definida no codigo.
# - Por quanto tempo? algumas vivem só durante a execução de uma função; Outras persistem por todo o programa.
# - Por que importa? entender escopo evita erros como NAMEERROR e conflitos de nomes.
# Tipos de escopo: Local(dentro de uma função); Global(no nivel do moóulo); Built-in(nomes pré definidos pelo python)

GLOBAL_VAR = 'valor global'

def exemplo_local():
     
    # variavel local - só existe dentro dessa função

    local_var = 'valor local'
    print('local_var:', local_var)
    
    # acessar variavel global para leitura funciona sem declarar 'global'
    
    print('GLOBAR_VAR:', GLOBAL_VAR)

    # usar um built-in (len)

print('Built-in len(\'abc\'):', len('abc'))

def exemplo_modifica():
    # para modificar a variavel global dentro da função, declarar 'global'
    global GLOBAl_VAR
    GLOBAL_VAR = 'novo valor global'
    print('GLOBAL_VAR modificado para:', GLOBAL_VAR)

print('GLOBAL_VAR (antes):', GLOBAL_VAR)
exemplo_local()
exemplo_modifica()
print('GLOBAL_VAR (depois):', GLOBAL_VAR)