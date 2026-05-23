# entrega do projeto

Foi criado um projeto em Python para simular um sistema de reconhecimento facial, passando pelas etapas de deteccao de faces e identificacao visual das pessoas encontradas na imagem.

O projeto usa OpenCV com um detector Haar Cascade pre-treinado para localizar faces em uma imagem. Depois da deteccao, cada face recebe uma bounding box e um label simulado, como `pessoa_1`, `pessoa_2` e `pessoa_3`.

A parte de reconhecimento/classificacao foi representada por esses labels simulados. Isso deixa claro o fluxo esperado de um sistema de reconhecimento facial, sem afirmar que um modelo foi treinado do zero.

Como caminho futuro, o projeto pode ser evoluido com um dataset proprio, organizado por pessoa, permitindo treinar ou ajustar um classificador real para reconhecer faces conhecidas.

Tecnologias usadas:

- Python
- OpenCV
- NumPy
- Matplotlib
- Google Colab
