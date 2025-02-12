Autenticação de Dois Fatores (2FA) com Python
Este projeto demonstra como implementar a Autenticação de Dois Fatores (2FA) em Python, aumentando a segurança dos sistemas ao exigir um código gerado dinamicamente a cada 30 segundos. A solução utiliza Google Authenticator ou aplicativos similares para validar o acesso dos usuários.

📌 Recursos do Projeto
✅ Geração e validação de códigos TOTP (Time-based One-Time Password)
✅ Criação de QR Codes para fácil configuração em aplicativos autenticadores
✅ Implementação simples e segura utilizando bibliotecas otimizadas

🛠 Tecnologias Utilizadas
Python 3.x
pyotp – Geração e verificação de códigos TOTP
qrcode – Criação de QR Codes para sincronização
time – Controle do tempo para geração dos códigos
🚀 Como Funciona
1️⃣ O sistema gera uma chave secreta única para cada usuário.
2️⃣ Essa chave é convertida em um QR Code, permitindo a leitura e sincronização com o Google Authenticator.
3️⃣ O aplicativo autenticador gera códigos de 6 dígitos, que mudam a cada 30 segundos.
4️⃣ O usuário insere o código gerado, e o sistema valida se ele corresponde ao código esperado.

▶️ Como Executar o Projeto
1️⃣ Clone o repositório:

bash
Copy
Edit
git clone https://github.com/seuusuario/projeto-2fa.git
cd projeto-2fa
2️⃣ Instale as dependências:

bash
Copy
Edit
pip install pyotp qrcode[pil]
3️⃣ Execute o script:

bash
Copy
Edit
python main.py
🔗 Demonstração do QR Code
Ao rodar o código, um QR Code será gerado. Basta escaneá-lo com o Google Authenticator para começar a receber códigos de autenticação.

🔒 Por que Usar 2FA?
A autenticação de dois fatores reduz drasticamente o risco de acesso não autorizado, tornando o login mais seguro, mesmo se a senha do usuário for comprometida.

💡 Melhore a segurança do seu sistema com 2FA!

📌 Dúvidas ou sugestões? Contribua no repositório! 🚀