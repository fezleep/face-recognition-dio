# face recognition dio

Projeto criado para o desafio da DIO: **criando um sistema de reconhecimento facial do zero**.

A ideia aqui foi montar um fluxo simples, funcional e bem documentado para detectar faces em uma imagem e associar nomes/classes às faces encontradas. O reconhecimento foi representado com labels simulados, deixando o projeto honesto sobre o que foi implementado.

## objetivo

Detectar faces em uma imagem usando OpenCV, desenhar bounding boxes ao redor das faces detectadas e adicionar labels como `pessoa_1`, `pessoa_2` e `pessoa_3`.

O resultado final é salvo em:

```bash
images/output/face_detection_result.jpg
```

## o que foi feito

- criação de um script local em Python
- criação de um notebook para Google Colab
- detecção facial com Haar Cascade pré-treinado do OpenCV
- geração de bounding boxes nas faces detectadas
- criação de labels simulados para representar a etapa de reconhecimento/classificação
- salvamento da imagem processada em `images/output`
- documentação sobre como evoluir para reconhecimento facial real com dataset próprio

## detecção facial x reconhecimento facial

Detecção facial é a etapa que localiza onde existem faces em uma imagem. Ela responde à pergunta: "onde há um rosto aqui?".

Reconhecimento facial é a etapa que tenta identificar quem é a pessoa detectada. Ela responde à pergunta: "de quem é esse rosto?".

Neste projeto, a detecção foi implementada com um detector pré-treinado do OpenCV. A etapa de reconhecimento foi simulada com labels automáticos, como `pessoa_1`, para representar o fluxo completo sem afirmar que um modelo próprio foi treinado.

## tecnologias usadas

- Python
- OpenCV
- NumPy
- Matplotlib
- Google Colab

## estrutura do projeto

```text
face-recognition-dio/
├── README.md
├── requirements.txt
├── .gitignore
├── notebooks/
│   └── face_recognition_colab.ipynb
├── src/
│   └── main.py
├── images/
│   ├── input/
│   ├── output/
│   └── README.md
├── dataset/
│   └── README.md
└── docs/
    └── entrega_dio.md
```

## como rodar no colab

1. Abra o arquivo `notebooks/face_recognition_colab.ipynb` no Google Colab.
2. Execute as células na ordem.
3. Faça upload de uma imagem quando o notebook solicitar.
4. Ao final, o resultado será salvo em:

```bash
images/output/face_detection_result.jpg
```

## como rodar localmente

Crie um ambiente virtual, instale as dependências e execute o script:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python src/main.py
```

Antes de executar, coloque uma imagem em:

```bash
images/input/input.jpg
```

## resultado esperado

O projeto gera uma nova imagem com:

- retângulos ao redor das faces detectadas
- labels simulados acima das faces
- arquivo final salvo em `images/output`

## imagem do resultado

Adicione aqui o print ou a imagem gerada pelo projeto:

```md
![resultado da detecção facial](images/output/face_detection_result.jpg)
```

## observações importantes

Este projeto usa um detector pré-treinado para localizar faces. Ele não treina um modelo de reconhecimento facial do zero.

A etapa de reconhecimento/classificação foi representada com labels simulados para demonstrar o fluxo de um sistema completo.

Para transformar isso em reconhecimento real, o próximo passo seria criar um dataset próprio, separar imagens por pessoa e treinar ou ajustar um classificador.

## aprendizados

- diferença entre detectar uma face e reconhecer uma pessoa
- uso do OpenCV para visão computacional
- aplicação de Haar Cascade para detecção facial
- desenho de bounding boxes e textos em imagens
- organização de um projeto simples para entrega técnica

## próximos passos

- montar um dataset próprio com imagens por pessoa
- extrair faces detectadas para treino
- testar descritores faciais ou embeddings
- treinar um classificador real
- comparar Haar Cascade com detectores mais modernos

## comandos git

```bash
git init
git add .
git commit -m "feat: add face recognition project"
git branch -M main
git remote add origin https://github.com/fezleep/face-recognition-dio.git
git push -u origin main
```

O repositório local foi preparado, mas o push não é feito automaticamente.

## conclusão

O projeto entrega um fluxo funcional de detecção facial com OpenCV e simula a etapa de reconhecimento usando labels. A implementação é simples, mas deixa uma base clara para evoluir para reconhecimento facial real com uma base de imagens própria.
