# Admin Dashboard — Tenants Management (Wireframe)

## Objetivo da Tela
Permitir que o administrador da plataforma gerencie as empresas (tenants), controle planos de assinatura, status operacional e uso global do sistema.

## Usuários
- PLATFORM_ADMIN

## Blocos da Tela (Hierarquia Visual)
1. Header
   - Indicadores globais:
     - Total de Tenants (Ativos/Inativos)
     - Total de Usuários na plataforma
     - Novos Cadastros (Últimos 30 dias)
2. Lista de Empresas (Tenants)
   - Tabela com:
     - Nome da Empresa (Tenant)
     - Plano de Assinatura
     - Qtd. de Usuários
     - Qtd. de Clientes Cadastrados
     - Data de Cadastro
     - Status (Ativo/Suspenso)
     - CTA: Gerenciar Tenant
3. Filtros e Busca
   - Busca por Nome ou Domínio
   - Filtro por Plano (Gratuito/Pro/Enterprise)
   - Filtro por Status
4. Ações Administrativas
   - Atribuir Novo Usuário Admin à Empresa
   - Alterar Plano de Assinatura
   - Suspender/Reativar Empresa
5. Monitoramento de Uso
   - Gráfico: Volume de interações globais (saúde da plataforma)
   - Alertas: Tenants atingindo limite de usuários do plano

## Estados da Tela
- Empty State: "Nenhuma empresa cadastrada no sistema."
- Loading State: Skeleton da tabela e cards.
- Error State: Mensagem de erro ao carregar dados globais.

## Acessibilidade (Obrigatório)
- Tabela navegável por teclado.
- Confirmação obrigatória para suspensão de tenant.
- Labels claros para filtros.

## Eventos/Interações
- Clique em "Gerenciar Tenant" abre visão detalhada da empresa.
- Alteração de plano exige confirmação de mudança de limites.
