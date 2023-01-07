# # from cpf_cnpj import Documento
# # from validate_docbr import CNPJ
# # # cpf_um = Cpf("10919137652")
# # # print(cpf_um)
# # # exemplo_cnpj = "05137574000120"
# # exemplo_cpf = "00623836041"
# # # cnpj = CNPJ()
# # # print(cnpj.validate(exemplo_cnpj))
# # documento = Documento.cria_documento(exemplo_cpf)
# # # documento2 = CpfCnpj(exemplo_cpf,'cpf')
# # print(documento)
#
# from TelefonesBr import TelefonesBr
# import re
#
# telefone = "552126481234"
# telefone_objeto = TelefonesBr(telefone)
#
# #padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
# #resposta = re.search(padrao,telefone)
# #print(resposta.group())
#
# print(telefone_objeto)
#
#
# # padrao = "\w{5,50}@\w{3,10}.\w{2,3}.\w{2,3}"
# # texto = "aaabbbcc rodrigo123@gmail.com.br"
# # resposta = re.search(padrao, texto)
# # print(resposta.group())
#
# # padrao_molde = "(xx)aaaa-wwww"
# # padrao = "[0-9]{2}[0-9]{4,5}[0-9]{4}"
# # texto = "eu gosto do numero 2126451234 e gosto tben do 34996849987"
# # resposta = re.findall(padrao, texto)
# # print(resposta)


from datetime import datetime, timedelta
from datas_br import DatasBr

# cadastro = DatasBr()
# cadastro.format_data()
#
#
# hoje = datetime.today()
# hoje_formatada = hoje.strftime("%d/%m/%Y %H:%M")
#
# print(hoje)
# print(hoje_formatada)
# print(type(hoje_formatada))



# from datetime import datetime, timedelta
# from datas_br import DatasBr
#
# hoje = DatasBr()
# print(hoje.tempo_cadastro())