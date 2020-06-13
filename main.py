import cProfile, pstats, io
from pstats import SortKey
from PythonStudies.sample_functions import cpf_utils
import itertools

def profile_fn(fn):
    pr = cProfile.Profile()
    pr.enable()
    fn()
    pr.disable()
    s = io.StringIO()
    sortBy = SortKey.CUMULATIVE
    ps = pstats.Stats(pr, stream=s).sort_stats(sortBy)
    ps.print_stats()
    print(s.getvalue())


def formata_cpf_loop_1(): 
    i=int(0)
    # success = 0
    # failures = 0    
    while i < 1000000:
        cpf_utils.formata_cpf_1(12345678900)
    #     if ret == "123.456.789-00":
    #         success += 1
    #     else:
    #         failures += 1
        i += 1
    # print(f"Sucessos: {success}, falhas: {failures}, iterações: {i}")

def formata_cpf_loop_2(): 
    for _ in itertools.repeat(None, 1000000):
        cpf_utils.formata_cpf_2(12345678900)

def formata_cpf_loop_3(): 
    for _ in itertools.repeat(None, 1000000):
        cpf_utils.formata_cpf_3(12345678900)


def formata_cpf_loop_3_slow(): 
    for _ in itertools.repeat(None, 1000000):
        cpf_utils.formata_cpf_slow_3(12345678900)

if __name__ == "__main__":
    print("Executando funções de exemplo")
    # print("=============== Função 1 ===============")
    # profile_fn(formata_cpf_loop_1)
    # print("========================================")
    print("=============== Função 2 ===============")
    profile_fn(formata_cpf_loop_2)
    print("========================================")
    print("=============== Função 3 ===============")
    profile_fn(formata_cpf_loop_3)
    print("========================================")
    # print(cpf_utils.formata_cpf_3(12345678900))