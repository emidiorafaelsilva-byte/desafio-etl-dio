import pandas as pd

# =========================
# EXTRACT
# =========================

print("Iniciando etapa EXTRACT...")

df = pd.read_csv("SDW2023_clientes.csv")

print("\nDados originais:")
print(df.head())

# =========================
# TRANSFORM
# =========================

print("\nIniciando etapa TRANSFORM...")

# Criando uma nova coluna com classificação financeira
def classificar_cliente(saldo):
    if saldo >= 5000:
        return "Premium"
    elif saldo >= 2000:
        return "Intermediário"
    else:
        return "Básico"

df["CategoriaCliente"] = df["Saldo"].apply(classificar_cliente)

# Criando mensagem personalizada
df["Mensagem"] = (
    "Olá " + df["Nome"] +
    ", conheça oportunidades de investimento para seu perfil "
    + df["PerfilInvestidor"]
)

print("\nDados transformados:")
print(df.head())

# =========================
# LOAD
# =========================

print("\nIniciando etapa LOAD...")

arquivo_saida = "clientes_transformados.xlsx"

df.to_excel(arquivo_saida, index=False)

print(f"\nArquivo salvo com sucesso: {arquivo_saida}")

print("\nPipeline ETL finalizado com sucesso!")
