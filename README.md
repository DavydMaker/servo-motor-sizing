# servo-motor-sizing
##### Script to assist in the dimensioning of servomotors in electrical design.
[![Python Version](https://img.shields.io/badge/python-v3.x-blue)](https://www.python.org/downloads/)

Ao executar o script ele vai gerar um arquivo `result.txt` com o resultado dos dimensionamentos realizados de acordo com as informações configuradas no arquivo `conf.txt`.

---

## Configurações
### Configurar nova superfície
Para adicionar uma superfície nova e suas configurações de relevância, adicione uma nova linha no começo do arquivo seguindo o seguinte padrão:
```
{Nome da Superfície}={Valor Torque Mínimo Requerido}|Confiabilidade={X}|Tipo de Engrenagem={X}|Peso={X}|Necessidade/Torque={X}
```

Trocar `{Nome da Superfície}` pelo nome da nova superfície.\
Trocar `{Valor Torque Mínimo Requerido}` pelo torque mínimo requerido (kg*cm) desta superfície.\
Trocar  `{X}` pelos valores das relevâncias em questão para essa superfície.

Exemlo:
```
Aileron=2,15|Confiabilidade=70|Tipo de Engrenagem=80|Peso=90|Necessidade/Torque=100
```

### Configurar novo servo motor
Para adicionar um servo motor novo para realizar os cálculos em cima dele, adicione uma nova linha no final do arquivo seguindo o seguinte padrão:
```
{t}|{p}|{e}|{c}
```

Trocar `{t}` pelo Torque Mínimo 4,8V (N·cm) do servo motor.\
Trocar `{p}` pelo Peso (g) do servo motor.\
Trocar `{e}` pela nota do Tipo de Engrenagem do servo motor.\
Trocar `{c}` pela nota de Confiabilidade do servo motor.

Exemplo:
```
4,8|8,5|10|8
```
