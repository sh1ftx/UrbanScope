# UrbanScope - Documentação do Projeto

> **Status do Projeto:** Em desenvolvimento (MVP em construção)

---

## ✨ Visão Geral
**UrbanScope** é um dashboard interativo focado em análise de vendas imobiliárias na cidade de Nova York. O projeto visa oferecer uma experiência de exploração geoespacial e estatística de forma visual e intuitiva, utilizando mapas, histogramas e filtros dinâmicos.

---

## 📈 Funcionalidades
- Visualização de dados de vendas com filtro por distrito
- Seleção de metragem dos imóveis
- Mapa interativo com pontos georreferenciados
- Histograma dinâmico baseado na variável escolhida
- Design responsivo com uso de Dash Bootstrap Components

---

## 📁 Estrutura de Diretórios
```
UrbanScope/
│
├── assets/
│   ├── style.css          # Estilos personalizados
│   └── tubrao.jpg         # Logo ou imagem visual
│
├── dataset/
│   ├── cleaned_data.csv   # Dados tratados
│   └── nyc-rolling-sales.csv # Dados originais (backup)
│
├── _controllers.py        # Componentes de controle e filtros
├── _histogram.py          # Componente de histograma
├── _map.py                # Componente do mapa interativo
├── app.py                 # Instância principal do app Dash
└── index.py               # Script principal com layout e callbacks
```

---

## ⚙ Tecnologias Utilizadas
- **Python 3.10+**
- **Dash** (by Plotly)
- **Pandas**
- **Plotly Express & Graph Objects**
- **Dash Bootstrap Components**

---

## 🔧 Como Executar Localmente
```bash
# Clonar o repositório
$ git clone https://github.com/sh1ftx/UrbanScope.git
$ cd urbanscope

# (Recomendado) Criar ambiente virtual
$ python -m venv venv
$ source venv/bin/activate  # Windows: venv\Scripts\activate

# Instalar dependências
$ pip install -r requirements.txt

# Rodar o app
$ python index.py
```

---

## 📊 Futuras Implementações
- Callback para atualização dinâmica do mapa
- Download de relatórios em PDF/CSV
- Filtros temporais por data de venda
- Tradução para inglês (modo bilíngue)

---

## 🚀 Objetivo Final
Fornecer uma ferramenta robusta e intuitiva para análise imobiliária urbana, promovendo insights relevantes a partir de dados reais de mercado em Nova York.

---

## 📄 Licença
Projeto em desenvolvimento. Licença a definir.

---

## 👥 Autoria
Desenvolvido por Kayki Ivan, 2025

