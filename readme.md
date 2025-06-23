# INVOX3 - Conectando Marcas e Criadores de Conteúdo

## Descrição

INVOX3 é uma plataforma web inovadora projetada para ser o principal marketplace de influenciadores, facilitando a conexão autêntica e eficiente entre marcas e criadores de conteúdo. O objetivo é descentralizar o marketing de influência, permitindo que criadores de todos os tamanhos construam uma presença profissional e que marcas descubram talentos alinhados com suas campanhas de forma intuitiva e transparente.

A plataforma foca em uma experiência de usuário moderna, jovial e "instagramável", com um design atraente e funcionalidades que simplificam o processo de descoberta e contratação.

## 🎯 Objetivo Principal

* Facilitar a descoberta de criadores de conteúdo adequados para campanhas de marketing de influência.
* Permitir que marcas filtrem criadores por nicho, localização, plataformas e métricas de engajamento.
* Oferecer aos criadores de conteúdo um espaço para criar uma página profissional e apresentar seu trabalho.
* Descentralizar o acesso ao marketing de influência, com funcionalidades gratuitas para pesquisa (marcas) e criação de perfil (criadores) no MVP.

## 👥 Público-Alvo

* **Marcas e Agências:** Buscando criadores de conteúdo para parcerias e campanhas publicitárias.
* **Criadores de Conteúdo Digital (Influenciadores):** Procurando visibilidade, novas oportunidades de parceria e uma forma profissional de apresentar seu trabalho e métricas.

## ✨ Principais Funcionalidades (Planejadas/Desenvolvidas no Frontend MVP)

* **Marketplace de Descoberta:** Interface para marcas encontrarem criadores.
* **Perfis Detalhados de Criadores:** Páginas ricas com informações, portfólio, métricas, público-alvo, e histórico de campanhas.
* **Busca Avançada e Filtros:** Ferramentas para refinar a busca por criadores com base em múltiplos critérios (nome, nicho, plataforma, localização, seguidores, engajamento).
* **Cadastro e Login:** Sistemas separados para Marcas e Criadores.
* **Dashboard do Criador:** Área para o criador gerenciar seu perfil e atividades na plataforma.
* **Conteúdo Informativo ("Radar INVOX"):** Seção com artigos, dicas e notícias sobre o universo do marketing de influência.

## 📄 Páginas Desenvolvidas (Estrutura HTML e CSS Principal)

* **`index.html` (Página Inicial):**
    * Hero section vibrante com CTA.
    * Seção "Criadores em Destaque" com busca avançada expansível e filtros rápidos.
    * Grade de cards de criadores com informações resumidas.
    * Seção "Como Funciona" (para a plataforma em geral).
    * Seção "Inspirações" (carrossel de criadores).
    * Banner CTA final com fundo gradiente.
* **`cadastro.html` (Página de Cadastro):**
    * Layout de duas colunas (institucional + formulário).
    * Fundo gradiente na página.
    * Seletor para tipo de conta (Marca/Criador).
    * Formulário básico (Nome, E-mail, Senha) com campo condicional "Nome da Empresa" para marcas.
    * Botão para cadastro com Google.
* **`login.html` (Página de Login):**
    * Layout e design consistentes com a página de cadastro.
    * Formulário de login (E-mail, Senha), link para "Esqueci minha senha".
    * Botão para login com Google.
* **`criadores.html` (Página de Listagem de Criadores):**
    * Cabeçalho de página com título e fundo gradiente.
    * Layout com barra lateral de filtros (busca por nome, nicho, plataforma, estado, cidade, seguidores, engajamento) e área de resultados.
    * Grade para exibir os cards de criadores.
    * Placeholder para ordenação e paginação.
* **`perfil-criador.html` (Página de Perfil do Criador):**
    * Design moderno com "Hero Section" do criador (foto, nome, bio curta, métricas chave, redes sociais, CTA de contato).
    * Navegação por abas internas (Portfólio, Métricas, Campanhas Anteriores, Contato).
    * Seções de conteúdo detalhadas:
        * Portfólio Visual (carrossel de posts).
        * Métricas e Desempenho (cards de métricas detalhadas, gráficos de barra para Público-Alvo).
        * Campanhas Anteriores (lista de campanhas com detalhes e KPIs).
        * Entre em Contato (informações de contato direto e formulário de proposta).
        * Criadores Relacionados (sugestões de outros perfis).
    * Botão Flutuante CTA.
* **`para-marcas.html` (Página Informativa para Marcas):**
    * Hero section com título, subtítulo e CTA.
    * Seção de Benefícios ("Por que usar a INVOX3?").
    * Seção "Como funciona?" para marcas.
    * CTA Final.
* **`dashboard-criador.html` (Dashboard do Criador):**
    * Header adaptado para usuário logado (com menu de perfil dropdown).
    * Layout com sidebar de navegação escura e área de conteúdo principal.
    * Seção "Visão Geral" com widgets (Complete seu Perfil, Novas Oportunidades, Métricas Rápidas, Notificações).

## 🛠️ Tecnologias Utilizadas (Frontend MVP)

* HTML5 (Estrutura semântica)
* CSS3
    * Flexbox e Grid para layouts responsivos.
    * Variáveis CSS (Custom Properties) para tema e consistência.
    * Design Responsivo (Media Queries).
    * Gradientes, Sombras, Transições e Animações sutis.
* JavaScript (Vanilla JS)
    * Manipulação do DOM.
    * Ouvintes de Eventos.
    * Interatividade básica para componentes como:
        * Toggle da Busca Avançada.
        * Seleção de Filtros Rápidos.
        * Carrosséis (Inspirações, Portfólio do Perfil).
        * Atualização em tempo real de valores de sliders.
        * Navegação por abas na página de perfil do criador.
        * Dropdown do menu de usuário no dashboard.
        * Mostrar/ocultar campos condicionais no formulário de cadastro.
* Font Awesome (para ícones)
* Google Fonts (Poppins)

## 🚦 Status Atual do Projeto

* Frontend do MVP (Minimum Viable Product) em desenvolvimento avançado.
* Principais páginas e fluxos de usuário com estrutura HTML e estilização CSS definidos.
* Interatividade básica do frontend implementada com JavaScript.

## 🚀 Próximos Passos Planejados (Geral)

* **Implementação Completa do Backend:**
    * Criação de banco de dados (usuários, perfis de criadores, campanhas, artigos, etc.).
    * Desenvolvimento de APIs para comunicação com o frontend.
    * Lógica de autenticação e autorização.
    * Implementação da lógica de busca e filtragem no servidor.
    * Sistema de gerenciamento de conteúdo para o "Radar INVOX".
* **Aprofundamento das Funcionalidades JavaScript no Frontend:**
    * Validação completa de formulários.
    * Interação dinâmica dos filtros com o backend para carregar resultados.
    * Paginação funcional.
    * Funcionalidade de "Briefing Rápido" (modal e formulário).
    * Melhorias na navegação por abas e interações do dashboard.
* **Desenvolvimento das Páginas Restantes:** FAQ, Termos de Uso, Política de Privacidade, "Para Criadores", etc.
* **Testes e Refinamentos:** Testes de usabilidade, responsividade em mais dispositivos, otimizações de performance.
* **SEO Técnico e de Conteúdo.**

## 🏃 Como Visualizar (Ambiente de Desenvolvimento Estático)

1.  Clone ou baixe os arquivos do projeto.
2.  Certifique-se de que a estrutura de pastas está correta (ex: pasta `css` com `style.css`, pasta `js` se houver scripts externos, pasta `img` para imagens locais).
3.  Abra os arquivos `.html` diretamente em um navegador web moderno (Google Chrome, Firefox, Edge, etc.).

---