# dataset

Esta pasta representa como uma base propria poderia ser organizada para evoluir o projeto para reconhecimento facial real.

Uma estrutura simples seria:

```text
dataset/
├── pessoa_1/
├── pessoa_2/
└── pessoa_3/
```

Cada pasta teria varias imagens da pessoa correspondente. Com isso, seria possivel extrair as faces, gerar caracteristicas e treinar ou ajustar um classificador para associar uma nova face a uma pessoa conhecida.

Neste projeto, essa etapa ainda nao treina um modelo proprio. A classificacao foi simulada com labels como `pessoa_1`, `pessoa_2` e `pessoa_3`, mantendo o foco no fluxo de deteccao e anotacao das faces.
