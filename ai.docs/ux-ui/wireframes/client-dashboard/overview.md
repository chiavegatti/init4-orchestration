# Client Dashboard — Overview (Wireframe)

## Objetivo da Tela
Fornecer uma visão rápida e acionável da carteira de clientes, interações recentes e saúde das contas.

## Usuários
- Owner/Admin da Empresa
- Usuário da Empresa

## Blocos da Tela (Hierarquia Visual)
1. Header
   - Nome da empresa
   - Total de clientes ativos
   - CTA: Novo Cliente
2. Cards de Status (Métricas)
   - Card: Interações nos últimos 7 dias
   - Card: Novos contatos adicionados (mês atual)
   - Card: Clientes sem contato há mais de 30 dias
3. Lista de Interações Recentes (Timeline)
   - Tabela/Feed com: Cliente, Tipo (Ligação/Email/Nota), Autor, Data/Hora, Resumo (Snippet)
4. Atalhos Rápidos
   - Ver todos os clientes
   - Adicionar nota rápida
   - Convidar novo colega de equipe

## Estados da Tela
- Empty State:
  - Mensagem: "Nenhum cliente cadastrado"
  - CTA: Adicionar meu primeiro cliente
- Loading State:
  - Skeleton para cards e timeline
- Error State:
  - Mensagem clara + ação de retry

## Acessibilidade (Obrigatório)
- Navegação completa por teclado
- Header e cards com hierarquia semântica correta (H1, H2)
- CTA com aria-label descritivo
- Estados de loading anunciados via aria-live

## Eventos/Interações
- Clique em "Novo Cliente" abre formulário de criação
- Clique em interação abre o detalhe do cliente/contato
- Clique em "Ver todos os clientes" redireciona para a lista de clientes
