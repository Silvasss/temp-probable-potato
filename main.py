# Python 3.9
import json


def main():
    #Abrindo o arquivo original e fechando logo em seguida.
    file = open('extracao.json', 'r', encoding='utf-8')
    json_object = json.load(file)
    file.close()

    #Selecionando os objetos válidos que são diferentes de "{}" e "7"
    def number_fields():
        words = ["saude mental", "mental health"]

        #Criando um novo arquivo json para adicionar os objetos válidos
        with open('file_final_extracao1.json', 'w', encoding='utf-8') as file_final:
            for i in range(len(json_object['data']['dados'][:30000])):
                # Verificar o tamanho
                if len(json_object['data']['dados'][i]) == 7:
                    # Verificar a existência das palavras
                    if ("saude mental" or "mental health") in json_object['data']['dados'][i]['Titulo'] or json_object['data']['dados'][i]['Resumo'] or json_object['data']['dados'][i]['Palavraschaves']:
                        #Salvando no novo arquivo e codificando em "uft-8"
                        file_final.write(json.dumps(json_object['data']['dados'][i], ensure_ascii=False))
                        file_final.write(",\n")

        # Criando um novo arquivo json para adicionar os objetos válidos
        with open('file_final_extracao2.json', 'w', encoding='utf-8') as file_final:
            for i in range(len(json_object['data']['dados'][30000:])):
                # Verificar o tamanho
                if len(json_object['data']['dados'][i]) == 7:
                    # Verificar a existência das palavras
                    if ("saude mental" or "mental health") in json_object['data']['dados'][i]['Titulo'] or json_object['data']['dados'][i]['Resumo'] or json_object['data']['dados'][i]['Palavraschaves']:
                        #Salvando no novo arquivo e codificando em "uft-8"
                        file_final.write(json.dumps(json_object['data']['dados'][i], ensure_ascii=False))
                        file_final.write(",\n")

    number_fields()

if __name__ == '__main__':
    main()