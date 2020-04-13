# Guia do desenvolvedor sistema EAR-FW

## Escopo

O objetivo deste documento é descrever os aspectos necessários do sistema EAR para possibilitar o desenvolvimento do “firmware” da ECU EAR. É indispensável a leitura prévia da última versão do documento “EAR System Developer's HW Guide” para que o desenvolvedor de software entenda o sistema EAR e seu HW.

**Estão previstas ampliações de escopo do projeto para suportar respiração assistida,
Somente para os pacientes em fase de recuperação. A eletrônica do projeto EAR já
contempla expansões para esta função e outras.**

** Este projeto pode ser alterado a qualquer momento, sem aviso prévio.**

**Disclaimer: não assumimos nenhuma responsabilidade sobre qualquer dispositivo
construído a partir das informações deste documento e orientamos para que os dispositivos sejam projetados na estrita observância às normas locais, que sigam as recomendações de especialistas e que sejam homologados pelas agências reguladoras em todas as fases.**

## Controle de documento

| Data       | Assunto                    | Descrição                                                    |
| ---------- | -------------------------- | ------------------------------------------------------------ |
| 30/03/2020 | Emissão R00 – Português BR | - Definidos requisitos gerais<br />- Definidos em FW01: testes de hardware e ferramentas necessárias para próximas etapas<br /> - Definidos em FW01: testes para podermos modelar parâmetros importantes de funcionamento<br />- Operação com paciente a ser implementada |

## Referências

* [Open Source COVID19 Medical Supplies facebook](https://www.facebook.com/groups/670932227050506/)
* [COVID-19 Air BRASIL - Fast production of assisted ventilation devices](https://www.facebook.com/groups/235476464265909)
* RDSV200320 Emergency Automatic Respirator Specification R00 – Preliminary
* RDSV200322 EAR Hardware Proposition Draft R00 – PTBR
* MIT E-Vent – “Key Ventilation Specifications”
* RDSV200329 EAR System Developer's HW Guide PTBR R00

## Abreviaturas utilizadas

Abreviaturas e termos utilizadas em todo o documento:

| Abreviatura | Descrição                                                    |
| ----------- | ------------------------------------------------------------ |
| EAR         | Emergency Automotic Respirator                               |
| FDC         | Fim de Curso                                                 |
| BAG         | Bolsa de ar, pode ser a do AMBU ou a do FIO2                 |
| AMBU        | Equipamento médico existente, utilizamos somente o BAG para comprimir ar para o paciente |
| FIO2        | Fraction of Inspired O2 define a proporção de O2 no ar inspirado pelo paciente |
| ECU         | Electronic Control Unit                                      |
| PEEP        | Pressão positiva expiratória final. Para eletrônicos e SW developers, se trata de um “Offset DC” na pressão do ar do pulmão do paciente. A pressão nunca cai a menos de 5-10cm de H20. |
| HEPA        | tecnologia empregada em filtros de ar com alta eficiência na separação de partículas (wikipedia) |
| NPN         | Polaridade da conexão do sensor ou atuador, comuta ou é comutado pelo GND (Low Side) |
| SPI         | Serial Peripheral Interface, interface serial síncrona, baseada em registradores de deslocamento |
| WIP         | Work in Progress, trabalho não finalizado                    |
| GPIO        | General Purpose IO, ou porta de uso geral do arduíno         |
| SOA         | Safe operating area, ou área de operação segura do componente |
| POTS        | Potenciômetros                                               |
| CW          | Clockwise ou sentido de compressão do AMBU (A+ B-)           |
| CCW         | Counterclockwise ou descompressão do AMBU (A- B+)            |

## Considerações Iniciais, Requisitos Básicos, Visão Global do Sistema EAR, Visão Geral do Hardware Controlado pelo Sistema EAR
Ver RDSV200329 EAR System Developer's HW Guide PTBR R00.

### Requisitos do SW ECU EAR

#### Requisitos Gerais

##### Target HW

Qualquer firmware deve ser desenvolvido para rodar em um Arduíno Pro Mini, mediante
bootloader. Embora tenha sido previsto um conector ICSP no hardware, não disponível no
Arduíno Pro Mini, isto exigiria um equipamento de gravação AVR que pode não ser disponível.

Pinout do Arduino Pro Mini:

