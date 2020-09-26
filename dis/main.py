import cProfile, pstats, io
from pstats import SortKey
import cpf_utils
import itertools
import sys

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
    for _ in itertools.repeat(None, 1000000):
        cpf_utils.formata_cpf_1(12345678900)

def formata_cpf_loop_2(): 
    for _ in itertools.repeat(None, 1000000):
        cpf_utils.formata_cpf_2(12345678900)

def formata_cpf_loop_3(): 
    for _ in itertools.repeat(None, 1000000):
        cpf_utils.formata_cpf_3(12345678900)

def formata_cpf_loop_4(): 
    for _ in itertools.repeat(None, 1000000):
        cpf_utils.formata_cpf_4(12345678900)

def formata_cpf_loop_5(): 
    for _ in itertools.repeat(None, 1000000):
        cpf_utils.formata_cpf_5(12345678900)

def formata_cpf_loop_6(): 
    for _ in itertools.repeat(None, 1000000):
        cpf_utils.formata_cpf_6(12345678900)

def formata_cpf_loop_7(): 
    for _ in itertools.repeat(None, 1000000):
        cpf_utils.formata_cpf_7(12345678900)


if __name__ == "__main__":
    fns = [ formata_cpf_loop_1,
          formata_cpf_loop_2,
          formata_cpf_loop_3,
          formata_cpf_loop_4,
          formata_cpf_loop_5,
          formata_cpf_loop_6,
          formata_cpf_loop_7 ]
    print("Executando funções de exemplo")
    for fn_ix in sys.argv[1:]:
      print(f"=============== Função {fn_ix} ===============")
      profile_fn(fns[int(fn_ix) - 1])
