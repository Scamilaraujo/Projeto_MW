# Projeto_MW

## Pré-requisitos

- Docker instalado e com suporte a Swarm
- Git

---

## Arquivos `.yml` (não versionados)

Os arquivos `01_grafana.yml`, `02_questdb.yml` e `03_python.yml` foram fornecidos pelo desafio e **não estão no repositório** (estão no `.gitignore`).  
Você deve obtê-los pelo link disponibilizado no desafio e colocá-los na **raiz do projeto**, junto ao `README.md`.

> O arquivo `03_python.yml` foi ajustado para incluir as variáveis de ambiente necessárias. Os nomes das variáveis esperadas são:
>
> | Variável         | Descrição                          |
> |------------------|------------------------------------|
> | `QUESTDB_HOST`   | Hostname do serviço QuestDB        |
> | `QUESTDB_PORT`   | Porta ILP TCP do QuestDB (`9009`)  |
> | `TABLE_NAME`     | Nome da tabela de destino          |

---

## Passo a passo para rodar

### 1. Descobrir o IP da máquina

```bash
ip addr show
```

Anote o IP da interface principal (ex: `192.168.x.x`).

---

### 2. Inicializar o Docker Swarm

> O Swarm precisa de IP explícito quando a máquina possui múltiplos endereços IPv6.

```bash
docker swarm init --advertise-addr "seu_ip"
```

---

### 3. Criar a rede overlay

```bash
docker network create --driver overlay mwsolucoes
```

---

### 4. Subir os containers

Suba as stacks **nessa ordem**:

```bash
docker stack deploy -c 02_questdb.yml teste_selecao
docker stack deploy -c 01_grafana.yml teste_selecao
docker stack deploy -c 03_python.yml  teste_selecao
```

Aguarde alguns segundos para os serviços subirem antes de prosseguir.

---

### 5. Localizar o container Python

```bash
docker ps -a
```

Copie o `CONTAINER ID` do container cujo nome contém `python`.

---

### 6. Acessar o container e rodar o script

```bash
docker exec -it -u root id_do_container bash
```

Dentro do container:

```bash
cd src
python3 script.py
```

O script irá:
1. Ler o CSV em `data/questdb-usuarios-dataset.csv`
2. Aplicar as transformações nos dados
3. Enviar os registros para o QuestDB na tabela configurada em `TABLE_NAME`

---

## Verificar os dados

- **QuestDB UI:** `http://localhost:9000` — acesse a aba SQL e execute `SELECT * FROM usuarios`
- **Grafana:** `http://localhost:3000` — configure ao datasource apontando para `questdb:8812`

---

## Estrutura do projeto

```
Projeto_MW/
├── data/
│   └── questdb-usuarios-dataset.csv
├── src/
│   ├── script.py                        # Ponto de entrada do pipeline
│   ├── config/
│   │   └── variaveis_ambiente.py        # Leitura das variáveis de ambiente
│   ├── tratamento_dados/
│   │   ├── conexao_cliente.py           # Nullifica valores não-numéricos
│   │   ├── status_internet.py           # Mapeia código → nome do status
│   │   └── nome_cliente.py              # Mantém primeiro e último nome
│   └── banco_de_dados/
│       └── questdb.py                   # Envia os dados via ILP TCP
├── 01_grafana.yml                       # Stack Grafana  (não versionado)
├── 02_questdb.yml                       # Stack QuestDB  (não versionado)
└── 03_python.yml                        # Stack Python   (não versionado)
```