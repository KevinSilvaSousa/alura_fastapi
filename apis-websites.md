API
aplication programing interface
Interface de programação de aplicações

GET /status
    json = {"status": "ok"}
    xml = <status>ok</status>

POST /cliente
nome = string
idade = number
{"nome": "raphael", "idade": 30}



O WSGI (Web Server Gateway Interface) é o padrão tradicional usado por frameworks como Flask e Django. Ele foi criado em 2003 e funciona de forma síncrona: cada requisição é processada completamente antes que a próxima possa começar. É como um atendente de loja que precisa terminar de atender completamente um cliente antes de poder ajudar o próximo, mesmo que o primeiro cliente esteja apenas esperando o cartão de crédito ser aprovado. Esse modelo funcionou bem por anos, mas com o crescimento de aplicações que precisam lidar com milhares de conexões simultâneas (como chats em tempo real, streaming de dados, ou microsserviços), suas limitações ficaram evidentes.

Já o ASGI (Asynchronous Server Gateway Interface) é o sucessor moderno do WSGI, criado especificamente para suportar operações assíncronas, WebSockets e HTTP/2. Com ASGI, o servidor pode lidar com múltiplas requisições simultaneamente, alternando entre elas quando uma está esperando por algo (como uma resposta do banco de dados). Voltando à analogia da loja: é como ter um atendente que, enquanto espera a aprovação do cartão de um cliente, pode começar a atender outro, maximizando o uso do tempo. O Uvicorn é um servidor ASGI extremamente rápido que permite ao FastAPI explorar todo esse potencial, sendo construído sobre uvloop (uma implementação mais rápida do event loop do Python) e httptools (para parsing HTTP eficiente).